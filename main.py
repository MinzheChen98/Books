import sys
from db_client import DbClient

            
CLIENT = DbClient()
GO_HOME = "You can enter 'exit' to go to home page."

def try_again():
    return input('Incorrect command, please enter again:')

def show_options(options: dict) -> None:
    for opt in options.items():
        print("    {}: {}".format(opt[0], opt[1]))

def search():
    print("Use s command search the book you want.")
    print("You may search by:")
    options = {
        '-name $book_name': "Exact name of the book.",
        '-nc $book_name': "Name contains.",
        '-tag $tab_name': 'Tag name.',
        '-read T': 'Books you are reading.' ,
        '-read F': 'Books you are not reading.', 
    }
    show_options(options)
    print(GO_HOME)
    command = input().split()
    while command[0] != 's':
        if command[0] == 'exit':
            return
        command = try_again()
    print(CLIENT.select("select * from users limit 2"))
    return
    
    
def main():
    while True:
        print("\nWelcome to book reading system.")
        print('Please choose options:')
        options = {
            'create_user': 'Create a user.',
            'search': 'Search a book.',
            'read': 'Start reading a book',
            'rate': 'rate a book',
            'quit': 'Quit.'
        }
        show_options(options)
        opt = input()
        if opt == 'quit':
            break
        while opt not in options:
            opt = try_again()
        print()
        getattr(sys.modules[__name__], opt)()


def create_user():
    user_name = input("Plsease enter username: ")
    password = input("Please enter password: ")
    query = 'select max(user_id) from users'
    user_id = CLIENT.select(query)[0][0] + 1
    fields = 'user_id, user_name, password, admin'
    values = "{}, '{}', '{}', 1".format(user_id, user_name, password)
    CLIENT.insert('users', fields, values)


if __name__ == "__main__":
    main()