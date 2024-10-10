class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.balance = 0.0

    def display_info(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Balance: {self.balance}"


class Transaction:
    def __init__(self, transaction_id, customer_id, amount, transaction_type):
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.amount = amount
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Customer ID: {self.customer_id}, Amount: {self.amount}, Type: {self.transaction_type}"


class BankAccount:
    def __init__(self):
        self.transactions = []

    def deposit(self, customer, amount):
        customer.balance += amount
        transaction = Transaction(len(self.transactions) + 1, customer.customer_id, amount, 'Deposit')
        self.transactions.append(transaction)
        print(f"Deposited {amount} to {customer.name}'s account. New Balance: {customer.balance}")

    def withdraw(self, customer, amount):
        if amount > customer.balance:
            print("Insufficient funds!")
        else:
            customer.balance -= amount
            transaction = Transaction(len(self.transactions) + 1, customer.customer_id, amount, 'Withdrawal')
            self.transactions.append(transaction)
            print(f"Withdrew {amount} from {customer.name}'s account. New Balance: {customer.balance}")

    def log_transactions(self):
        for transaction in self.transactions:
            print(transaction)


class CustomerDatabase:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Added: {customer.display_info()}")

    def get_all_customers(self):
        return [customer.display_info() for customer in self.customers]

    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer.display_info()
        return "Customer not found."


# Example usage
if __name__ == "__main__":
    # Creating customer database
    customer_db = CustomerDatabase()

    # Creating a bank account instance
    bank_account = BankAccount()

    # Adding customers
    customer_db.add_customer(Customer("001", "Alice"))
    customer_db.add_customer(Customer("002", "Bob"))
    customer_db.add_customer(Customer("003", "Charlie"))

    # Depositing money
    bank_account.deposit(customer_db.customers[0], 1000)  # Deposit for Alice
    bank_account.deposit(customer_db.customers[1], 500)   # Deposit for Bob

    # Withdrawing money
    bank_account.withdraw(customer_db.customers[0], 200)  # Withdraw for Alice
    bank_account.withdraw(customer_db.customers[1], 700)  # Should show insufficient funds

    # Logging transactions
    print("\nTransaction Log:")
    bank_account.log_transactions()

    # Retrieving all customers
    all_customers = customer_db.get_all_customers()
    print("\nAll Customers:")
    for customer_info in all_customers:
        print(customer_info)


import matplotlib.pyplot as plt

# Data for visualization
customers = customer_db.customers
names = [customer.name for customer in customers]
balances = [customer.balance for customer in customers]

# Creating the bar chart
plt.bar(names, balances)
plt.title("Customer Balances")
plt.xlabel("Customers")
plt.ylabel("Balance")
plt.show()

