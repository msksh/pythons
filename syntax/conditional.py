#로그인 아이디 비번 코딩

user_id = input('id?')
user_pwd = input('password?')

'''
if user_input == '111111':
    print('Hello master')
else:
    print('Who are you?')
'''
#보기편한버전
'''
if user_id == 'sunghoon':
    if user_pwd == '111111':
        print('Hello master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
'''

#보기 더 편한버전
if user_id == 'sunghoon' and user_pwd == '111111':
        print('Hello master')
elif user_id == 'leezche' and user_pwd == '222':
        print('Hello master')
else:
    print('Who are you?')
