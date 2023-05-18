from validate import *

if __name__ == '__main__':
    flag = False
    list_users = []
    while not flag:
        answer = input('Хотите зашифровать или проверить пароль? (y, n) ')
        if check_answer(answer):
            if answer == 'y':
                login = input('Введите логин: ')
                password = input('Введите пароль: ')
                len_key = check_len_key()
                list_users.append(Crypt(login, password, len_key))
            else:
                is_user = False
                login = input('Введите логин: ')
                password = input('Введите пароль: ')
                for user in list_users:
                    if user.login == login:
                        is_correct_password(user, password)
                        is_user = True
                        break
                if not is_user:
                    print('Пользователя с таким логином нет!')
        else:
            print('Некорректно введен ответ!')
            continue
        is_continue = False
        while not is_continue:
            answer = input('Хотите продолжить? (y, n) ')
            if check_answer(answer):
                is_continue = True
                if answer == 'y':
                    continue
                else:
                    flag = True
            else:
                print('Некорректно введен ответ!')
