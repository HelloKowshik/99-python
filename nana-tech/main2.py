class User:
    def __init__(self, name, email, password, current_job_title):
        self.name = name
        self.email = email
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_title):
        self.current_job_title = new_title

    def get_user_info(self):
        print(f'{self.name}, {self.email}, {self.current_job_title}')    

user1 = User('Kowshik', 'k@k.com', '12345', 'Developer')
user1.get_user_info()              
