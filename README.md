# Data Analysis Project - Company Stock Data

## Overview
This project involves analyzing the stock data for multiple companies, focusing on various statistical and visual analysis techniques such as calculating daily spreads, identifying trends, and comparing key metrics across different companies. It also includes extensive preprocessing to handle missing values, outliers, erroneous rows, and more.

## Preprocessing Steps
Before conducting any analysis, several preprocessing steps were applied to ensure the quality of the data. Below are the key preprocessing steps taken for each dataset:

### 1. **Handling Missing Values**
- **Volume**: Missing values in the `Volume` column were filled using a rolling window mean with a window size of 7 days.
- **Price Columns (Open, High, Low, Close, Adj Close)**: Missing values in price-related columns were filled using a rolling median with a window size of 7 days.

### 2. **Outlier Handling**
- **Price Columns**: Z-scores were calculated for each price column (`Open`, `High`, `Low`, `Close`, `Adj Close`). Any outliers with Z-scores greater than 3 or less than -3 were replaced with the rolling median value for that column.

### 3. **Erroneous Data Correction**
- **Low vs. High**: If the value in the `Low` column was greater than or equal to the `High` column for any row, the erroneous `Low` value was replaced with the rolling mean of the `Low` values over the previous 7 days. If the rolling mean of `Low` was still higher than `High`, the `Low` value was adjusted to match the `High` value.
  
### 4. **Handling Zero Volume**
- **Volume Zero**: If the `Volume` was zero for any row, and the `Open`, `High`, `Low`, or `Close` prices were different, the prices were replaced with the most frequent value (mode) in that row.

### 5. **Duplicate Dates**
- **Duplicate Date Handling**: Any duplicate dates in the dataset were identified, and if duplicates were found, they were printed out for further inspection.

### 6. **NaN Volume with Identical Prices**
- If a row had identical values in the price columns (`Open`, `High`, `Low`, `Close`) and `Volume` was missing, the missing `Volume` was replaced with 0.0.

---

## Exercises

### **EXERCISE 1**  
---

## 📝 **Description**  

### **1: For Each Dataset**  
- **Print the number of rows and columns**  
- **Display the column names and their data types**  
🎉

---

### **EXERCISE 2**  
---

## 📝 **Description**  

### **2: Extract Rows for 2023**  
- **Filter all rows where the date is in the year 2023**  
- **Print the number of rows**  
- **Visualize the Close price trend for this period**  
🎉

---

### **EXERCISE 3**  
---

## 📝 **Description**  

### **3: Find the Day with Highest Close Price**  
- **For each company, identify the day with the highest Close price**  
- **Display the date and the corresponding Close price**  
🎉

---

### **EXERCISE 4**  
---

## 📝 **Description**  

### **4: Monthly Average Close Price Analysis**  
- **Group the data by month and calculate the average Close price for each company**  
- **Plot these monthly averages for 3 companies and compare them**  
- **Justify the chart selection**  
🎉

---

### **EXERCISE 5**  
---

## 📝 **Description**  

### **5: Yearly Average Close Price Comparison**  
- **For each company:**  
  - **Compute the yearly average of the Close price**  
  - **Plot a comparison of yearly averages for all companies on a chart**  
- **Justify your chart selection**  
🎉

---

### **EXERCISE 6**  
---

## 📝 **Description**  

### **6: Monthly Price Range Visualization**  
- **For each company, create a plot showing the range of prices for each month**  
- **Justify the chart selection**  
🎉

---

### **EXERCISE 7**  
---

## 📝 **Description**  

### **7: Relationship Between Trading Volume and Close Price**  
- **Create a plot showing the relationship between trading volume and the Close price for a selected company**  
- **Add insights about the pattern**  
- **Justify your chart selection**  
🎉

---

### **EXERCISE 8**  
---

## 📝 **Description**  

### **8: Month with Highest Total Trading Volume**  
- **For each company, identify the month with the highest total trading volume**  
- **Display the results in a summary table, showing the month and total volume**  
🎉

---

### **EXERCISE 9**  
---

## 📝 **Description**  

### **9: Merging Datasets by Year**  
- **Merge the datasets for all companies into a single dataset, one for each year**  
- **Print the structure of the combined dataset, ensuring proper alignment and handling of missing values**  
🎉

---

### **EXERCISE 10**  
---

## 📝 **Description**  

### **10: Daily Price Spread Analysis**  
- **For each company:**  
  1. **Calculate the spread between the High and Low prices for each day**  
  2. **Compute the average spread for each company and visualize the result in a chart**  
  3. **Justify the chart selection**  
  4. **Interpret which companies exhibit the largest spreads and why this might happen**  
🎉

---

## Requirements
- Python 3.x
- pandas
- matplotlib
- numpy
- sklearn (if needed for further modeling)

## Installation
1. Clone the repository to your local machine.
2. Install the required libraries using pip:

```bash
pip install -r requirements.txt
