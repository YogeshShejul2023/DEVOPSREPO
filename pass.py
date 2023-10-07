cp="123456"
while True: 
    up=input("Enter the password")
    if cp==up:
        print("Password id correct,access granted")
        break
    else:
        print("PAssword incorrect Try again")