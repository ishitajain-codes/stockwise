from portfolio import add_stock, view_portfolio,remove_stock,update_stock,search_stock,portfolio_insights,investment_goal,transaction_history


while True:

    print("==================================================")
    print("                    STOCKWISE")
    print("             Your Portfolio Tracker")
    print("==================================================")

    print()
    print("                 MAIN MENU")
    print("--------------------------------------------------")
    print("[1]  Add Stock")
    print("[2]  Remove Stock")
    print("[3]  View Portfolio")
    print("[4]  Update Portfolio")
    print("[5]  Search Stock")
    print("[6]  Portfolio Insights")
    print("[7]  Investment Goal")
    print("[8]  Transaction History")
    print("[9]  Exit")
    print("--------------------------------------------------")
    
    user_choice = int(input("Enter your choice listed above :- "))
 
 

    if user_choice == 1:
        add_stock()

    elif user_choice == 2:
       remove_stock()
       
    elif user_choice == 3:
        view_portfolio()

    elif user_choice == 4:
        update_stock()
        
    elif user_choice == 5:
       search_stock()
       
    elif user_choice == 6:
       portfolio_insights()

    elif user_choice == 7:
        investment_goal()

    elif user_choice == 8:
        transaction_history()
        
    elif user_choice == 9:
        print("Exit.. Thank you for using Portfolio Manager !")
        
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 9.")