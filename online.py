import time, vk_api

Login = input('Ваш логин :')
Pass = input('Ваш пароль :')

try:
	vk= vk_api.VkApi(login = Login, password = Pass)
	vk.auth()
	print('login successfull :)')
	
except:
	print('error occured :(')
	exit(0)
	
def online():
	try:
		vk.method('account.setOnline')
		
	except:
		print('error :(')
		
while True:
	online()
	time.sleep(20)