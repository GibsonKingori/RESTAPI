

### *README.md*


# Product API

A Django-based REST API for managing products. The API allows you to create and list products with the following fields:
- *Name*: The name of the product.
- *Description*: A brief description of the product.
- *Price*: The price of the product.

## Features
- Create a new product.
- List all products.

---

## Prerequisites

Make sure you have the following installed on your system:
1. *Python 3.8+*: [Download Python](https://www.python.org/downloads/)
2. *pip*: Comes with Python; verify by running pip --version.
3. *Virtualenv* (optional but recommended): Install with pip install virtualenv.

---

## Setting Up the Environment

### 1. Clone the Repository
bash
git clone https://github.com/GibsonKingori/RESTAPI.git
cd product_api


### 2. Create a Virtual Environment
Create and activate a virtual environment to isolate dependencies.

#### On Windows:
bash
python -m venv env
env\Scripts\activate


#### On macOS/Linux:
bash
python3 -m venv env
source env/bin/activate


### 3. Install Dependencies
bash
pip install -r requirements.txt


### 4. Apply Migrations
Run the following commands to set up the database:
bash
python manage.py makemigrations
python manage.py migrate


### 5. Create a Superuser (Optional)
If you want to access the Django admin interface:
bash
python manage.py createsuperuser


### 6. Start the Server
Run the server:
bash
python manage.py runserver


The server will be available at http://127.0.0.1:8000/.

---

## Testing the API

### Testing with a Browser
1. Open the following URL in your browser:
   - *List Products*: http://127.0.0.1:8000/api/products/

### Testing with Postman
1. Download and install [Postman](https://www.postman.com/).
2. Use the following details to test the API endpoints:

#### *List All Products*
- *URL*: http://127.0.0.1:8000/api/products/
- *Method*: GET
- *Response*: JSON containing all products.

#### *Create a New Product*
- *URL*: http://127.0.0.1:8000/api/products/create/
- *Method*: POST
- *Body* (raw, JSON format):
  json
  {
      "name": "Laptop",
      "description": "A high-performance laptop",
      "price": 1200.00
  }
  
- *Response*: JSON containing the created product.

---

### Testing with the Provided Python Script

Run the provided client_script.py to interact with the API:
1. Ensure the Django server is running.
2. Execute the script:
   bash
   python client_script.py
   

This script will:
1. Add a new product using the /products/create/ endpoint.
2. Fetch and display all products using the /products/ endpoint.

---

## Directory Structure

product_api/
├── product_api/            # Main project folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project-level URL configuration
│   └── ...
├── products/               # App folder
│   ├── models.py           # Product model
│   ├── serializers.py      # Product serializer
│   ├── views.py            # API views
│   ├── urls.py             # App-level URL configuration
│   └── ...
├── client_script.py        # Python script to interact with the API
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── requirements.txt        # Dependencies
└── README.md               # Documentation (this file)


---

## Upload to GitHub

### 1. Initialize Git
If you haven’t initialized Git in your project directory, run:
bash
git init


### 2. Add All Files
bash
git add .


### 3. Commit the Changes
bash
git commit -m "Initial commit with API and documentation"


### 4. Push to GitHub
1. Create a new repository on GitHub.
2. Link your local repository to GitHub:
   bash
   git remote add origin https://github.com/GibsonKingori/RESTAPI.git
   
3. Push your code:
   bash
   git push -u origin main
   

---

## Contributors
- Gibson Kingori

---

## License
This project is licensed under the MIT License.



---

### Additional Notes:
- `https://github.com/GibsonKingori/RESTAPI.git
- Ensure the `requirements.txt` file is up-to-date by running:
  bash
  pip freeze > requirements.txt
  ```
