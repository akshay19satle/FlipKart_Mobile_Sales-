import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title("📊 Flipkart Mobile Sales Dashboard")
st.subheader("📈 Flipkart Mobile Sales Data")

df=pd.read_csv('c:/Users/HP/Documents/akshay data analysis/Flipkart_Mobiles_Cleaned.csv')
df

# sidebar
st.sidebar.header("Filters")
selection = st.sidebar.radio('Data Selection Method', ["None","Head","Tail"])
if selection in ['Head','Tail']:
    num_rows = st.sidebar.number_input('Number of Rows', 1, df.shape[0],5)
    if selection == 'Head':
        st.subheader(f"Top {num_rows} Rows")
        st.write(df.head(num_rows))
    elif selection == 'Tail':
        st.subheader(f"Bottom {num_rows} Rows")
        st.write(df.tail(num_rows))
    else:
        st.write(df)

selected_brand = st.sidebar.multiselect("Select Brand", df["Brand"].unique())
Selling_Price_range = st.sidebar.slider("Selling Price Range", int(df["Selling Price"].min()), int(df["Selling Price"].max()),(1000, 179900))
filtered_df = df[(df["Selling Price"] >= Selling_Price_range[0]) & (df["Selling Price"] <= Selling_Price_range[1])]
if selected_brand:
    filtered_df = filtered_df[filtered_df["Brand"].isin(selected_brand)]
st.subheader("📌 Filtered Data Preview")
st.write(filtered_df)
st.write(f"The filtered rows are {filtered_df.shape[0]}")


# Visualizations

# 1
brand_counts = df["Brand"].value_counts().reset_index()
brand_counts.columns = ["Brand", "Count"]
fig = px.bar(brand_counts, x='Count', y='Brand', orientation="h", labels={'x': 'Count', 'y': 'Brand'},title='📊 Total Number of Mobile Brand Sold',text='Count')
st.plotly_chart(fig)




# Sidebar Filters
st.sidebar.subheader("📊 Filter Top/Bottom Categories")
# st.sidebar.subheader("📊 Select Graph")
# select_graph = st.sidebar.selectbox("Select Graph", 
#                                     ["Most Popular Mobile Models Across Brands", 
#                                      "Top Colors Preferred by Buyers", 
#                                      "Selling Price Distribution of Mobile Models"])
# if select_graph == "Most Popular Mobile Models Across Brands":
    
choose_range = st.sidebar.radio("Choose Top or Bottom", ["None", "Top", "Bottom"])
choose_values = st.sidebar.number_input("Number of values", 1, 50, 10)

### **1️⃣ Most Popular Mobile Models Across Brands**
model_counts = df['Model'].value_counts().reset_index()
model_counts.columns = ['Model', 'Count']

if choose_range == "Top":
    filtered_models = model_counts.head(choose_values)
elif choose_range == "Bottom":
    filtered_models = model_counts.tail(choose_values)
else:
    filtered_models = model_counts.head(20)  # Default Top 20

top_df = pd.merge(filtered_models, df, on='Model', how='left')

fig1 = px.bar(top_df, x='Brand', y='Count', color='Model', 
              labels={'x': 'Brand', 'y': 'Model count'}, 
              title=" 📈 Most Popular Mobile Models Across Brands")

### **2️⃣ Top Colors Preferred by Buyers**
color_counts = df['Color'].value_counts().reset_index()
color_counts.columns = ['Color', 'Count']

if choose_range == "Top":
    filtered_colors = color_counts.head(choose_values)
elif choose_range == "Bottom":
    filtered_colors = color_counts.tail(choose_values)
else:
    filtered_colors = color_counts.head(10)  # Default Top 10

fig2 = px.pie(filtered_colors, values='Count', names='Color', 
              title=" 🎯 Top Colors Preferred by Buyers", color='Color', 
              color_discrete_map={color: color for color in filtered_colors['Color']})

### **3️⃣ Selling Price Distribution of Mobile Models**
if choose_range == "Top":
    filtered_df = df.nlargest(choose_values, 'Selling Price')
elif choose_range == "Bottom":
    filtered_df = df.nsmallest(choose_values, 'Selling Price')
else:
    filtered_df = df.copy()  # Default - Show all data

fig8 = px.bar(filtered_df, x='Selling Price', y='Model', title="🏆 Selling Price Distribution of Mobile Models", 
              orientation='h', labels={'Selling Price': 'Selling Price', 'Model': 'Mobile Model'})

