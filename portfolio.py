import json
from data_manager import load_data, save_data
from portfolio_analysis import find_best_stock, find_worst_stock


def add_stock():
    print()
    print("==================================================")
    print("                  ADD STOCK")
    print("==================================================")
    print()

    stock_name = input("Enter Stock Name: ")
    stock_symbol = input("Enter Stock Symbol: ")
    quantity = input("Enter Quantity: ")
    buy_price = input("Enter Buy Price: ")
    current_price = input("Enter Current Price")

    try:
        quantity = int(quantity)
    except ValueError:
        print("Please enter a valid quantity.")
        return

    try:
        buy_price = float(buy_price)
    except ValueError:
        print("Please enter a valid buy price.")
        return

    try:
        current_price = float(current_price)
    except ValueError:
        print("Please enter a valid current price.")
        return
   
    stock_data = {
        "name": stock_name,
        "symbol": stock_symbol,
        "quantity": quantity,
        "buy_price": buy_price,
        "current_price": current_price
    }
    
    transaction = {
        "action": "Added",
        "name": stock_name,
        "symbol": stock_symbol,
        "quantity": quantity,
        "buy_price": buy_price,
        "current_price": current_price
    }
    
    portfolio = load_data()
    portfolio.append(stock_data)

    save_data(portfolio)

    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        transactions = []

    transactions.append(transaction)

    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)
    
    print()
    print("==================================================")
    print("             STOCK ADDED SUCCESSFULLY")
    print("==================================================")
    print()


def view_portfolio():
    portfolio = load_data()

    total_investment = 0
    total_current_value = 0

    if portfolio == []:
        print("Your portfolio is empty.")
        return

    for stock in portfolio:

        investment = stock["quantity"] * stock["buy_price"]
        current_value = stock["quantity"] * stock["current_price"]

        total_investment += investment
        total_current_value += current_value

        profit_loss = current_value - investment

        if investment == 0:
            profit_loss_percentage = 0
        else:
            profit_loss_percentage = (profit_loss / investment) * 100

        print()
        print("========================================")
        print("           STOCK DETAILS")
        print("========================================")

        print(f"Stock Name     : {stock['name']}")
        print(f"Stock Symbol   : {stock['symbol']}")
        print(f"Quantity       : {stock['quantity']}")
        print(f"Buy Price      : ₹{stock['buy_price']}")
        print(f"Current Price  : ₹{stock['current_price']}")
        print()

        print(f"Investment     : ₹{investment}")
        print(f"Current Value  : ₹{current_value}")
        print(f"Profit/Loss    : ₹{profit_loss}")
        print(f"Profit/Loss %  : {profit_loss_percentage:.2f}%")

        if profit_loss > 0:
            print("Status         : Profit")

        elif profit_loss < 0:
            print("Status         : Loss")

        else:
            print("Status         : No Profit / No Loss")

        print("========================================")

    best_stock, best_profit = find_best_stock(portfolio)

    print()
    print("========================================")
    print("        BEST PERFORMING STOCK")
    print("========================================")
    print(f"Stock Name     : {best_stock['name']}")
    print(f"Stock Symbol   : {best_stock['symbol']}")
    print(f"Profit/Loss    : ₹{best_profit}")
    print("========================================")

    worst_stock, worst_profit = find_worst_stock(portfolio)

    print()
    print("========================================")
    print("        WORST PERFORMING STOCK")
    print("========================================")
    print(f"Stock Name     : {worst_stock['name']}")
    print(f"Stock Symbol   : {worst_stock['symbol']}")
    print(f"Profit/Loss    : ₹{worst_profit}")
    print("========================================")

    overall_profit_loss = total_current_value - total_investment

    if total_investment == 0:
        print("The % is 0")

    else:
        print(
            f"Overall Profit/Loss % = "
            f"{(overall_profit_loss / total_investment) * 100:.2f}%"
        )

    if overall_profit_loss > 0:
        print("Overall_profit=", overall_profit_loss)

    elif overall_profit_loss < 0:
        print("Overall_loss=", overall_profit_loss)

    else:
        print("There is no Profit / Loss")

    portfolio_graph()


