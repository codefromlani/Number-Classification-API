Number Classification API

This project implements a simple Flask API that classifies numbers based on certain mathematical properties and provides fun facts about numbers.


Features:
- Check if a number is prime
- Check if a number is perfect
- Check if a number is an Armstrong number
- Sum of digits of a number
- Fun fact about the number


Technologies Used:
- Flask 
- Requests - For making HTTP requests to fetch fun facts about numbers
- Flask-CORS
- JSON 


Installation

  - Clone the repository:

    - git clone https://github.com/codefromlani/Number-Classification-API.git
    - cd Number-Classification-API
    

Create a virtual environment:

- python -m venv venv
    - `venv\Scripts\activate` # to activate on Windows 
    - source venv/bin/activate # On Mac/Linux:


Install the required dependencies:

- pip install -r requirements.txt


Run the Flask app:

- python app.py
- The API will be available at http://127.0.0.1:5000/api/classify-number


API Endpoints:
- Classify a Number
    URL: /api/classify-number

    Method: GET

    Query Parameter: number (required)

    Description: Classifies a given number by checking its properties: prime, perfect, Armstrong, and even/odd. Also provides the sum of its digits and a fun fact.

    Example Request:
    - GET http://127.0.0.1:5000/api/classify-number?number=153


    Example Response:

        {

    "number": 153,

    "is_prime": false,

    "is_perfect": false,

    "properties": ["armstrong", "odd"],

    "digit_sum": 9,

    "fun_fact": "153 is a narcissistic number."

    }


Error Handling:
- 400 Bad Request: If the provided number is not valid (e.g., non-numeric input).
- 404 Not Found: If the endpoint is incorrect.
- 500 Internal Server Error: For unexpected issues.


Example of invalid request:

    {

    "number": "alphabet",

    "error": true

    }
