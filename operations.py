import sys
from db_client import DbClient
from pandas import DataFrame


CLIENT = DbClient()
GO_HOME = "You can enter 'exit' to go to home page."
BOOK_FIELD = ['book_id', 'title', 'authors', 'language_code','average_rating',]

def try_again():
    return input('Incorrect command, please enter again:')


def show_data(data,fields):
    if data:
        df = DataFrame(data, columns=fields)
        print(df.to_string(index=False))
    else:
        print("Empty")


def display(table: str, fields, query=""):
    f = ', '.join(fields)
    q = 'select {} from {} {};'.format(f, table, query)
    print(q)
    data = CLIENT.select(q)
    show_data(data, fields)
    return data


def show_options(options: dict) -> None:
    for opt in options.items():
        print("    {}: {}".format(opt[0], opt[1]))


def search(user_id):
    print("Use s command search the book you want.")
    print("You may search by:")
    options = {
        '-name $book_name': "Exact name of the book.",
        '-authors $authors_name': 'Authors names of the book.',
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
    fields = ','.join(BOOK_FIELD)
    query = "select "+ fields+" from books {} limit 20;"
    where_clause = ""
    if len(command) > 1:
        where_clause = "where "
        conditions = []
        where_dict = {
            '-name': "title = '{}'",
            '-authors': "authors = '{}'",
            '-tag': r"goodreads_book_id in (select books.goodreads_book_id from book_tags, tags, books where tags.tag_name = '{}\r' and tags.tag_id = book_tags.tag_id and books.goodreads_book_id = book_tags.goodreads_book_id)",
            '-read': 'book_id{}in (select book_id from to_read where user_id = '+ str(user_id) +')',
            'T': " ",
            'F': ' not ',
        }
        for i in range(1,len(command)):
            if command[i].startswith('-'):
                cmd = command[i]
                content = command[i+1]
                arg = where_dict[content] if content in where_dict else content
                while (i+2) < len(command) and not command[i+2].startswith('-'):
                    arg += (' ' + command[i+2])
                    i += 1
                condition = where_dict[cmd].format(arg)
                conditions.append(condition)
        where_clause += ' and '.join(conditions)
    data = CLIENT.select(query.format(where_clause))
    show_data(data,BOOK_FIELD)
    return


def read(user_id):
    book_id = input("Please enter the book id: ")
    fields = 'book_id, user_id'
    values = '{}, {}'.format(book_id, user_id)
    try:
        CLIENT.insert('to_read', fields, values)
    except:
        print("Book not exist or you have read it.")

    
def rate(user_id):
    book_id = input("Please enter the book id: ")
    query = "select * from ratings where book_id = {} and user_id = {}".format(book_id, user_id)
    if CLIENT.select(query):
        print('You have rated this book')
        return
    rating = input("Please enter your rating (0-10): ")
    comment = input("Please enter your comment: ")
    fields = 'user_id, book_id, rating, comment'
    values = "{}, {}, {}, '{}'".format(user_id, book_id, rating, comment)
    try:
        CLIENT.insert('ratings', fields, values)
    except:
        print("Book not exist")

def create_user(user_id):
    user_name = input("Plsease enter username: ")
    password = input("Please enter password: ")
    query = 'select max(user_id) from users'
    num = CLIENT.select(query)[0][0]
    user_id = 1 if not num else num + 1
    fields = 'user_id, user_name, password, admin'
    values = "{}, '{}', '{}', 1".format(user_id, user_name, password)
    try:
        CLIENT.insert('users', fields, values)
    except:
        print('Username already exists.')


def create_group(user_id):
    group_name = input("Plsease enter group name: ")
    query = 'select max(group_id) from orgs;'
    num = CLIENT.select(query)[0][0]
    group_id = 1 if not num else num + 1
    fields = 'group_id, group_name'
    values = "{}, '{}'".format(group_id, group_name)
    CLIENT.insert('orgs', fields, values)


def note(user_id):
    book_id = input("Plsease enter book id: ")
    print("Your previous notes:")
    notes = display('notes', ['note_number', 'note'], 'where user_id = {} and book_id = {}'.format(user_id, book_id))
    note = input("Enter your note or 'q' to quit: ")
    note_num = 1 if not notes else max([n[0] for n in notes]) + 1
    if note == 'q':
        return
    try:
        CLIENT.insert('notes', 'user_id, book_id, note_number, note', "{}, {}, {}, '{}'".format(user_id, book_id, note_num, note))
    except:
        print("Book not exist")

def join_group(user_id):
    orgs = display('orgs', ['group_id', 'group_name'])
    group_id = input("Please enter the group id to join: ")
    query = 'user_id = {}'.format(user_id)
    if int(group_id) not in [group[0] for group in orgs]:
        print("Group not exist.")
        return
    CLIENT.update('users', query, 'group_id', group_id)


def group_members(user_id):
    display('users', ['user_id', 'user_name', 'contact'], 'where group_id = (select group_id from users where user_id = {});'.format(user_id) )


def login() -> int:
    while(True):
        username = input('Please enter username: ')
        password = input('Password: ')
        query = "select password, user_id from users where user_name = '{}'".format(username)
        data = CLIENT.select(query)
        print(data)
        if not data:
            print('Username does not exist, please try again.\n')
        elif data[0][0] != password:
            print('Incorrect password, please try again.\n')
        else:
            return data[0][1]
