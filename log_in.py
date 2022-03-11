import os
import sys



class User:
    def __init__(self, user_info_file = "user.txt"):
        self.name = None
        self.login = None
        self.password = None
        self.age = None
        self.user_info_file = user_info_file
        self.all_users = []
        self.welcome()

    def welcome(self):
        reg_log = input('''
        Please choose one of the options:
        [1] register
        [2] login
        [3] exit
        ''')

        while reg_log.strip() not in ['1', '2']:
            os.system('cls')
            print("incorrect input!")
            reg_log = input('''
            choose on of these options:
            [1] register
            [2] log in 
            ''')

        if reg_log == '1':
            self.register()
        elif reg_log == '2':
            self.log_in()
        else:
            sys.exit()


    def register(self):
        pass



    def log_in(self):
        if self.login is not None and self.password is not None:
            print('You are already logged in!')
        else:
            if self.file_empty():
                print('you are not registered')
            else:
                #user login
                os.system('cls')
                self.login = input('your login - ').strip()
                while not self.login.isalnum():
                    os.system('cls')
                    print('choose alnum signs - ')
                    self.login = input('your login - ').strip()


            #user password
            self.password = input('your password - ')
            while not self.password or len(self.password) < 6:
                os.system('cls')
                print('password should contain at least 6 signs')
                self.password = input('your password - ')


        self.get_all_user_in_db()
        if self.user_exists():
            print('you are logged in successfully')
        else:
            print('this user does not exists') 


    def log_out(self):
        pass

    def change_login(self):
        pass

    def change_password(self):
        pass

    def delete_account(self):
        pass
    def file_empty(self):
        with open(self.user_info_file) as file:
            text = file.read()
        return text == ''         
    
















