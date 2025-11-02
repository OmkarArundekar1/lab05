import json
import logging
from datetime import datetime
import ast

# Global variable for stock data (simple script use only)
stock_data = {}

# Configure logging once
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def addItem(item="default", qty=0, logs=None):
    """Add a specified quantity of an item to stock."""
    if logs is None:
        logs = []

    # Input validation
    if not isinstance(item, str):
        item = str(item)
    try:
        qty = int(qty)
    except (ValueError, TypeError):
        logging.error(f"Invalid quantity '{qty}' for item '{item}'")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info(f"Added {qty} of {item}. Total now: {stock_data[item]}")
    return logs


def removeItem(item, qty):
    """Remove a quantity of an item from stock safely."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info(f"{item} removed from stock (<=0)")
    except KeyError:
        logging.warning(f"Tried to remove non-existent item '{item}'")
    except TypeError as e:
        logging.error(f"Invalid quantity type: {e}")


def getQty(item):
    """Return quantity of a given item, 0 if not found."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load stock data from a JSON file safely."""
    global stock_data
    try:
        with open(file, "r") as f:
            stock_data = json.load(f)
        logging.info("Stock data loaded successfully.")
    except FileNotFoundError:
        logging.warning(f"File {file} not found. Starting with empty data.")
        stock_data = {}
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in inventory file.")


def saveData(file="inventory.json"):
    """Save stock data to a JSON file safely."""
    try:
        with open(file, "w") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Stock data saved successfully.")
    except Exception as e:
        logging.error(f"Error saving data: {e}")


def printData():
    """Print all inventory items."""
    print("\nItems Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def checkLowItems(threshold=5):
    """Return items with quantity below the threshold."""
    return [i for i, q in stock_data.items() if q < threshold]


def main():
    logs = []
    logs = addItem("apple", 10, logs)
    logs = addItem("banana", -2, logs)
    logs = addItem(123, "ten", logs)  # will log an error instead of crashing
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()

    # Replaced unsafe eval with literal evaluation (safe)
    safe_expr = "['safe', 'example']"
    try:
        result = ast.literal_eval(safe_expr)
        logging.info(f"Literal eval result: {result}")
    except Exception as e:
        logging.error(f"Literal eval failed: {e}")


if __name__ == "__main__":
    main()
