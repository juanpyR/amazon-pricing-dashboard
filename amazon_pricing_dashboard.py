import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up page layout and styling
st.set_page_config(layout="wide")
sns.set_style("whitegrid")

# Cache data loading for performance
@st.cache(allow_output_mutation=True)
def load_data(file) -> pd.DataFrame:
    """
    Load the CSV file into a DataFrame, preprocess columns,
    and calculate additional fields like margin, revenue, and profit.
    """
    df = pd.read_csv(file)
    df.columns = df.columns.str.lower()  # normalize column names
    # Drop rows with missing essential values
    df = df.dropna(subset=['price', 'cost', 'units_sold', 'category', 'brand'])
    # Calculate extra fields
    df['margin'] = df['price'] - df['cost']
    df['revenue'] = df['price'] * df['units_sold']
    df['profit'] = df['margin'] * df['units_sold']
    return df

def compute_metrics(df):
    """
    Calculate key business metrics from the dataframe.
    Returns a dictionary with metric names and values.
    """
    metrics = {
        'Total Revenue': df['revenue'].sum(),
        'Total Profit': df['profit'].sum(),
        'Total Units Sold': df['units_sold'].sum(),
        'Average Price': df['price'].mean(),
        'Median Price': df['price'].median(),
        'Price Min': df['price'].min(),
        'Price Max': df['price'].max(),
        'Average Margin': df['margin'].mean(),
        'Number of Products': df['title'].nunique() if 'title' in df.columns else df.shape[0],
        'Number of Unique Brands': df['brand'].nunique(),
        'Average Rating': df['rating'].mean() if 'rating' in df.columns else np.nan,
        'Average Reviews per Product': df['reviews_count'].mean() if 'reviews_count' in df.columns else np.nan,
        'Products with Rating > 4 (%)': (df['rating'] > 4).mean() * 100 if 'rating' in df.columns else np.nan,
    }
    
    # Best product by profit
    if 'profit' in df.columns and 'title' in df.columns:
        max_profit_row = df.loc[df['profit'].idxmax()]
        metrics['Best Product by Profit'] = f"{max_profit_row['title']} (${max_profit_row['profit']:.2f})"
    else:
        metrics['Best Product by Profit'] = 'N/A'
    
    # Best product by rating
    if 'rating' in df.columns and 'title' in df.columns:
        max_rating_row = df.loc[df['rating'].idxmax()]
        metrics['Best Product by Rating'] = f"{max_rating_row['title']} ({max_rating_row['rating']:.1f})"
    else:
        metrics['Best Product by Rating'] = 'N/A'

    # Top 3 categories by units sold
    top_categories = df.groupby('category')['units_sold'].sum().sort_values(ascending=False).head(3)
    metrics['Top 3 Categories by Units Sold'] = ', '.join(top_categories.index)

    return metrics

def plot_units_sold_by_category(df):
    """
    Bar plot of total units sold per category.
    """
    data = df.groupby('category')['units_sold'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=data.index, y=data.values, ax=ax)
    ax.set_title("Units Sold by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Units Sold")
    plt.xticks(rotation=45)
    return fig

def plot_profit_by_brand(df):
    """
    Bar plot of total profit per brand, showing top 15 brands.
    """
    data = df.groupby('brand')['profit'].sum().sort_values(ascending=False).head(15)
    fig, ax = plt.subplots(figsize=(10,5))
    sns.barplot(x=data.index, y=data.values, ax=ax)
    ax.set_title("Profit by Brand (Top 15)")
    ax.set_xlabel("Brand")
    ax.set_ylabel("Profit")
    plt.xticks(rotation=45)
    return fig

def plot_margin_vs_price(df):
    """
    Scatter plot of margin vs price, colored by brand and sized by units sold.
    """
    fig, ax = plt.subplots(figsize=(10,5))
    sns.scatterplot(data=df, x='price', y='margin', hue='brand', size='units_sold',
                    sizes=(20, 200), alpha=0.7, ax=ax, legend=False)
    ax.set_title("Margin vs Price")
    ax.set_xlabel("Price")
    ax.set_ylabel("Margin")
    plt.xticks(rotation=45)
    return fig

