maximum_stories = 404
usernum = input("On what floor of the building is your office?")
while int(usernum) >= maximum_stories:
	usernum = input("You entered: " + str(usernum) + ". But there are only " + str(maximum_stories) + " floors in this building. Try again... ")
print("Congrats! You work on floor: " + str(usernum))