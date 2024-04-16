import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to read data and calculate combined SGPA
def calculate_combined_sgpa(data):
    data['Combined_SGPA'] = (data['SGPA_1'] + data['SGPA_2']) / 2
    return data

# Function to display top students
def display_top_students(data, position):
    top_students = data.sort_values(by='Combined_SGPA', ascending=False).head(position)
    st.write(f"Top {position} Students:")
    st.write(top_students)

# Function to display histogram of combined SGPA distribution
def display_sgpa_distribution(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(data['Combined_SGPA'], bins=10, edgecolor='black')
    ax.set_xlabel('Combined SGPA')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Combined SGPA')
    st.pyplot(fig)

# Function to display scatter plot of SGPA_1 vs SGPA_2
def display_sgpa_scatter(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(data['SGPA_1'], data['SGPA_2'])
    ax.set_xlabel('SGPA_1')
    ax.set_ylabel('SGPA_2')
    ax.set_title('SGPA_1 vs SGPA_2')
    st.pyplot(fig)

# Function to display bar chart of top students
def display_top_students_bar_chart(data, position):
    top_students = data.sort_values(by='Combined_SGPA', ascending=False).head(position)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(top_students['Name'], top_students['Combined_SGPA'])
    ax.set_xlabel('Student Name')
    ax.set_ylabel('Combined SGPA')
    ax.set_title(f'Top {position} Students')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
# Main function
def main():
    st.title('Top Students by Combined SGPA')
    st.write("Created by Rajesh Kumar,DEO,CON,SGPGI")  # Adding creator information
    file = st.file_uploader("Upload Excel file", type=["csv", "xlsx"])
    if file is not None:
        file_extension = file.name.split('.')[-1]
        if file_extension in ['csv', 'xlsx']:
            if file_extension == 'csv':
                data = pd.read_csv(file)
            else:
                data = pd.read_excel(file, engine='openpyxl')
            
            data = calculate_combined_sgpa(data)

            # Display top students
            top_position = st.sidebar.selectbox("Select Top Position", [1, 2, 3])
            display_top_students(data, top_position)

            # Display visualizations
            st.subheader('Visualizations:')
            display_sgpa_distribution(data)
            display_sgpa_scatter(data)
            display_top_students_bar_chart(data, top_position)
        else:
            st.error("Please upload a CSV or Excel file.")

# Disable the warning for PyplotGlobalUse
st.set_option('deprecation.showPyplotGlobalUse', False)

# Run the app
if __name__ == '__main__':
    main()