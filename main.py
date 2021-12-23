import operations


def main():
    user_id = operations.login()
    while True:
        print("\nWelcome to book reading system.")
        print('Please choose options:')
        admin_opt = {
            'create_user': 'Create a user.',
            'create_group': 'Create a group.',
            'join_group': 'Join a group.',
            'group_members': 'Show group members.',
        }
        operations.show_options(admin_opt)
        print()
        options = {
            'search': 'Search a book.',
            'read': 'Start reading a book',
            'rate': 'Rate a book',
            'note': 'Take notes while reading a book.',
            'quit': 'Quit.'
        }
        operations.show_options(options)
        opt = input()
        if opt == 'quit':
            break
        while opt not in options and opt not in admin_opt:
            opt = operations.try_again()
        try:
            getattr(operations, opt)(user_id)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # query = 'select tag_name from tags where tag_id =2124;'
    # data = CLIENT.select(query)[0]
    # print(data)
    main()
