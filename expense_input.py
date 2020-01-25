
class ExpenseInput:

    def __init__(self):
        pass

    def get_expense_day(self):
        date = input("Enter date for tracking expenses: ")
        return date

    def get_items(self):
        item = input("Item: ")
        quantity = input("Quantity: ")
        price = input("Price: ")
        store = input("Store: ")
        savings = input("Savings: ")
        item_dict = {"Item": item, "Quantity": quantity, "Price": price,
                      "Store": store, "Savings": savings}
        return item_dict


