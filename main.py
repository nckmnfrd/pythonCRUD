# main.py
from data_methods import DataMethods

def main():
    db = DataMethods('test_database')
    while True:
        print("Menu:")
        print("1. Display data")
        print("2. Delete data")
        print("3. Insert data")
        print("4. Quit")
        print("5. Update")
        choice = input("Enter your choice: ")

        if choice == '1':
            db.display()
        elif choice == '2':
            db.delete_row()
        elif choice == '3':
            db.insert_data()
        elif choice == '4':
            db.close()
            break
        elif choice == '5':
            db.update_row()
        else:
            print("Invalid choice. Please choose an option from the menu.")

if __name__ == '__main__':
    main()
