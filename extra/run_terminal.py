###
#
# Add codes here


###



def run_banking_system():
    # Initialize the database and bank account
    customer_db = CustomerDatabase()
    bank_account = BankAccount()

    while True:
        option = main_menu()

        if option == "1":
            # Add Customer
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            new_customer = Customer(customer_id, name)
            customer_db.add_customer(new_customer)

        elif option == "2":
            # Deposit Money
            customer_id = input("Enter customer ID for deposit: ")
            customer = customer_db.get_customer_by_id(customer_id)
            if customer:
                amount = float(input(f"Enter amount to deposit for {customer.name}: "))
                bank_account.deposit(customer, amount)
            else:
                print("Customer not found!")

        elif option == "3":
            # Withdraw Money
            customer_id = input("Enter customer ID for withdrawal: ")
            customer = customer_db.get_customer_by_id(customer_id)
            if customer:
                amount = float(input(f"Enter amount to withdraw for {customer.name}: "))
                bank_account.withdraw(customer, amount)
            else:
                print("Customer not found!")

        elif option == "4":
            # Show All Customers
            print("\n--- Customer List ---")
            if customer_db.customers:
                for customer in customer_db.customers:
                    print(customer.display_info())
            else:
                print("No customers available.")

        elif option == "5":
            # Log Transactions
            print("\n--- Transaction Log ---")
            bank_account.log_transactions()

        elif option == "6":
            # Exit the system
            print("Exiting the banking system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

# Run the program in the terminal
if __name__ == "__main__":
    run_banking_system()