# **Display All Graphs By Default**
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig8)



# # 2
# model_counts = df['Model'].value_counts().reset_index()
# model_counts.columns = ['Model', 'Count']
# top_20_models = model_counts.head(20)
# top_20_df = pd.merge(top_20_models, df, on='Model', how='left')
# fig1 = px.bar(top_20_df, x='Brand', y='Count', color='Model', labels={'x': 'Brand', 'y': 'Model count'}, title="Most Popular Mobile Models Across Brands")
# st.plotly_chart(fig1)
# fig1.update_layout(xaxis_tickangle=-45, legend_title="Model", title_x=0.5)

# 3
# color_counts=df['Color'].value_counts().sort_values(ascending=False).head(10).reset_index()
# color_counts.columns = ['Color', 'Count']
# fig2 = px.pie(color_counts, values='Count', names='Color', title="Top 10 Colors Preferred by Buyers", color='Color',color_discrete_map={color: color for color in color_counts['Color']}) 
# st.plotly_chart(fig2)

# 4
fig3 = px.scatter(df, x='Memory', y='Storage', color='Brand', title="📝 Storage vs. Memory: Trends in Smartphone Models")
st.plotly_chart(fig3)

# 5
fig5 = px.box(df, x='Brand', y='Rating', color='Brand', title="Rating Distribution of Mobile Brands", labels={'Brand': 'Mobile Brands', 'Rating': 'Rating'})
st.plotly_chart(fig5)

# 6
fig6 = px.scatter(df, x='Brand', y='Original Price', color='Brand', title="Price Distribution of Mobile Brands",labels={'Brand': 'Mobile Brand', 'Original Price': 'Original Price'},size_max=10)
st.plotly_chart(fig6)

# 7
df_sorted = df.sort_values(by="Selling Price", ascending=False)
fig7 = px.bar(df_sorted, x='Brand', y='Selling Price', color='Brand', title="Selling Price Distribution of Mobile Brands", labels={'Brand': 'Mobile Brand', 'Selling Price': 'Selling Price'})
st.plotly_chart(fig7)

# 8
# fig8 = px.bar(df, x='Selling Price', y='Model', title='Selling Price Distribution of Mobile Models', orientation='h', labels={'Selling Price': 'Selling Price', 'Model': 'Mobile Model'})
# st.plotly_chart(fig8)

# 9
memory_counts = df['Memory'].value_counts().reset_index()
memory_counts.columns = ['Memory', 'Count']
memory_counts = memory_counts.sort_values(by="Count", ascending=False)
fig9 = px.bar(memory_counts, x='Memory', y='Count', title="Mobile Sales Distribution by Memory Size", labels={'Memory': 'Memory', 'Count': 'Count'},text='Count', template="plotly_dark")
st.plotly_chart(fig9)

# 10
storage_counts = df['Storage'].value_counts().reset_index()
storage_counts.columns = ['Storage', 'Count']
storage_counts = storage_counts.sort_values(by="Count", ascending=False)
fig9 = px.bar(storage_counts, x='Storage', y='Count', title="Mobile Sales Distribution by Storage Size", labels={'Storage': 'Storage', 'Count': 'Count'},text='Count', template="plotly_dark")
st.plotly_chart(fig9)
    
# 11
memory = df.groupby('Memory')['Selling Price'].mean().reset_index()
memory['Memory'] = memory['Memory'].astype(str)
memory = memory.sort_values(by='Memory', key=lambda col: col.str.extract(r'(\d+)').astype(int)[0], ascending=False)
fig11 = px.bar(memory, x='Selling Price', y='Memory', title="Average Selling Price by Mobile Memory Size", orientation='h', labels={'Memory': 'Memory', 'Selling Price': 'Average Selling Price'})
st.plotly_chart(fig11)

# 12
storage = df.groupby('Storage')['Selling Price'].mean().reset_index()
storage['Storage'] = storage['Storage'].astype(str)
storage = storage.sort_values(by='Storage', key=lambda col: col.str.extract(r'(\d+)').astype(int)[0], ascending=False)
fig12 = px.bar(storage, x='Selling Price', y='Storage', title="Average Selling Price by Mobile Storage Size", orientation='h', labels={'Storage': 'Storage', 'Selling Price': 'Average Selling Price'})
st.plotly_chart(fig12)








