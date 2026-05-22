# Sales Data Analysis
# Author: Tanishk Verma
# Tools: Python, Pandas, Matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ================================
# STEP 1: Load Data
# ================================
df = pd.read_csv('sales_data.csv')
print("Dataset loaded successfully!")
print(f"Total Records: {len(df)}")
print(f"\nFirst 5 rows:\n{df.head()}")

# ================================
# STEP 2: Basic Info
# ================================
print("\n--- Dataset Info ---")
print(df.info())
print("\n--- Summary Statistics ---")
print(df.describe())

# ================================
# STEP 3: Key Insights
# ================================
print("\n--- KEY BUSINESS INSIGHTS ---")

# Total Revenue
total_revenue = df['Total_Sales'].sum()
print(f"Total Revenue: ₹{total_revenue:,}")

# Best Selling Category
best_category = df.groupby('Category')['Total_Sales'].sum().idxmax()
print(f"Best Selling Category: {best_category}")

# Best Region
best_region = df.groupby('Region')['Total_Sales'].sum().idxmax()
print(f"Best Performing Region: {best_region}")

# Best Product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
print(f"Top Selling Product: {best_product}")

# ================================
# STEP 4: Visualizations
# ================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sales Data Analysis - Tanishk Verma', fontsize=16, fontweight='bold')

# Chart 1: Sales by Category
category_sales = df.groupby('Category')['Total_Sales'].sum()
axes[0, 0].bar(category_sales.index, category_sales.values, color=['#2196F3', '#4CAF50', '#FF9800'])
axes[0, 0].set_title('Total Sales by Category')
axes[0, 0].set_xlabel('Category')
axes[0, 0].set_ylabel('Total Sales (₹)')
for i, v in enumerate(category_sales.values):
    axes[0, 0].text(i, v + 5000, f'₹{v:,}', ha='center', fontsize=9)

# Chart 2: Sales by Region
region_sales = df.groupby('Region')['Total_Sales'].sum()
colors = ['#E91E63', '#9C27B0', '#00BCD4', '#8BC34A']
axes[0, 1].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%', colors=colors)
axes[0, 1].set_title('Sales Distribution by Region')

# Chart 3: Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%b %Y')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
axes[1, 0].plot(range(len(monthly_sales)), monthly_sales.values, marker='o', color='#2196F3', linewidth=2)
axes[1, 0].set_xticks(range(len(monthly_sales)))
axes[1, 0].set_xticklabels(monthly_sales.index, rotation=45, ha='right', fontsize=8)
axes[1, 0].set_title('Monthly Sales Trend')
axes[1, 0].set_ylabel('Total Sales (₹)')
axes[1, 0].grid(True, alpha=0.3)

# Chart 4: Top 5 Products
product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=True)
axes[1, 1].barh(product_sales.index, product_sales.values, color='#4CAF50')
axes[1, 1].set_title('Sales by Product')
axes[1, 1].set_xlabel('Total Sales (₹)')

plt.tight_layout()
plt.savefig('sales_analysis_charts.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nCharts saved as 'sales_analysis_charts.png'")
print("\nAnalysis Complete! ✅")
