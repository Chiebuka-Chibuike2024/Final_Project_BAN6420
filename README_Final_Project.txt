                                   FINAL PROJECT: FLASK HEALTHCARE APPLICATION

This project aims to understand potential healthcare product users by analyzing their income and spending habits. 

Overview:
The objective of this Project is to analyze income spending of both genders (male and female) in preparation for a new product launch in the healthcare industry.

Contents:
1) A web survey to collect user data using Flask.
2) A MongoDB database to store user details like age, gender, income, and expenses.
3) Data processing with Python to prepare the data for analysis.
4) Interactive visualizations with Jupyter Notebook to identify trends.
5) A  PowerPoint presentation showing key findings (charts included).

Software Used:

1) Python.
2) Flask.
3) Jupyter Notebook.
4) MongoDB.

Structure:

1) `web_page_app.py`: Flask application for the survey.
2) Data Storage with MongoDB: It is used to store user details such as: Age, Gender, Total Income, and Expenses, in MongoDB.
3) `template/index.html`: HTML template for the survey webpage.
4) `data_processing.py`: Python script to manage user data. Create a Python class named "User". This can be found in `data_processing.py` script. Loop through the collected data and store it in a CSV file.
5) `data.csv`: CSV file to store user data.
6) `data_visualization.ipynb`: This file contains visualizations.
7) `charts`: Folder containing exported charts.
8) `README.md`: Project documentation & instructions

Running the Project:

1. Install Python, Flask, and other dependencies.
2. Start your MongoDB server.
3. Run `web_page_app.py` to launch the survey app.
4. Submit the survey to store user data.
5. Run `data_processing.py` to prepare the data for analysis (CSV file).
6. Open `data_visualization.ipynb` in Jupyter Notebook. Perform visualizations in a Jupyter notebook, including:
    - Loading required libraries like matplotlib, seaborn and pandas.
    - Showing the ages with the highest income.
    - Showing the gender distribution across spending categories.
    - Export the charts for use in a PowerPoint presentation for client use.
7. The PowerPoint presentation is stored in a file named "Final Project_BAN 6420 (Chart Visualization)".
8. Deployment on AWS: Host the Flask application on Amazon Web Services (AWS).