def portfolio_graph():
    portfolio = load_data()

    if portfolio == []:
        print("Your portfolio is empty.")
        return

    print()
    print("==================================================")
    print("          STOCK PERFORMANCE COMPARISON")
    print("==================================================")

    for stock in portfolio:

        investment = stock["quantity"] * stock["buy_price"]
        current_value = stock["quantity"] * stock["current_price"]

        if investment == 0:
            profit_loss_percentage = 0
        else:
            profit_loss = current_value - investment
            profit_loss_percentage = (profit_loss / investment) * 100

        bars = int(abs(profit_loss_percentage) / 2)

        if profit_loss_percentage > 0:
            graph = "█" * bars
            print(
                f"{stock['symbol']:<10} | "
                f"{graph} +{profit_loss_percentage:.2f}%"
            )

        elif profit_loss_percentage < 0:
            graph = "░" * bars
            print(
                f"{stock['symbol']:<10} | "
                f"{graph} {profit_loss_percentage:.2f}%"
            )

        else:
            print(
                f"{stock['symbol']:<10} | "
                f"0.00%"
            )

    print("--------------------------------------------------")
    print("Higher bar = Better performance")
    print("==================================================")



def remove_stock():
    portfolio = load_data()

    if portfolio == []:
        print("Your portfolio is empty.")
        return

    symbol = input("Enter Stock Symbol to remove: ")

    for stock in portfolio:
        if stock["symbol"] == symbol:

            transaction = {
                "action": "Removed",
                "name": stock["name"],
                "symbol": stock["symbol"],
                "quantity": stock["quantity"],
                "buy_price": stock["buy_price"],
                "current_price": stock["current_price"]
            }

            portfolio.remove(stock)
            save_data(portfolio)

            try:
                with open("transactions.json", "r") as file:
                    transactions = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                transactions = []

            transactions.append(transaction)

            with open("transactions.json", "w") as file:
                json.dump(transactions, file, indent=4)

            print()
            print("----------------------------")
            print("Stock removed successfully.")
            print("----------------------------")
            print()
            return

    print("Stock not found.")

def update_stock():    
    portfolio = load_data()

    if portfolio == []:
        print("Your portfolio is empty.")
        return

    symbol = input("Enter Stock Symbol to update: ")
    
    for stock in portfolio:
        if stock["symbol"] == symbol:

            stock["quantity"] = int(input("Enter new Quantity: "))
            stock["buy_price"] = float(input("Enter new Buy Price: "))
            stock["current_price"] = float(input("Enter new Current Price: "))

            transaction = {
                "action": "Updated",
                "name": stock["name"],
                "symbol": stock["symbol"],
                "quantity": stock["quantity"],
                "buy_price": stock["buy_price"],
                "current_price": stock["current_price"]
            }

            save_data(portfolio)

            try:
                with open("transactions.json", "r") as file:
                    transactions = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                transactions = []

            transactions.append(transaction)

            with open("transactions.json", "w") as file:
                json.dump(transactions, file, indent=4)

            print()
            print("---------------------------")
            print("Stock updated successfully")
            print("---------------------------")
            return

    print("Stock not found")

def search_stock():
    portfolio = load_data()

    if portfolio == []:
        print("Your portfolio is empty.")
        return

    symbol = input("Enter Stock Symbol to search: ")

    for stock in portfolio:
        if stock["symbol"] == symbol:

            print()
            print("========================================")
            print("             STOCK FOUND")
            print("========================================")

            print(f"Stock Name     : {stock['name']}")
            print(f"Stock Symbol   : {stock['symbol']}")
            print(f"Quantity       : {stock['quantity']}")
            print(f"Buy Price      : ₹{stock['buy_price']}")
            print(f"Current Price  : ₹{stock['current_price']}")

            investment = stock["quantity"] * stock["buy_price"]
            current_value = stock["quantity"] * stock["current_price"]
            profit_loss = current_value - investment

            print()
            print(f"Investment     : ₹{investment}")
            print(f"Current Value  : ₹{current_value}")
            print(f"Profit/Loss    : ₹{profit_loss}")

            print("========================================")
            return

    print("Stock not found.")
    

