from crypter import Crypt


def check_answer(answer):
	if answer in ('y', 'n'):
		return True
	else:
		return False


def check_len_key():
	len_key = input('Введите длину ключа (16, 24 или 32 байта): ')
	if len_key in ('16', '24', '32'):
		return len_key
	else:
		print('Некорректно введены данные длины ключа!')
		return check_len_key()


def is_correct_password(user, password):
	if Crypt.decrypt(user) == password:
		print('Верный логин и пароль!')
	else:
		print('Неверный пароль!')
