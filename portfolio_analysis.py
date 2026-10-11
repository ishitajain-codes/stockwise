def find_best_stock(portfolio):
    best_stock = None
    best_profit = 0

    for stock in portfolio:

        investment = stock["quantity"] * stock["buy_price"]
        current_value = stock["quantity"] * stock["current_price"]

        profit_loss = current_value - investment

        if best_stock == None:
            best_stock = stock
            best_profit = profit_loss

        else:
            if profit_loss > best_profit:
                best_stock = stock
                best_profit = profit_loss

    return best_stock, best_profit


def find_worst_stock(portfolio):
    worst_stock = None
    worst_profit = 0

    for stock in portfolio:

        investment = stock["quantity"] * stock["buy_price"]
        current_value = stock["quantity"] * stock["current_price"]

        profit_loss = current_value - investment

        if worst_stock == None:
            worst_stock = stock
            worst_profit = profit_loss

        else:
            if profit_loss < worst_profit:
                worst_stock = stock
                worst_profit = profit_loss

    return worst_stock, worst_profit