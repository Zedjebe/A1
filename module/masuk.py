import os, sys

print ("Masukan Username dan Password !")
username = 'zedjebe'      
password = 'herocynaku'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "so mandi nga?"
			print "mandi jo dlu, bobou nga bnya orang binci",
			sys.exit()

		else:
			print "Password Kamu Salah!!!"
			print "Back Login"
			restart()

	else:
		print "Username Kamu Salah !!!"
		print "Back Login"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
