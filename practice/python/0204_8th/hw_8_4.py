class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        na_me = input("이름을 입력하세요 : ")
        a_ge = input("나이를 입력하세요 : ")
        try:
            self.user_data['이름'] = na_me
            self.user_data['나이'] = int(a_ge)
        except:
            print(f'나이는 숫자로 입력해야 합니다. ')
        

    def display_user_info(self):
        try:
            print(f"사용자 정보:\n이름: {self.user_data['이름']}\n나이: {self.user_data['나이']}")
        except:
            print(f'사용자 정보가 입력되지 않았습니다.')


user = UserInfo()
user.get_user_info()
user.display_user_info()

