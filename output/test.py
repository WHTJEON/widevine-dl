def decrypt_url(ct_b64):
	from Cryptodome import Random
	from Cryptodome.Cipher import AES
	import base64
	from hashlib import md5
	
	BLOCK_SIZE = 16
	
	def pad(data):
		length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
		return data + (chr(length)*length).encode()
	
	def unpad(data):
		return data[:-(data[-1] if type(data[-1]) == int else ord(data[-1]))]
	
	def bytes_to_key(data, salt, output=48):
		assert len(salt) == 8, len(salt)
		data += salt
		key = md5(data).digest()
		final_key = key
		while len(final_key) < output:
			key = md5(key + data).digest()
			final_key += key
		return final_key[:output]
	
	def encrypt(message, passphrase):
		salt = Random.new().read(8)
		key_iv = bytes_to_key(passphrase, salt, 32+16)
		key = key_iv[:32]
		iv = key_iv[32:]
		aes = AES.new(key, AES.MODE_CBC, iv)
		return base64.b64encode(b"Salted__" + salt + aes.encrypt(pad(message)))
	
	def decrypt(encrypted, passphrase):
		encrypted = base64.b64decode(encrypted)
		assert encrypted[0:8] == b"Salted__"
		salt = encrypted[8:16]
		key_iv = bytes_to_key(passphrase, salt, 32+16)
		key = key_iv[:32]
		iv = key_iv[32:]
		aes = AES.new(key, AES.MODE_CBC, iv)
		return unpad(aes.decrypt(encrypted[16:]))


	KEY = '!@7now$%1api)6*'.encode()
	DECRYPTED = decrypt(ct_b64, KEY).decode('utf-8')
	print(DECRYPTED)

#ct_b64 = "U2FsdGVkX1/AkouUvhWcJpTLDt1B6n4Wf3MRJPS8P47NFjbLLZlsQqe+uR5LAVdc2Es5uvVj1ECYwbQMNSkSFfXiTTBV536a2QsPcxlo53IAHngpw2CSCNKVJbRCQh9dPiKW+swGJvapzdAIoOuDC0NyZKUdLr1NTdQe+knuLgXw/aD5XY+czOSxTlmAn79zCimNvDdsPKfbbUcKeny+io9H8GLcRKdaV4iDV6QB5yv1X85yoECgfQhNJAEIKwsVIliNRboDdr6qS4F4X6sXX7BzengyjtzOZUV0AM/0Ofoqt3Kfn7DDiwGebGTAnmHcalfzS4J6sDN2yT5bzns7U3ugSz9XREflct4UbrvizF/8LUtOFOKnH9YRhMVQ4UaL4oG6o2ojlhaOw0ZgboUoy9fqM0vZtDd2fJDlJ/87f4UiaJ7PWz9MP9xhm/d9J1YT+LHpJUq18mXVH5eoobfQcc5t5QbKlWjUrADIibea7YsF2ZiOKmyYUdaldGpMVyz5eKd6pV6F0nK7PY09iq4xVbl7iVHQjJ2Kp1WbYwfYg8xsBlm+yy0nCibyMrX8HsXNiWyhpVr+x8knvNEtrMCj3Az9tGdwbo25D0aNxFdjlFtKdqGYcx1fkNCe0qXnjunEj0hUCPJvzXZNm7RUcJ9LY7Rl4/ROa6ByUE+5JZq24LQ/EXt0YOBdFdzd7d+COkhtUMgvdEYLsf8RQAqLaBZWOw=="



	
	