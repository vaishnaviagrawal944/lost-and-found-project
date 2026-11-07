
import json
import os

FILE = "items.json"


# Load saved items
def load_items():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


# Save items
def save_items(items):
    with open(FILE, "w") as file:
        json.dump(items, file, indent=4)


# Add a new item
def add_item(items):

    print("\n--- Report an Item ---")

    name = input("Enter item name: ")
    category = input("Enter category: ")
    location = input("Enter location: ")

    print("1. Lost Item")
    print("2. Found Item")

    choice = input("Enter your choice: ")

    if choice == "1":
        status = "Lost"
    elif choice == "2":
        status = "Found"
    else:
        print("Invalid choice!")
        return

    item = {
        "name": name,
        "category": category,
        "location": location,
        "status": status
    }

    items.append(item)
    save_items(items)

    print("\nItem reported successfully!")


# Display all items
def view_items(items):

    print("\n--- All Reported Items ---")

    if len(items) == 0:
        print("No items reported yet.")
        return

    for i, item in enumerate(items, start=1):

        print("\nItem Number:", i)
        print("Name:", item["name"])
        print("Category:", item["category"])
        print("Location:", item["location"])
        print("Status:", item["status"])


# Search for an item
def search_item(items):

    print("\n--- Search Item ---")

    search = input("Enter item name: ").lower()

    found = False

    for item in items:

        if search in item["name"].lower():

            print("\nItem Found!")
            print("Name:", item["name"])
            print("Category:", item["category"])
            print("Location:", item["location"])
            print("Status:", item["status"])

            found = True

    if not found:
        print("No matching item found.")


# Delete recovered item
def delete_item(items):

    view_items(items)

    if len(items) == 0:
        return

    try:
        number = int(input("\nEnter item number to delete: "))

        if 1 <= number <= len(items):

            removed = items.pop(number - 1)
            save_items(items)

            print(removed["name"], "deleted successfully!")

        else:
            print("Invalid item number!")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def main():

    items = load_items()

    while True:

        print("\n================================")
        print("   LOST & FOUND MANAGEMENT")
        print("================================")

        print("1. Report Lost or Found Item")
        print("2. View All Items")
        print("3. Search Item")
        print("4. Delete Recovered Item")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_item(items)

        elif choice == "2":
            view_items(items)

        elif choice == "3":
            search_item(items)

        elif choice == "4":
            delete_item(items)

        elif choice == "5":
            print("\nThank you for using Lost & Found!")
            break

        else:
            print("Invalid choice! Try again.")


# Start the program
main()
