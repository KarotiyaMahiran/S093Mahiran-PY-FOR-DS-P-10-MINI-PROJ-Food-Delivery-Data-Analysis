# ============================================================
# MINI DATA SCIENCE PROJECT
# FOOD DELIVERY DATA ANALYSIS AND DASHBOARD
# S093 MAHIRAN KAROTIYA
# ============================================================

# ============================================================
# PART 1 - IMPORT LIBRARIES
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

print("======================================================")
print("       FOOD DELIVERY DATA ANALYSIS PROJECT")
print("       S093 MAHIRAN KAROTIYA")
print("======================================================")


# ============================================================
# PART A - LOAD DATASET
# ============================================================

df = pd.read_csv("food_delivery.csv")

print("\n========== DATASET LOADED ==========")
print("Dataset loaded successfully.")


# ============================================================
# PART B - DATA LOADING AND EXPLORATION
# ============================================================

print("\n========== FIRST 5 RECORDS ==========")
print(df.head())

print("\n========== LAST 5 RECORDS ==========")
print(df.tail())

print("\n========== DATASET SHAPE ==========")
print("Rows and Columns:", df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== STATISTICAL INFORMATION ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE RECORDS ==========")
print(df.duplicated().sum())


# ============================================================
# PART C - DATA CLEANING
# ============================================================

print("\n========== DATA CLEANING ==========")

# Remove duplicate records
df = df.drop_duplicates()

# Remove spaces from column names
df.columns = df.columns.str.strip()

# Handle missing values
df["Order_Value"] = df["Order_Value"].fillna(
    df["Order_Value"].mean()
)

df["Delivery_Time"] = df["Delivery_Time"].fillna(
    df["Delivery_Time"].mean()
)

df["Rating"] = df["Rating"].fillna(
    df["Rating"].mean()
)

print("Duplicate records removed.")
print("Column names cleaned.")
print("Missing values handled.")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================================
# PART D - DATA ANALYSIS USING NUMPY AND PANDAS
# ============================================================

print("\n========== DATA ANALYSIS ==========")


# 1. Total Orders
total_orders = df["Order_ID"].count()

print("\n1. Total Orders:", total_orders)


# 2. Total Order Value
total_sales = np.sum(df["Order_Value"])

print("2. Total Order Value: ₹", round(total_sales, 2))


# 3. Average Order Value
average_order = np.mean(df["Order_Value"])

print("3. Average Order Value: ₹", round(average_order, 2))


# 4. Highest Order Value
maximum_order = np.max(df["Order_Value"])

print("4. Highest Order Value: ₹", maximum_order)


# 5. Lowest Order Value
minimum_order = np.min(df["Order_Value"])

print("5. Lowest Order Value: ₹", minimum_order)


# 6. Median Order Value
median_order = np.median(df["Order_Value"])

print("6. Median Order Value: ₹", median_order)


# 7. Average Delivery Time
average_delivery = np.mean(df["Delivery_Time"])

print(
    "7. Average Delivery Time:",
    round(average_delivery, 2),
    "minutes"
)


# 8. Average Customer Rating
average_rating = np.mean(df["Rating"])

print(
    "8. Average Customer Rating:",
    round(average_rating, 2)
)


# 9. Most Popular Food Category
category_counts = df["Food_Category"].value_counts()

popular_category = category_counts.idxmax()

print(
    "9. Most Popular Food Category:",
    popular_category
)


# 10. Best Rated Restaurant
restaurant_rating = df.groupby(
    "Restaurant"
)["Rating"].mean()

best_restaurant = restaurant_rating.idxmax()

print(
    "10. Best Rated Restaurant:",
    best_restaurant
)

print(
    "    Average Rating:",
    round(restaurant_rating.max(), 2)
)


# ============================================================
# CATEGORY-WISE SALES
# ============================================================

category_sales = df.groupby(
    "Food_Category"
)["Order_Value"].sum()

print("\n========== CATEGORY-WISE SALES ==========")
print(category_sales)


# ============================================================
# CITY-WISE ORDERS
# ============================================================

city_orders = df["City"].value_counts()

print("\n========== CITY-WISE ORDERS ==========")
print(city_orders)


# ============================================================
# RESTAURANT-WISE SALES
# ============================================================

restaurant_sales = df.groupby(
    "Restaurant"
)["Order_Value"].sum()

restaurant_sales = restaurant_sales.sort_values(
    ascending=False
)

print("\n========== RESTAURANT-WISE SALES ==========")
print(restaurant_sales)


# ============================================================
# PART E - DATA VISUALIZATION
# ============================================================

print("\n========== DATA VISUALIZATION ==========")


# ------------------------------------------------------------
# GRAPH 1 - FOOD CATEGORY-WISE SALES
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Food Category-wise Sales")
plt.xlabel("Food Category")
plt.ylabel("Total Order Value")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 2 - ORDERS BY CITY
# ------------------------------------------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    city_orders,
    labels=city_orders.index,
    autopct="%1.1f%%"
)

plt.title("Orders by City")

plt.show()


# ------------------------------------------------------------
# GRAPH 3 - ORDER VALUE DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Order_Value"],
    bins=10
)

plt.title("Order Value Distribution")
plt.xlabel("Order Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 4 - DELIVERY TIME VS CUSTOMER RATING
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Delivery_Time",
    y="Rating",
    data=df
)

plt.title("Delivery Time vs Customer Rating")
plt.xlabel("Delivery Time (Minutes)")
plt.ylabel("Customer Rating")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 5 - ORDER VALUE BY FOOD CATEGORY
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

sns.boxplot(
    x="Food_Category",
    y="Order_Value",
    data=df
)

