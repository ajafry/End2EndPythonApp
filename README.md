# Streamlit App and Web APIs

## Overview

This project contains a Streamlit application along with several web APIs to enhance its functionality. Web API and UI are both
using Python

## Streamlit App

The Streamlit app provides an interactive user interface for visualizing and interacting with data.

### Features

- **Data Visualization**: Interactive charts and graphs.
- **User Input**: Forms and widgets for user input.
- **Real-time Updates**: Live data updates and visualizations.

### Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

### Running the App

To start the Streamlit app, use the following command:

```bash
streamlit run app.py
```

## Web APIs

The project includes several web APIs to support the Streamlit app.

### Available Endpoints

- `GET /api/data`: Fetches data for visualization.
- `POST /api/update`: Updates data based on user input.
- `GET /api/status`: Checks the status of the application.

### API Documentation

Detailed API documentation can be found [here](docs/api.md).

### Running the API Server

To start the API server, use the following command:

```bash
uvicorn api:app --reload
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.