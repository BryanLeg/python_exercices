nb_user1 = int(input("type a number "))
nb_user2 = int(input("type a second number "))
nb_user3 = int(input("type a third number "))

if nb_user1 > nb_user2 and nb_user1 > nb_user3:
    print(f'{nb_user1} is the greatest number')
elif nb_user2 > nb_user3 and nb_user2 > nb_user1:
    print(f'{nb_user2} is the greatest number')
else:
    print(f'{nb_user3} is the greatest number')