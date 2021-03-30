print("Hi, welcome to an exciting python game")
print('''About: There is a lucky_number which is unknown. So, guess the number. 
If you guess it, you will get Great. if you guess less than the number, you will get Very close and
if, you guess more, you will get Very Bad...''')
print("To get the answer, go to http://pyanswers.website2.me")
lucky_number=input("Enter a number")
lucky_number = int(lucky_number)
if lucky_number==25:
    print('Great, you guessed the correct number')

elif lucky_number<25:
    print('Very close')

else:
    print('Very Bad')

