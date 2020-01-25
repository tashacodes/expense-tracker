from expense_input import ExpenseInput


def collect_data():
    tracker = ExpenseInput()
    date = tracker.get_expense_day()
    print(date)
    shopping = input("Did you shop today? (y/n): ")
    if shopping.lower() == 'y':
        item_count = 0
        items_dict = dict()
        daily_tracker_dict = dict()
        no_of_items = int(input("How many items do you want to add?: "))
        while no_of_items != 0:
            item = tracker.get_items()
            item_count += 1
            items_dict[item_count] = item
            no_of_items -= 1

        daily_tracker_dict[date] = items_dict
        # print(items_dict)
        return items_dict
    else:
        print("Have a good day!")

def main():
    expense_data = collect_data()
    print(expense_data)
    more_items = input("Do you have more items to add? (y/n): ")
    while more_items.lower() != 'y':
        more_expenses = collect_data()
        print(more_expenses)



if __name__ == main():
    main()
