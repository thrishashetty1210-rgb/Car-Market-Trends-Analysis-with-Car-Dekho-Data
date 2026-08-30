import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("car_data.csv")

print("========== VEHICLE DATA ANALYSIS ==========")

print("\n1. Manufacturing Year Range")
oldest_year = df["Year"].min()
newest_year = df["Year"].max()
print("Vehicles are available from", oldest_year, "to", newest_year)


print("\n2. Lowest Selling Price")
lowest_price = df["Selling_Price"].min()
print("Lowest Selling Price:", lowest_price)
print(df[df["Selling_Price"] == lowest_price])


print("\n3. Highest Selling Price")
highest_price = df["Selling_Price"].max()
print("Highest Selling Price:", highest_price)
print(df[df["Selling_Price"] == highest_price])


print("\n4. Total Number of Records")
total_records = df.shape[0]
print("Total Records:", total_records)


print("\n5. Missing Values")
missing_values = df.isnull().sum()
print(missing_values)
total_missing = df.isnull().sum().sum()
print("Total Missing Values:", total_missing)


print("\n6. Number of Different Vehicles")
different_vehicles = df["Car_Name"].nunique()
print("Number of Different Vehicles:", different_vehicles)


print("\n7. Most Sold Vehicle")
vehicle_count = df["Car_Name"].value_counts()
most_sold_vehicle = vehicle_count.idxmax()
sales_count = vehicle_count.max()
print("Most Sold Vehicle:", most_sold_vehicle)
print("Number of Times Sold:", sales_count)


print("\n8. CNG Vehicles")
cng_vehicles = df[df["Fuel_Type"] == "CNG"]
print("Number of CNG Vehicles:", len(cng_vehicles))
print(cng_vehicles)


print("\n9. Vehicles Sold by Individuals")
individual_vehicles = df[df["Seller_Type"] == "Individual"]
print("Number of Vehicles Sold by Individuals:", len(individual_vehicles))


print("\n10. Automatic Transmission Vehicles")
automatic_vehicles = df[df["Transmission"] == "Automatic"]
print("Number of Automatic Vehicles:", len(automatic_vehicles))


print("\n11. Single Owner Vehicles")
single_owner = df[df["Owner"] == 0]
print("Number of Single Owner Vehicles:", len(single_owner))


df["Depreciation"] = df["Present_Price"] - df["Selling_Price"]
df["Depreciation_Percentage"] = (df["Depreciation"] / df["Present_Price"]) * 100


print("\n12. Most Depreciated Vehicle")
most_depreciated = df.loc[df["Depreciation"].idxmax()]
print(most_depreciated[
    [
        "Car_Name",
        "Year",
        "Present_Price",
        "Selling_Price",
        "Depreciation",
        "Depreciation_Percentage"]])
print("\nLeast Depreciated Vehicle")
least_depreciated = df.loc[df["Depreciation"].idxmin()]
print(least_depreciated[
    [
        "Car_Name",
        "Year",
        "Present_Price",
        "Selling_Price",
        "Depreciation",
        "Depreciation_Percentage"
    ]
])


print("\n13. Vehicles Less Affected by Depreciation")
vehicle_depreciation = df.groupby("Car_Name")["Depreciation_Percentage"].mean()
vehicle_depreciation = vehicle_depreciation.sort_values()
print(vehicle_depreciation.head(10))
print("\n14. Factors Affecting Depreciation")
CURRENT_YEAR = 2026
df["Vehicle_Age"] = CURRENT_YEAR - df["Year"]
numeric_columns = [
    "Selling_Price",
    "Present_Price",
    "Kms_Driven",
    "Vehicle_Age",
    "Owner",
    "Depreciation"
]
correlation = df[numeric_columns].corr()
print(correlation)


print("\n15. Effect of Age and Distance on Selling Price")
price_correlation = df[
    [
        "Selling_Price",
        "Vehicle_Age",
        "Kms_Driven"    ]].corr()
