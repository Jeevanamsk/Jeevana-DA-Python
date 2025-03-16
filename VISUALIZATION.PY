import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D
from matplotlib_venn import venn3

# Load dataset
df = pd.read_csv("Flipkart_Mobiles.csv")

# Handle missing values
df.dropna(inplace=True)

# Convert price columns to numeric if applicable
df['Selling Price'] = pd.to_numeric(df['Selling Price'], errors='coerce')
df['Original Price'] = pd.to_numeric(df['Original Price'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

# 1. Line Plot - Selling Price Trend
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Selling Price'], marker='o', linestyle='-', color='b')
plt.title("Selling Price Trend")
plt.xlabel("Index")
plt.ylabel("Selling Price")
plt.show()

# 2. Bar Plot - Brand Distribution
plt.figure(figsize=(12, 6))
# fig = plt.figure(figsize=(10, 6))
# fig.canvas.manager.set_window_title("Bar plot")
df['Brand'].value_counts().plot(kind='bar', color='g')
plt.title("Brand Distribution")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 3. Histogram - Selling Price Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Selling Price'], bins=20, kde=True, color='orange')
plt.title("Selling Price Distribution")
plt.show()

# 4. Scatter Plot - Ratings vs Selling Price
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['Rating'], y=df['Selling Price'], alpha=0.5, color='red')
plt.title("Rating vs Selling Price")
plt.xlabel("Rating")
plt.ylabel("Selling Price")
plt.show()

# 5. 3D Scatter Plot - Selling Price vs Original Price vs Ratings
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['Selling Price'], df['Original Price'], df['Rating'], c='purple', alpha=0.6)
ax.set_xlabel("Selling Price")
ax.set_ylabel("Original Price")
ax.set_zlabel("Rating")
plt.title("3D Scatter Plot")
plt.show()

# 6. Box Plot - Selling Price by Brand
plt.figure(figsize=(12, 6))
sns.boxplot(x=df['Brand'], y=df['Selling Price'])
plt.xticks(rotation=45)
plt.title("Selling Price Distribution by Brand")
plt.show()

# 7. Violin Plot - Selling Price by Brand
plt.figure(figsize=(12, 6))
sns.violinplot(x=df['Brand'], y=df['Selling Price'])
plt.xticks(rotation=45)
plt.title("Selling Price Violin Plot by Brand")
plt.show()

# Create a figure and set its name
# fig = plt.figure(figsize=(10, 6))
# fig.canvas.manager.set_window_title("Correlation Heatmap")
# Select only numeric columns
numeric_df = df.select_dtypes(include=[float, int])
# Plot Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()


# 9. Word Cloud - Brand Frequency
text = " ".join(df['Brand'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Brand Word Cloud")
plt.show()

# 10. Pie Chart - Brand Distribution
plt.figure(figsize=(8, 8))
df['Brand'].value_counts().head(10).plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='tab10')
plt.title("Top 10 Brands Distribution")
plt.ylabel("")
plt.show()

# 11. Bubble Plot - Selling Price vs Ratings (Size = Original Price)
plt.figure(figsize=(10, 6))
plt.scatter(df['Rating'], df['Selling Price'], s=df['Original Price'] / 100, alpha=0.5, color='cyan', edgecolors='black')
plt.title("Bubble Plot - Selling Price vs Ratings")
plt.xlabel("Rating")
plt.ylabel("Selling Price")
plt.show()

# 12. Treemap - Brand Distribution
plt.figure(figsize=(10, 6))
sizes = df['Brand'].value_counts().values
labels = df['Brand'].value_counts().index
squarify.plot(sizes=sizes, label=labels, alpha=0.7)
plt.axis("off")
plt.title("Brand Distribution Treemap")
plt.show()

# 13. Venn Diagram (Assuming three top brands exist)
top_brands = df['Brand'].value_counts().index[:3]
if len(top_brands) >= 3:
    set1 = set(df[df['Brand'] == top_brands[0]].index)
    set2 = set(df[df['Brand'] == top_brands[1]].index)
    set3 = set(df[df['Brand'] == top_brands[2]].index)

    plt.figure(figsize=(5, 5))
    venn3([set1, set2, set3], set_labels=top_brands[:3])
    plt.title("Venn Diagram of Top 3 Brands")
    plt.show()

print("All visualizations generated successfully!")
