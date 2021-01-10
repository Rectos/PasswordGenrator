import random 
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!£$%^&*(')"
while 1 :
    password_len = int(input("what length would you like your password to be : "))
    password_count = int(input("How many password you like : "))
    for i in range(0,password_count):
        password =""
        for i in range(0,password_len):
            password_char = random.choice(chars)
            password = password + password_char 
        print(" here is your password : ", password)





