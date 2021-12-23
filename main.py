import operations


def main():
    print('Please choose an option:')
    login_opt = {
        'login': 'Login with username and password.',
        'register': 'Create a user.',
    }
    operations.show_options(login_opt)
    if input() == 'register':
        user_id = operations.create_user(1)
    else:
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
            'recommand': 'The system recommands a book for you.',
            'quit': 'Quit.'
        }
        operations.show_options(options)
        opt = input()
        if opt == 'quit':
            return
        while opt not in options and opt not in admin_opt:
            opt = operations.try_again()
            if opt == 'quit':
                return
        try:
            getattr(operations, opt)(user_id)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
