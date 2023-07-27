# data_methods.py
from create_database import Database
import pandas as pd


class DataMethods(Database):
    def insert_data(self):
        # Fetch maximum user_id
        self.c.execute('''
              SELECT MAX(user_id) FROM users
              ''')
        max_id = self.c.fetchone()[0]
        if max_id is None:
            max_id = 0  # In case the table is empty

        # User input for new entry
        first_name = input("Enter the First Name: ")
        last_name = input("Enter the Last Name: ")
        favorite_food = input("Enter the Favorite Food: ")

        self.c.execute('''
                  INSERT INTO users (user_id, first_name, last_name, favorite_food)
                  VALUES (?, ?, ?, ?)
                  ''', (max_id + 1, first_name, last_name, favorite_food))
        self.conn.commit()

    def delete_row(self):
        request = input('Are you sure you like to delete your account? Yes or No\n')
        if request.lower() == 'yes':
            input_id = input('Enter your user ID number\n')

            self.c.execute('''
                      DELETE from users where user_id = ?
                      ''', (int(input_id),))
            self.conn.commit()
        else:
            print('did not enter a valid id')

    def update_row(self):
        # enter your user ID number
        print('Enter your user ID number')
        # if the user ID number is registered in the database, ask what needs to be updated
        user_id_num = input()
        if self.check_db(int(user_id_num)) is True:
            print('What would you like to update?')
            entryToUpdate = input(' 1. First Name\n 2. Last Name\n 3. Favorite Food\n')
            if entryToUpdate.lower() == 'first name' or entryToUpdate == '1':
                #update the first name column in the user_id row
                new_value = input("Enter the new First Name: ")
                self.update_entry(int(user_id_num), 'first_name', new_value)

            elif entryToUpdate.lower() == 'last name' or entryToUpdate == '2':
                #update the last name column in the user_id row
                new_value = input("Enter the new Last Name: ")
                self.update_entry(int(user_id_num), 'last_name', new_value)

            elif entryToUpdate.lower() == 'favorite food' or entryToUpdate == '3':
                #update their favorite food
                new_value = input("Enter the new Favorite Food: ")
                self.update_entry(int(user_id_num), 'favorite_food', new_value)

            else:
                print("That isn't a valid column to choose")
                # if the user id number is not within the database, state that its invalid
        else:
            print('Could not find this user ID within our records')

        # update the correct column based off row (user_id)
        # ask if there are any more updates needed
        # if not, go back to menu?

    def check_db(self, user_id):
        self.c.execute('''
                SELECT * FROM users WHERE user_id = ?
            ''', (user_id,))

        result = self.c.fetchone()
        if result:
            return True
        else:
            return False

    def update_entry(self, user_id, field, new_value):
        query = f"UPDATE users SET {field} = ? WHERE user_id = ?"
        self.c.execute(query, (new_value, user_id))
        self.conn.commit()


    def display(self):
        self.c.execute('''
              SELECT * FROM users
              ''')
        df = pd.DataFrame(self.c.fetchall(), columns=['user_id', 'first_name', 'last_name', 'favorite_food'])
        df.set_index('user_id', inplace=True)
        print(df)
