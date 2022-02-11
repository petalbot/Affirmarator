#introduction
print("Welcome to the subliminal affirmation generator!\n")
print("Here you can enter information about your subliminal topic and receive affirmations based on the style of your choice.\n")
print("\n")
print("Menu:\n")
print("1: Scientific: Affirmations exaggerated with the concept of science\n")
print("2: Emotional: Affirmations that play into feelings and gratitude\n")
print("3: Universal: Affirmations emphasizing the extent of possession\n")
print("4: Changes: Affirmations based on the concept of something changing quickly\n")
print("5: Reality: Affirmations based on existence and reality\n")
print("\n")
print("For more information on affirmations, you can search for YouTube videos about manifestation or subliminals.\n")

#user input
#affirmation style
while(True):
    num = input("Enter the style you prefer: ")
    if(int(num)== 1 or int(num)== 2 or int(num)== 3 or int(num)== 4 or int(num)== 5 ):
        break
    else:
        print("Please enter a valid value.")
       
#feature        
feature = input("Enter what you want to change: ")

#amount
while(True):
    nf = input("Is it singular or plural? (s/p)")
    if(nf=="s" or nf=="S"):
        ia = "is"
        a = "a"
        break
    elif(nf=="p" or nf=="P"):
        ia = "are"
        a = ""
        break
    else:
        print("Please enter a valid value.")
        
#modifiers        
adjective =  input("Enter how you want it to be (adjective): ")
er = input("Enter the comparative form of this adjective: ")
ef = input("Enter the superlative form of this adjective: ")
print("\n")

#output affirmations
#scientific
if(int(num)==1):
    print("You have the most scientifically", adjective, feature, ".")
    print("Your", feature, ia, "supernaturally", adjective, "forever.")
    print("Scientists say you have the", ef, feature, "in the world.")
    print("According to science, you have the", ef, feature, "on earth.")
    print("Your", feature, "is scientifically", adjective, "forever.")
    print("You always have the", ef, feature, "of all time.")
    print("It is a scientific fact that", feature, ia, "permanently", adjective, ".")
    print("Every scientist knows that you have the", ef, feature)
#emotional
elif(int(num)==2):
    print("It's so wonderful that you have the", ef, feature, "ever.")
    print("It's so lovely that your", feature, ia, "so", adjective, "every day.")
    print("You always know that you have the most wonderfully", adjective, feature, "ever.")
    print("How do you have such", ia, "beautifully", adjective, feature, "forever?")
    print("Just letting you know your", feature, ia, "permanently", adjective, "for life.")
    print("Just reminding you that you have the", ef, feature, "for eternity.")
#universal
elif(int(num)==3):
    print("You literally have the", ef, feature, "in existence.")
    print("It is a universal truth that your", feature, ia, "the", ef, feature, "to exist.")
    print("It is a well known fact that you have the", ef, feature, "on the planet.")
    print("Everyone knows that you have the", ef, feature, "ever known to exist.")
    print("The whole world loves how your", feature, ia, "the", ef, "in history.")
#changes
elif(int(num)==4):
    print("Your", feature, ia, "getting", er, "every single second.")
    print("Your", feature, "becomes", er, "faster than light speed.")
    print("Your", feature, "is constantly getting", er, "every single day.")
#reality
elif(int(num)==5):
    print("Reality fully expresses that you have the", ef, feature, "ever.")
    print("Reality fully reflects the fact that your", feature, ia, adjective, "forever.")
    print("You are always in a reality where your", feature, ia, "the", ef, "of all.")