# Car-Market-Trends-Analysis-with-Car-Dekho-Data

# Car Market Trends Analysis Using Car Dekho Dataset

##  Project Overview

This project focuses on analyzing used vehicle data from the **Car Dekho dataset** using Python and exploratory data analysis techniques.

The main purpose of the project is to identify useful patterns in vehicle prices, age, kilometres driven, depreciation, fuel type, transmission, seller type, and ownership.

The analysis contains **25 different questions** that provide insights into the vehicle market and resale prices.

## Objectives

The project aims to:

* Analyze the manufacturing years of vehicles
* Find the highest and lowest selling prices
* Identify the most frequently sold vehicles
* Analyze CNG vehicles
* Identify vehicles sold by individual sellers
* Analyze automatic transmission vehicles
* Find single-owner vehicles
* Calculate vehicle depreciation
* Study factors affecting depreciation
* Analyze the relationship between vehicle age and selling price
* Analyze the relationship between kilometres driven and selling price
* Separate cars and two-wheelers
* Identify the oldest and newest cars and bikes
* Find the most frequently sold bike
* Detect vehicles with unusually high selling prices

## Dataset

The project uses the **Car Dekho vehicle dataset**.

The dataset contains **301 vehicle records** with attributes such as:

* `Car_Name` – Name of the vehicle
* `Year` – Manufacturing year
* `Selling_Price` – Selling price of the vehicle
* `Present_Price` – Current/market price
* `Kms_Driven` – Kilometres driven
* `Fuel_Type` – Fuel used by the vehicle
* `Seller_Type` – Type of seller
* `Transmission` – Manual or Automatic
* `Owner` – Number of previous owners

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook / VS Code**

### Libraries

```bash
pip install pandas numpy matplotlib
```

---

## 🔍 Analysis Performed

The program performs 25 different analyses, including:

### Vehicle Analysis

1. Manufacturing year range
2. Lowest selling price
3. Highest selling price
4. Total number of records
5. Missing value detection
6. Number of unique vehicles
7. Most sold vehicle

### Vehicle Category Analysis

8. CNG vehicles
9. Vehicles sold by individuals
10. Automatic transmission vehicles
11. Single-owner vehicles

### Depreciation Analysis

12. Most and least depreciated vehicles
13. Vehicles with lower depreciation
14. Factors affecting depreciation
15. Effect of vehicle age and kilometres driven on selling price

### Two-Wheeler Analysis

16. Vehicles manufactured after 2014
17. Two-wheelers
18. Oldest bike
19. Newest bike
20. Most sold bike
21. Two-wheelers with unusually high selling prices

### Car Analysis

22. Cars only
23. Oldest car
24. Newest car
25. Cars with unusually high selling prices

## Visualizations

The project generates graphical visualizations to understand relationships between vehicle attributes.

### Vehicle Age vs Selling Price

This visualization helps examine how the age of a vehicle affects its selling price. Generally, older vehicles tend to have lower resale prices because of depreciation.

### Kilometres Driven vs Selling Price

This graph is used to study the relationship between the distance travelled by a vehicle and its selling price.

##  Depreciation Calculation

Vehicle depreciation is calculated using:

```text
Depreciation = Present Price - Selling Price
```

The depreciation percentage is calculated as:

```text
Depreciation Percentage =
(Depreciation / Present Price) × 100
```

These values help compare the reduction in vehicle value.


##  Project Structure

```text
Car-Market-Trends-Analysis/
│
├── aicte1.py
├── car_data.csv
└── README.md
```


## ▶️ How to Run

### 1. Clone the repository


### 2. Open the project folder

```bash
cd Car-Market-Trends-Analysis
```

### 3. Install the required libraries

```bash
pip install pandas numpy matplotlib
```

### 4. Make sure the dataset is available

Keep `car_data.csv` in the same folder as `aicte1.py`.

### 5. Run the Python program

```bash
python Car_Market_Trends_Analysis.py
```

The program will display the analysis results in the terminal and generate graphs for vehicle age, kilometres driven, and selling price relationships.



## End Users

This project can be useful for:

* **Vehicle Buyers** – To compare vehicle prices and resale values
* **Vehicle Dealers** – To understand pricing patterns
* **Data Analysts** – To practice data analysis and visualization
* **Used Car Businesses** – To study depreciation and resale trends
* **Students & Researchers** – To learn practical applications of Python and EDA