plt.title("Order Value by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Order Value")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# GRAPH 6 - RESTAURANT-WISE SALES
# ------------------------------------------------------------

plt.figure(figsize=(9, 5))

restaurant_sales.plot(kind="bar")

plt.title("Restaurant-wise Sales")
plt.xlabel("Restaurant")
plt.ylabel("Total Order Value")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


print("\nAll 6 visualizations created successfully.")


# ============================================================
# PART F - BEAUTIFUL SOUP WEB DATA COLLECTION
# ============================================================

print("\n========== BEAUTIFUL SOUP ==========")

url = "https://quotes.toscrape.com/"

try:

    response = requests.get(
        url,
        timeout=10
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    print("\nWebsite Title:")
    print(soup.title.text)

    print("\nSample Public Web Data:")

    quotes = soup.find_all(
        "span",
        class_="text"
    )

    for i, quote in enumerate(
        quotes[:5],
        start=1
    ):
        print(
            i,
            ".",
            quote.text
        )

    print(
        "\nBeautiful Soup data collection completed."
    )

except Exception as e:

    print(
        "\nWeb data collection failed."
    )

    print(
        "Error:",
        e
    )


# ============================================================
# PART G - DASHBOARD
# ============================================================

print("\n========== CREATING DASHBOARD ==========")


# Dashboard calculations
total_orders = len(df)

total_sales = df["Order_Value"].sum()

average_order = df["Order_Value"].mean()

average_delivery = df["Delivery_Time"].mean()

average_rating = df["Rating"].mean()

category_sales = df.groupby(
    "Food_Category"
)["Order_Value"].sum()

city_orders = df["City"].value_counts()


# Create dashboard
fig = plt.figure(
    figsize=(16, 10)
)

fig.suptitle(
    "FOOD DELIVERY DATA ANALYSIS DASHBOARD",
    fontsize=22,
    fontweight="bold"
)


# ------------------------------------------------------------
# DASHBOARD SUMMARY
# ------------------------------------------------------------

fig.text(
    0.15,
    0.90,
    f"TOTAL ORDERS\n{total_orders}",
    ha="center",
    fontsize=16,
    fontweight="bold"
)

fig.text(
    0.35,
    0.90,
    f"TOTAL SALES\n₹{total_sales:,.0f}",
    ha="center",
    fontsize=16,
    fontweight="bold"
)

fig.text(
    0.55,
    0.90,
    f"AVG ORDER VALUE\n₹{average_order:,.0f}",
    ha="center",
    fontsize=16,
    fontweight="bold"
)

fig.text(
    0.75,
    0.90,
    f"AVG DELIVERY\n{average_delivery:.1f} MIN",
    ha="center",
    fontsize=16,
    fontweight="bold"
)


# ------------------------------------------------------------
# DASHBOARD CHART 1
# ------------------------------------------------------------

ax1 = fig.add_axes(
    [0.07, 0.50, 0.40, 0.30]
)

category_sales.plot(
    kind="bar",
    ax=ax1
)

ax1.set_title(
    "Sales by Food Category"
)

ax1.set_xlabel(
    "Food Category"
)

ax1.set_ylabel(
    "Order Value"
)

ax1.tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# DASHBOARD CHART 2
# ------------------------------------------------------------

ax2 = fig.add_axes(
    [0.55, 0.50, 0.35, 0.30]
)

ax2.pie(
    city_orders,
    labels=city_orders.index,
    autopct="%1.1f%%"
)

ax2.set_title(
    "Orders by City"
)


# ------------------------------------------------------------
# DASHBOARD CHART 3
# ------------------------------------------------------------

ax3 = fig.add_axes(
    [0.07, 0.12, 0.40, 0.28]
)

ax3.hist(
    df["Order_Value"],
    bins=10
)

ax3.set_title(
    "Order Value Distribution"
)

ax3.set_xlabel(
    "Order Value"
)

ax3.set_ylabel(
    "Frequency"
)


# ------------------------------------------------------------
# DASHBOARD CHART 4
# ------------------------------------------------------------

ax4 = fig.add_axes(
    [0.55, 0.12, 0.35, 0.28]
)

sns.scatterplot(
    x="Delivery_Time",
    y="Rating",
    data=df,
    ax=ax4
)

ax4.set_title(
    "Delivery Time vs Rating"
)

ax4.set_xlabel(
    "Delivery Time (Minutes)"
)

ax4.set_ylabel(
    "Customer Rating"
)


# ------------------------------------------------------------
# SAVE DASHBOARD
# ------------------------------------------------------------

plt.savefig(
    "dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nDashboard created successfully!")

print(
    "Dashboard saved as: dashboard.png"
)


# ============================================================
# PART H - KEY FINDINGS
# ============================================================

print("\n==============================================")
print("                 KEY FINDINGS")
print("==============================================")


# Finding 1
print(
    "1. Most popular food category:",
    df["Food_Category"].value_counts().idxmax()
)


# Finding 2
print(
    "2. City with highest number of orders:",
    df["City"].value_counts().idxmax()
)


# Finding 3
print(
    "3. Highest order value: ₹",
    df["Order_Value"].max()
)


# Finding 4
print(
    "4. Average delivery time:",
    round(
        df["Delivery_Time"].mean(),
        2
    ),
    "minutes"
)


# Finding 5
print(
    "5. Average customer rating:",
    round(
        df["Rating"].mean(),
        2
    )
)


# ============================================================
# PROJECT COMPLETED
# ============================================================

print("\n==============================================")
print("          PROJECT ANALYSIS COMPLETED")
print("          S093 MAHIRAN KAROTIYA")
print("==============================================")
