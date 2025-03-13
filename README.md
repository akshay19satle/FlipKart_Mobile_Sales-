# FlipKart Mobile Sales Analysis And Visualization-

## Description
The Flipkart Mobile Sales dataset contains details of mobile phones listed for sale on Flipkart. The data captures essential attributes of each phone, including brand, model, technical specifications, pricing, and user ratings. 
This project analyzes and visualizes Flipkart mobile sales data using Python and Streamlit. It includes data cleaning, analysis, and an interactive web dashboard for exploring the sales trends and insights.

## Column description
1) Brand - Name of the mobile phone manufacturer (e.g., Samsung, Apple).
2) Model -  Specific model or series name of the phone (e.g., iPhone 11, Galaxy S21).
3) Color -  Color variant of the phone (e.g., Black, Blue, Mint Cream).
4) Memory - Size of the phone's RAM (e.g., 4 GB, 8 GB).
5) Storage - Internal storage capacity of the phone (e.g., 64 GB, 128 GB).
6) Rating - Average customer rating (out of 5) based on user reviews.
7) Selling Price - Current selling price of the phone on Flipkart (in INR).
8) Original Price - Original listed price before any discounts (in INR).

## Tools & Libraries
Programming Language – Python

Libraries – Pandas, Matplotlib, Seaborn, Plotly, Streamlit

Platform – Google Colab, Streamlit

## Project Workflow
1) Data Collection

Collected the raw Flipkart mobile sales data (Flipkart_Mobiles.csv) from an online source.The data contained information about mobile brands, models, specifications, prices, and ratings.

2) Data Cleaning and Preprocessing
   
Loaded the raw data using Pandas.Cleaned the data by:Removing duplicates and handling missing values. Standardizing formatting (e.g., consistent brand names, memory, storage).Saved the cleaned data to a new file (Flipkart_Mobiles_Cleaned.csv).

3) Building the Streamlit Web App
   
Created a Streamlit app (flipkart.py) to visualize the data interactively.
Added sidebar filters amd visuals. Enabled dynamic user interaction to explore data insights. Packaged the project and made it available for easy execution through Streamlit.

## Insights
1) The highest number of models sold are from [Top Brand].
2) [Top Color] is the most preferred color by customers.
3) Higher storage models generally have higher selling prices.
4) The average rating is highest for [Brand] models.
5) Impact of discounts on customer purchase decisions.