def plot_rating_distribution(df):
    """
    Histogram of product ratings, if ratings are available.
    """
    if 'rating' in df.columns:
        fig, ax = plt.subplots(figsize=(8,4))
        sns.histplot(df['rating'], bins=10, kde=False, ax=ax)
        ax.set_title("Rating Distribution")
        ax.set_xlabel("Rating")
        ax.set_ylabel("Number of Products")
        return fig
    else:
        return None

def main():
    st.title("📊 Amazon Products Dashboard")

    # File uploader for CSV
    uploaded_file = st.file_uploader("Upload your Amazon products CSV file", type=["csv"])
    if uploaded_file:
        df = load_data(uploaded_file)

        # Calculate and display metrics
        metrics = compute_metrics(df)
        st.markdown("### 📈 Key Metrics")
        cols = st.columns(4)
        numeric_metrics = ['Total Revenue', 'Total Profit', 'Total Units Sold', 'Average Price', 
                           'Median Price', 'Price Min', 'Price Max', 'Average Margin', 
                           'Number of Products', 'Number of Unique Brands', 'Average Rating', 
                           'Average Reviews per Product', 'Products with Rating > 4 (%)']

        for i, metric_name in enumerate(numeric_metrics):
            val = metrics.get(metric_name, np.nan)
            if not np.isnan(val):
                if 'Units' in metric_name or 'Number' in metric_name or 'Products with' in metric_name:
                    cols[i % 4].metric(metric_name, f"{val:,.0f}")
                else:
                    cols[i % 4].metric(metric_name, f"${val:,.2f}")

        # Display textual metrics separately
        st.markdown(f"**Best Product by Profit:** {metrics['Best Product by Profit']}")
        st.markdown(f"**Best Product by Rating:** {metrics['Best Product by Rating']}")
        st.markdown(f"**Top 3 Categories by Units Sold:** {metrics['Top 3 Categories by Units Sold']}")

        st.markdown("---")
        st.markdown("### 🎯 Filters")

        # Filters for category, brand, price range
        categories = df['category'].unique()
        brands = df['brand'].unique()
        price_min, price_max = float(df['price'].min()), float(df['price'].max())

        selected_categories = st.multiselect("Categories", categories, default=list(categories))
        selected_brands = st.multiselect("Brands", brands, default=list(brands))
        selected_price = st.slider("Price Range", price_min, price_max, (price_min, price_max))

        # Filter dataframe based on user selection
        df_filtered = df[
            df['category'].isin(selected_categories) &
            df['brand'].isin(selected_brands) &
            df['price'].between(selected_price[0], selected_price[1])
        ]

        st.markdown(f"##### 🔎 Showing {len(df_filtered)} filtered products")
        st.dataframe(df_filtered.head(10))

        st.markdown("---")
        col1, col2 = st.columns(2)

        # Show plots side by side
        with col1:
            st.pyplot(plot_units_sold_by_category(df_filtered))
            fig_rating = plot_rating_distribution(df_filtered)
            if fig_rating:
                st.pyplot(fig_rating)

        with col2:
            st.pyplot(plot_profit_by_brand(df_filtered))
            st.pyplot(plot_margin_vs_price(df_filtered))

        st.markdown("---")
        st.markdown("### 🏆 Top 10 Most Profitable Products")
        top_products = df_filtered.sort_values('profit', ascending=False).head(10)
        st.dataframe(top_products[['title', 'brand', 'category', 'price', 'cost', 'units_sold', 'profit']])

        # Button to download filtered data as CSV
        st.markdown("---")
        st.download_button(
            label="📥 Download Filtered CSV",
            data=df_filtered.to_csv(index=False).encode('utf-8'),
            file_name='amazon_filtered_products.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
