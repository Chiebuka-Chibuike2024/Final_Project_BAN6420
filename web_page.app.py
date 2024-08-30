#Install "pymongo" if unavailable using "pip install pymongo"
# Verify installation using "pip list"

from flask import Flask, request, jsonify
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['survey_db']
collection = db['responses']

@app.route('/')
def index():
    """
    Render the index page with a form to submit data.
    """
    return '''
        <form action="/submit" method="post">
        <h1> Income Spending Data </h1>
            First Name: <input type="text" name="first_name"><br>
            Last Name: <input type="text" name="last_name"><br>
            Age: <input type="text" name="age"><br>
            Gender: <input type="text" name="gender"><br>
            Total Income: <input type="text" name="total_income"><br>
            <h3>Expenses</h3>
            Utilities: <input type="text" name="utilities"><br>
            Entertainment: <input type="text" name="entertainment"><br>
            School Fees: <input type="text" name="school_fees"><br>
            Shopping: <input type="text" name="shopping"><br>
            Healthcare: <input type="text" name="healthcare"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    """
    Submit form data to MongoDB.
    """
    try:
         # Collect form data
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'total_income': request.form['total_income'],
            'expenses': {
                'utilities': request.form['utilities'],
                'entertainment': request.form['entertainment'],
                'school_fees': request.form['school_fees'],
                'shopping': request.form['shopping'],
                'healthcare': request.form['healthcare']
            }
        }

         # Insert the collected data into the MongoDB collection
        collection.insert_one(data)

        # Return success message if data is inserted successfully
        return 'Data submitted successfully!'
    except Exception as e:

        # Handle any errors that occur during data insertion
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
