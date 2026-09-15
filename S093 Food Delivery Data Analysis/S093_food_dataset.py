import pandas as pd
import random

random.seed(10)

restaurants = [
    "Spice Hub", "Pizza Point", "Burger House",
    "Tasty Bites", "Food Corner", "Royal Kitchen",
    "Cafe Delight", "South Indian Cafe"
]

categories = [
    "Indian", "Pizza", "Burger",
    "Chinese", "South Indian", "Dessert"
]

cities = [
    "Mumbai", "Pune", "Delhi",
    "Bangalore", "Nashik"
]

customers = [
    "Aarav", "Riya", "Kunal", "Rishi",
    "Aditya", "Sneha", "Rahul", "Priya",
    "Neha", "Vikas"
]

data = []

for i in range(1, 151):

    restaurant = random.choice(restaurants)
    category = random.choice(categories)
    city = random.choice(cities)
    customer = random.choice(customers)

    order_value = random.randint(150, 2000)
    delivery_time = random.randint(20, 90)
    rating = round(random.uniform(2.5, 5.0), 1)

    data.append([
        i,
        customer,
        restaurant,
        category,
        city,
        order_value,
        delivery_time,
        rating
    ])

df = pd.DataFrame(data, columns=[
    "Order_ID",
    "Customer",
    "Restaurant",
    "Food_Category",
    "City",
    "Order_Value",
    "Delivery_Time",
    "Rating"
])

df.to_csv("food_delivery.csv", index=False)

print("==========================================")
print("FOOD DELIVERY DATASET CREATED")
print("S093 MAHIRAN KAROTIYA")
print("==========================================")

print("\nDataset Shape:", df.shape)

print("\nFirst 5 Records:")
print(df.head())

print("\nCSV file saved as: food_delivery.csv")
