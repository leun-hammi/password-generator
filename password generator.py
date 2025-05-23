import random

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
symbol = ["!","+","#","$","%","&","*","(",")"]
number = ["0","1","2","3","4","5","6","7","8","9"]

print("HEY! WELCOME TO PASSWORD GENERATOR!\n  i know why your here! it is cuz your too dumb to create password without the petty hacker figuring it out!\n but dont cry we got u now!! ")

no_letter = int(input("how many letters do u need in ur password?"))
no_symbol = int(input("how many symbols do u need in ur password?"))
no_number = int(input("how many numbers do u need in ur password?"))

password_list = []

for char in range(1,no_letter+1):
    password_list.append(random.choice(letter))
for char in range(1,no_symbol+1):
    password_list.append(random.choice(symbol))
for char in range(1,no_number+1):
    password_list.append(random.choice(number))

random.shuffle(password_list)
   
password=" "

for char in password_list :
    password+=char

print(f"YOUR NEW POWERFUL PASSWORD IS...{password}")
print("\n now the hacker will get a brain attack if he tries to crack your password!\n and... IT'S ALL THANKS TO US! so don't you dare forget us!")
