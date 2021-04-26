usernum = input("Gimmy a number greater than 100: ")
while int(usernum) <= 100:
	usernum = input(str(usernum) + " is less than 100, dummy. Try again... I've got all day...: ")
print(str(usernum) + " is greater than 100! Good work.")