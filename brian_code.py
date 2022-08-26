

# exercise for Brian

decor = '#' * 57

print(f"""    {decor}  
    #### Welcome to my awsome program made just for you! ####
    ####### I'm a great python dev, do you know? #########
    {decor}""")

name = input("Hello, stranger! You are a Palmtree? [y/n]     ")
palmtree = 'y'
brian = 'n'


if name == palmtree:
    print('Hello, your beautifull plant! Hope Brian is watering you correctly!')
elif name == brian:
    coffee_answer = input('Hi Brian! Have you aready had your coffee today?[y/n]   ')
    print(coffee_answer)
else:
    print('Hey, I dont know you! Let me talk with Palmtree and let Brian have your morning coffee in peace, please.')
    
if name == brian and coffee_answer == 'n':
    print('Take your time Brian, I can be here with my great friend Palmtree!')
elif name == brian and coffee_answer == 'y':
    print('Great! Now we can finally start! :D')
