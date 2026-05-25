# ==============================================================================
# DEVELOPERS HUB CORPORATION (DHC)
# Advanced Data Science & Analytics Internship
# TASK 5: Interactive Streamlit Business Intelligence Dashboard
# ==============================================================================

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration Setup
st.set_page_config(page_title="DHC Global Superstore Analytics", layout="wide", initial_sidebar_state="expanded")

st.title("📊 Global Superstore Business Intelligence Dashboard")
st.markdown("Developed under the operational mandate of **Developers Hub Corporation (DHC)**")

# 2. Data Loading & Cleaning Phase
@st.cache_data
def load_and_clean_data():
    # Read CSV dataset safely
    df = pd.read_csv('Global_Superstore.csv')
    return df

try:
    df = load_and_clean_data()
except Exception as e:
    st.error(f"Failed to find or parse 'Global_Superstore.csv'. Details: {e}")
    st.stop()

# 3. Sidebar Filtering Implementation
st.sidebar.header("🎯 Dashboard Interactive Filters")

# Filter A: Region Multi-select
all_regions = sorted(df['Region'].unique().tolist())
selected_regions = st.sidebar.multiselect("Select Target Region(s):", options=all_regions, default=all_regions)

# Filter B: Category Multi-select
all_categories = sorted(df['Category'].unique().tolist())
selected_categories = st.sidebar.multiselect("Select Product Category:", options=all_categories, default=all_categories)

# Filter C: Sub-Category Multi-select (Dynamically filters based on selected categories)
sub_df_temp = df[df['Category'].isin(selected_categories)]
all_sub_categories = sorted(sub_df_temp['Sub-Category'].unique().tolist())
selected_subs = st.sidebar.multiselect("Select Product Sub-Category:", options=all_sub_categories, default=all_sub_categories)

# Apply active filters to the core dataframe slice
filtered_df = df[
    (df['Region'].isin(selected_regions)) &
    (df['Category'].isin(selected_categories)) &
    (df['Sub-Category'].isin(selected_subs))
]

# 4. KPI Scorecards Metric Blocks
st.markdown("### 📈 Key Performance Indicators (KPIs)")
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

with kpi_col1:
    st.metric(label="💰 Total Revenue / Sales", value=f"${total_sales:,.2f}")
with kpi_col2:
    st.metric(label="📊 Cumulative Operational Profit", value=f"${total_profit:,.2f}", delta=f"{profit_margin:.2f}% Margin")
with kpi_col3:
    st.metric(label="📦 Total Items Handled (Volume)", value=f"{len(filtered_df):,}")

st.markdown("---")

# 5. Visualizations Rows Configuration
viz_col1, viz_col2 = st.columns(2)

with viz_col1:
    st.markdown("#### 🗺️ Financial Performance Distribution by Region")
    region_summary = filtered_df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
    fig_region = px.bar(region_summary, x='Region', y=['Sales', 'Profit'], 
                        barmode='group', title="Sales vs Profit breakdown across Regions",
                        color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_region, use_container_width=True)

with viz_col2:
    st.markdown("#### 🍰 Product Category Market Share Matrix")
    cat_summary = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    fig_pizza = px.pie(cat_summary, values='Sales', names='Category', hole=0.4,
                       title="Revenue Weight Share by Product Category",
                       color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_pizza, use_container_width=True)

# 6. Top 5 Target Customers Section
st.markdown("---")
st.markdown("#### 🏆 Top 5 Customer Accounts by Sales Volume")

customer_summary = filtered_df.groupby('Customer Name')[['Sales', 'Profit']].sum().reset_index()
top_5_customers = customer_summary.sort_values(by='Sales', ascending=False).head(5)

cust_col1, cust_col2 = st.columns([2, 1])

with cust_col1:
    fig_cust = px.bar(top_5_customers, x='Sales', y='Customer Name', orientation='h',
                      title="Highest Contributing Valued Accounts (USD)",
                      color='Profit', color_continuous_scale='Viridis', text_auto='.2s')
    fig_cust.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_cust, use_container_width=True)

with cust_col2:
    st.markdown("**Leaderboard Raw Matrix Preview:**")
    st.dataframe(top_5_customers.reset_index(drop=True), use_container_width=True)

st.success("🎯 Live Analytics Feed Active. Adjust inputs in the sidebar to dynamically re-calculate metrics.")
