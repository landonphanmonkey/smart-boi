iq = 10
game_running = True
stress=0
print("u is stupid")
print("get smarter")
while game_running:
   
    print("1.read a book")
    print("2.scroll instagram")
    print("3.learn quantum physics")
    print("4.see ur stats")
    choice1 = input("")
    if choice1 == "1":
        iq +=5
        stress +=2
        print("You have read a book. Smarty good boy.")
    if choice1 == "2":
        iq -=2
        stress -=2
        print("U jst doomscrolled. Screenager. U got hella stressed out")
    if choice1 =="3":
        iq +=10
        stress +=8
        print("U learned quantum physics. GOOD BOII")
    if choice1 =="4":
        print(iq)
        print(stress)
    if iq==100:
        game_running=False
        print("U is smart now! GOOD BOY")
    if stress==20 and iq<0:
        game_running=False
        print("U too stressed out. You are dead")