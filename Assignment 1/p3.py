# 3.  Build an application that can be used to block certain websites from opening.

print("enter the website u want to block")
a = input()
ip = "127.0.0.1"
# host = "C:\Windows\System32\drivers\etc"
host_path = "D:"
file1 = open("host_path.txt", "r+")
website_list = file1.read()
if a in website_list:
	pass
else:
	file1.write(ip+" "+ a)
	print("website blocked successfully")
