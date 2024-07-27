# Currency Exchange

## Description
A web application built with Flask for currency conversion. This app allows users to convert amounts from one currency to another using real-time exchange rates provided by the Fixer API. Users can select currencies from a dropdown list and input the amount they wish to convert. The application then displays the converted amount and the exchange rate used.

## Features
- Currency Selection: Dropdown menus for selecting both base and target currencies from a list of global currencies.
- Real-Time Exchange Rates: Fetches up-to-date exchange rates from the Fixer API.
- Conversion Calculation: Calculates and displays the converted amount based on user input.

## Technologies Used

- Flask: Web framework
- Requests: Makes HTTP requests to Fixer API
- Jinja2: Rendering HTML templates, drop down menu
- Dotenv: For managing API key