print(price_correlation)
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Vehicle_Age"],
    df["Selling_Price"]
)
plt.xlabel("Vehicle Age")
plt.ylabel("Selling Price")
plt.title("Vehicle Age vs Selling Price")
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Kms_Driven"],
    df["Selling_Price"]
)
plt.xlabel("Kilometers Driven")
plt.ylabel("Selling Price")
plt.title("Kilometers Driven vs Selling Price")
plt.show()


print("\n16. Vehicles Manufactured After 2014")
new_vehicles = df[df["Year"] > 2014]
print(new_vehicles)
print("Number of Vehicles After 2014:", len(new_vehicles))
bike_keywords = [
    "Royal Enfield",
    "KTM",
    "Bajaj",
    "Yamaha",
    "Hero",
    "TVS",
    "Activa",
    "Honda CB",
    "Honda CBR",
    "Hyosung",
    "UM"
]
def vehicle_type(name):
    name = str(name).lower()
    for bike in bike_keywords:
        if bike.lower() in name:
            return "Bike"
    return "Car"
df["Vehicle_Type"] = df["Car_Name"].apply(vehicle_type)
print("\n17. Two-Wheelers Only")
two_wheelers = df[df["Vehicle_Type"] == "Bike"]
print(two_wheelers)
print("Number of Two-Wheelers:", len(two_wheelers))


print("\n18. Oldest Bike")
oldest_bike_year = two_wheelers["Year"].min()
oldest_bike = two_wheelers[
    two_wheelers["Year"] == oldest_bike_year]
print(oldest_bike[
    [
        "Car_Name",
        "Year",
        "Selling_Price",
        "Kms_Driven"]])


print("\n19. Newest Bike")
newest_bike_year = two_wheelers["Year"].max()
newest_bike = two_wheelers[two_wheelers["Year"] == newest_bike_year]
print(newest_bike[
    [
        "Car_Name",
        "Year",
        "Selling_Price",
        "Kms_Driven" ]])


print("\n20. Most Sold Bike")
bike_count = two_wheelers["Car_Name"].value_counts()
most_sold_bike = bike_count.idxmax()
most_sold_bike_count = bike_count.max()
print("Most Sold Bike:", most_sold_bike)
print("Number of Times Sold:", most_sold_bike_count)


print("\n21. Two-Wheelers Exceeding General Price Expectations")
Q1 = two_wheelers["Selling_Price"].quantile(0.25)
Q3 = two_wheelers["Selling_Price"].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + (1.5 * IQR)
exceptional_bikes = two_wheelers[ two_wheelers["Selling_Price"] > upper_limit]
print("General Upper Price Limit:", upper_limit)
print(exceptional_bikes[
    [
        "Car_Name",
        "Year",
        "Selling_Price",
        "Present_Price",
        "Kms_Driven"
    ]
])


print("\n22. Cars Only")
cars = df[df["Vehicle_Type"] == "Car"]
print(cars)
print("Number of Cars:", len(cars))


print("\n23. Oldest Car")
oldest_car_year = cars["Year"].min()
oldest_car = cars[cars["Year"] == oldest_car_year]
print(oldest_car[
    [
        "Car_Name",
        "Year",
        "Selling_Price",
        "Kms_Driven"
    ]
])


print("\n24. Newest Car")
newest_car_year = cars["Year"].max()
newest_car = cars[cars["Year"] == newest_car_year]
print(newest_car[
    [
        "Car_Name",
        "Year",
        "Selling_Price",
        "Kms_Driven"
    ]
])


print("\n25. Cars Exceeding General Price Expectations")
Q1 = cars["Selling_Price"].quantile(0.25)
Q3 = cars["Selling_Price"].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + (1.5 * IQR)
exceptional_cars = cars[cars["Selling_Price"] > upper_limit]
print("General Upper Price Limit:", upper_limit)
print(exceptional_cars[
    [
        "Car_Name",
        "Year",
        "Selling_Price",
        "Present_Price",
        "Kms_Driven",
        "Transmission"
    ]
])

print("\n========== ANALYSIS COMPLETED ==========")