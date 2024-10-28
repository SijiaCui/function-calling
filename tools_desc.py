
tool_get_current_datetime = {
    "type": "function",
    "function": {
        "name": "get_current_datetime",
        "description": "Retrieve the current date and time in the format YYYY-MM-DD HH:MM:SS. Use this whenever the current timestamp is required, such as for logging or displaying the current time.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    }
}

tool_find_factors = {
    "type": "function",
    "function": {
        "name": "find_factors",
        "description": "Calculate and return all unique factors of a given integer. Use this function to retrieve factors for mathematical computations or analysis.",
        "parameters": {
            "type": "object",
            "properties": {
                "num": {
                    "type": "integer",
                    "description": "The integer for which to find all factors.",
                }
            },
            "required": ["num"],
            "additionalProperties": False
        }
    }
}

tool_show_databases = {
    "type": "function",
    "function": {
        "name": "show_databases",
        "description": "Connects to a MySQL server and retrieves a list of all available databases. Use this function when you need to display or manage available databases on the server.",
        "parameters": {
            "type": "object",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "The hostname or IP address of the MySQL server, typically 'localhost' for local connections."
                },
                "user": {
                    "type": "string",
                    "description": "The username for authenticating the MySQL connection, such as 'root'."
                },
                "password": {
                    "type": "string",
                    "description": "The password for the MySQL user."
                }
            },
            "required": ["host", "user", "password"],
            "additionalProperties": False
        }
    }
}

tool_get_stock_high = {
    "type": "function",
    "function": {
        "name": "get_stock_high",
        "description": "Retrieves the highest stock price for a specified company within a given date range. The start date and end date must be at least 1 day apart.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticker_symbol": {
                    "type": "string",
                    "description": "The stock ticker symbol of the company (e.g., 'AAPL' for Apple Inc.)."
                },
                "start_date": {
                    "type": "string",
                    "description": "The start date for the stock price query in YYYY-MM-DD format."
                },
                "end_date": {
                    "type": "string",
                    "description": "The end date for the stock price query in YYYY-MM-DD format."
                }
            },
            "required": ["ticker_symbol", "start_date", "end_date"],
            "additionalProperties": False
        }
    }
}


all_tools = [
    tool_get_current_datetime,
    tool_find_factors,
    tool_show_databases,
    tool_get_stock_high
]