def portfolio_insights():
    portfolio = load_data()

    if portfolio == []:
        print("Your portfolio is empty.")
        return

    profit_stocks = 0
    loss_stocks = 0
    no_profit_loss = 0

    total_investment = 0
    total_current_value = 0

    for stock in portfolio:

        investment = stock["quantity"] * stock["buy_price"]
        current_value = stock["quantity"] * stock["current_price"]

        total_investment += investment
        total_current_value += current_value

        profit_loss = current_value - investment

        if profit_loss > 0:
            profit_stocks += 1

        elif profit_loss < 0:
            loss_stocks += 1

        else:
            no_profit_loss += 1

    overall_profit_loss = total_current_value - total_investment

    if total_investment == 0:
        overall_percentage = 0
    else:
        overall_percentage = (overall_profit_loss / total_investment) * 100

    best_stock, best_profit = find_best_stock(portfolio)
    worst_stock, worst_profit = find_worst_stock(portfolio)

    print()
    print("==================================================")
    print("              PORTFOLIO INSIGHTS")
    print("==================================================")

    print(f"Total Stocks          : {len(portfolio)}")
    print(f"Stocks in Profit      : {profit_stocks}")
    print(f"Stocks in Loss        : {loss_stocks}")
    print(f"No Profit / No Loss   : {no_profit_loss}")

    print()
    print(f"Total Investment      : ₹{total_investment}")
    print(f"Total Current Value   : ₹{total_current_value}")
    print(f"Overall Profit/Loss   : ₹{overall_profit_loss}")
    print(f"Overall Profit/Loss % : {overall_percentage:.2f}%")

    print()
    print("Best Performing Stock")
    print(f"Name                  : {best_stock['name']}")
    print(f"Symbol                : {best_stock['symbol']}")
    print(f"Profit/Loss           : ₹{best_profit}")

    print()
    print("Worst Performing Stock")
    print(f"Name                  : {worst_stock['name']}")
    print(f"Symbol                : {worst_stock['symbol']}")
    print(f"Profit/Loss           : ₹{worst_profit}")

    print("==================================================")


def investment_goal():
    portfolio = load_data()

    if portfolio == []:
        print("Your portfolio is empty.")
        return

    goal = float(input("Enter your Investment Goal: "))

    total_current_value = 0

    for stock in portfolio:
        current_value = stock["quantity"] * stock["current_price"]
        total_current_value += current_value

    remaining = goal - total_current_value

    print()
    print("==================================================")
    print("              INVESTMENT GOAL")
    print("==================================================")

    print(f"Investment Goal      : ₹{goal}")
    print(f"Current Portfolio    : ₹{total_current_value}")

    if remaining > 0:
        print(f"Amount Remaining     : ₹{remaining}")
        print("Goal Status          : Goal Not Reached")

    elif remaining < 0:
        print(f"Amount Above Goal    : ₹{abs(remaining)}")
        print("Goal Status          : Goal Achieved")

    else:
        print("Amount Remaining     : ₹0")
        print("Goal Status          : Goal Achieved")

    print("==================================================")
    

def transaction_history():
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)

    except FileNotFoundError:
        print()
        print("No transaction history found.")
        return

    except json.JSONDecodeError:
        print()
        print("Transaction history is empty.")
        return

    if transactions == []:
        print()
        print("No transaction history found.")
        return

    print()
    print("==================================================") 
    print("             TRANSACTION HISTORY")
    print("==================================================")

    for transaction in transactions:

        print()
        print(f"Action         : {transaction['action']}")
        print(f"Stock Name     : {transaction['name']}")
        print(f"Stock Symbol   : {transaction['symbol']}")
        print(f"Quantity       : {transaction['quantity']}")
        print(f"Buy Price      : ₹{transaction['buy_price']}")
        print(f"Current Price  : ₹{transaction['current_price']}")
        print("------------------------------------------")

    print("==================================================")