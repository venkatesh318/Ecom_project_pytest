# Flipkart Selenium Pytest Project

## About the Project

This project implements automated testing for the Flipkart e-commerce website using Selenium with pytest. The following test cases are covered:

- *Mobile Testing:* Validates user searching the mobile and adding to cart and verifies in cart whether correct product is added or not
- *Book Search Test:* Validates user searching the mobile and adding to cart and verifies in cart whether correct product is added or not
- *Adopter Adding and Pincode Verification:* Validates user searching the adpoter from the cart page and addinf to cart
- *Cart Operations Test:* Tests adding and removing products from the cart.
- *Price Confirmation:* Simulates the checkout process and ensures it works correctly.


## How to Clone the Repository

To clone this repository, use the following command:
```
git clone https://github.com/yourusername/flipkart-selenium-pytest.git
```

## Creation of Virtual Environment
It's recommended to use a virtual environment to manage dependencies. To create a virtual environment, navigate to your project directory and run:


```
python -m venv venv
```
Activate the virtual environment:

- Windows: venv\Scripts\activate
- Linux/Mac: source venv/bin/activate

## Installation of Requirements
Install the required packages using the following command:

```
pip install -r requirements.txt
```

## How to Run Tests
To execute the tests, use the following command:
```
pytest 
```
Another way to run, it will generate the report in html format
```
pytest --html=report.html
```
## How to See Results
Test results will be displayed in the terminal after running the tests. For a detailed report, you can generate an HTML report using pytest-html:

```
pytest --html=report.html
```
```
result file : Ecom_project_pytest/tests/report.html
```

## Test Evidence

Test evidences are available in **Ecom_project_pytest/screenshots** folder


#### Contact
For any questions or issues, please contact:

Name: Venkateswarlu gurram

Email: venkateshgurram01@gmail.com