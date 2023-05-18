from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

from store_passwords import StoreUser


class Crypt(StoreUser):

	def __init__(self, login, password, len_key):
		super().__init__(login, password, len_key)
		self.encrypt_data = self.encrypt(self.password)
		self.pprint_status()

	@staticmethod
	def pprint_status():
		print('Запись создана!')

	def encrypt(self, password):

		key = get_random_bytes(int(self.len_key))
		cipher = AES.new(key, AES.MODE_EAX)
		cipher_text, tag = cipher.encrypt_and_digest(bytes(password, 'utf-8'))

		self.password = ''

		return {
			'cipher_text': b64encode(cipher_text).decode('utf-8'),
			'key': b64encode(key).decode('utf-8'),
			'nonce': b64encode(cipher.nonce).decode('utf-8'),
			'tag': b64encode(tag).decode('utf-8')
		}

	def decrypt(self):

		key = b64decode(self.encrypt_data['key'])
		cipher_text = b64decode(self.encrypt_data['cipher_text'])
		nonce = b64decode(self.encrypt_data['nonce'])
		tag = b64decode(self.encrypt_data['tag'])

		cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
		decrypted = cipher.decrypt_and_verify(cipher_text, tag)

		return decrypted.decode('utf-8')
