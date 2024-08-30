# Import required libraries
import csv
from pymongo import MongoClient  # Import MongoClient for MongoDB connection

# Create user class
class User:
    def __init__(self, first_name, last_name, age, gender, total_income, expenses):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    @staticmethod
    def save_to_csv(data, filename='data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['First Name', 'Last Name', 'Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
            for user in data:
                writer.writerow([user.first_name, user.last_name, user.age, user.gender, user.total_income, user.expenses['utilities'], user.expenses['entertainment'], user.expenses['school_fees'], user.expenses['shopping'], user.expenses['healthcare']])


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
collection = db['responses']

# Fetch data from MongoDB and Save to CSV
users = []
for doc in collection.find():
    user = User(doc['first_name'], doc['last_name'], doc['age'], doc['gender'], doc['total_income'], doc['expenses'])
    users.append(user)

# Initialize the function
User.save_to_csv(users)
