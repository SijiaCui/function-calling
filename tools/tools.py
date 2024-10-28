
def get_current_datetime():
    """
    Returns the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    from datetime import datetime
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now


def find_factors(num):
    """
    Calculate and return all unique factors of a given integer
    """
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return sorted(list(set(factors)))


def show_databases(host: str, user: str, password: str):
    """
    Connects to a MySQL database and lists all available databases.
    """
    import mysql.connector
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    
    databases = []
    for (database, ) in cursor:
        databases.append(database)

    cursor.close()
    conn.close()
    return databases


def get_stock_high(ticker_symbol:str, start_date: str, end_date: str):
    import yfinance as yf
    """
    Retrieves the highest stock price for a specified company on a specific range of date.
    """
    stock = yf.Ticker(ticker_symbol)
    stock_data = stock.history(start=start_date, end=end_date)

    print(stock_data)
    if not stock_data.empty:
        # Extract the highest price for the date
        high_price = stock_data['High'].max()
        return high_price
    else:
        return "No data available for this date."


def get_function_result(tool_call) -> dict:
    import json
    func = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)
    if func == 'get_current_datetime':
        arguments['current_datetime'] = get_current_datetime(**arguments)
    elif func == 'find_factors':
        arguments['factors'] = find_factors(**arguments)
    elif func == 'show_databases':
        arguments['databases'] = show_databases(**arguments)
    elif func == 'get_stock_high':
        arguments['stock_high'] = get_stock_high(**arguments)
    return {
                "role": "tool",
                "content": json.dumps(arguments),
                "tool_call_id": tool_call.id
            }

"""
ChatCompletionMessageToolCall(
    id='call_NDWcBLzseRbW7VpHycTWDuRP', 
    function=Function(arguments='{}', name='get_current_datetime'), 
    type='function'
)
"""

if __name__ == '__main__':
    # print(get_current_datetime())
    # print(find_factors(9264857101))
    # print(show_databases('localhost', 'root', '123456'))
    print(get_stock_high('MSFT', '2024-10-25', '2024-10-26'))
