# Cookie Catalog Application

Welcome to the Cookie Catalog application! This Streamlit app allows users to browse a delightful collection of cookies, complete with descriptions, prices, and images.

## Project Structure

The project is organized as follows:

```
cookie-catalog-app
├── src
│   ├── app.py                # Main entry point of the Streamlit application
│   ├── components            # Directory for reusable components
│   │   └── __init__.py       # Initialization file for components
│   ├── data                  # Directory for data files
│   │   └── cookies.csv       # CSV file containing cookie data
│   └── utils                 # Directory for utility functions
│       └── __init__.py       # Initialization file for utilities
├── requirements.txt          # List of dependencies for the project
├── README.md                 # Documentation for the project
└── .streamlit                # Directory for Streamlit configuration
    └── config.toml           # Configuration settings for the Streamlit app
```

## Installation

To get started with the Cookie Catalog application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cookie-catalog-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command in your terminal:
```
streamlit run src/app.py
```

This will start the Streamlit server and open the application in your default web browser.

## Contributing

If you would like to contribute to the Cookie Catalog application, feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.