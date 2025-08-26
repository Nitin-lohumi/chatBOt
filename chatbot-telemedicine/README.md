# Telemedicine Chatbot

This project is a chatbot designed to provide telemedicine services in rural areas. It aims to assist users in accessing healthcare information, scheduling appointments, and answering frequently asked questions related to health.

## Features

- **User Interaction**: Engages users in conversation to provide health-related information.
- **Appointment Scheduling**: Allows users to schedule telemedicine appointments.
- **FAQ Support**: Provides answers to frequently asked questions using a predefined dataset.

## Project Structure

```
chatbot-telemedicine
├── src
│   ├── main.py                # Entry point of the application
│   ├── chatbot                 # Contains chatbot logic
│   │   ├── __init__.py
│   │   ├── bot.py             # ChatBot class with response handling
│   │   └── intents.py         # Intent loading and parsing
│   ├── services                # Contains service-related functions
│   │   ├── __init__.py
│   │   └── telemedicine.py     # Functions for telemedicine services
│   ├── data                   # Data files
│   │   └── faq.json           # FAQ data for chatbot responses
│   └── utils                  # Utility functions
│       └── helpers.py         # Helper functions for various tasks
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-telemedicine
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage

Once the application is running, users can interact with the chatbot through the command line interface. The chatbot will respond to health-related queries and assist with scheduling appointments.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.