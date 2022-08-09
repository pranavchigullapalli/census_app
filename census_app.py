import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()

	# Rename the column names in the DataFrame. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race', 'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

st.title('Census Data Visualisation App')

if st.sidebar.checkbox('Display Census Dataframe'):
	st.subheader('Census Dataset')
	st.dataframe(census_df)
	st.write(f'Number of rows = {census_df.shape[0]}')
	st.write(f'Number of columns = {census_df.shape[1]}')


st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.subheader('Visualisation Selector')

plot_list=st.sidebar.multiselect('Select the Charts/Plots:', ('Pie Chart', 'Box Plot', 'Count Plot'))


if "Pie Chart" in plot_list:
  st.subheader('Pie Chart')
  st.subheader('Distribution of Records for Different Income Groups')
  plt.figure(figsize=(8,6))
  array=np.array(census_df['income'].value_counts())
  plt.pie(array, labels=['<=50k', '>50k'], explode=[0.05, 0.05], autopct='%1.1f%%')
  st.pyplot()
  st.subheader('Distribution of Records for Different Gender Groups')
  plt.figure(figsize=(8,6))
  array=np.array(census_df['gender'].value_counts())
  plt.pie(array, labels=['Male', 'Female'], explode=[0.05, 0.05], autopct='%1.1f%%')
  st.pyplot()
if 'Box Plot' in plot_list:
  st.subheader('Box Plot for Hours Worked Per Week')
  plt.figure(figsize=(9, 5))
  plt.title('Boxplot for hours worked per week for different income groups')
  sns.boxplot(x='hours-per-week', y='income', data=census_df)
  st.pyplot()
  plt.figure(figsize=(9, 5))
  plt.title('Boxplot for hours worked per week for different gender groups')
  sns.boxplot(x='hours-per-week', y='gender', data=census_df)
  st.pyplot()
if 'Count Plot' in plot_list:
  st.subheader('Count Plot for distribution of records for unique workclass values')
  plt.figure(figsize=(9,5))
  sns.countplot(x='workclass', hue='income', data=census_df)
  st.pyplot()