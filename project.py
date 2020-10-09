# An application which will take the the future of based upon the zodic sign
import random

Aries = ["You will be maintaining a good rapport with friends, and they will inspire you or enthuse you.",
         "You will be filled with positive energy on most of the days.",
         "It is seen that some of your long-standing aims and ambitions can come to fruition."]

Tauras = ["You need to work on finding out what it is to improve the present state of your life.",
          "You will remain energetic and fit.",
          "There will be positive vibrations that will help you in strengthening."]

Gemini = ["You will be happy with the support of luck and even the reduction of obstacles that were following you for a long time.",
          "You must seek an expert option before taking this position.",
          "You will find all the health problems slowly taking a back seat."]

Cancer = ["You will see the cash balance improving and this will enhance your fortune.",
          "Your sign from Capricorn will make you see an increase in expenditure",
          "Make sure that you do not rush up to any temptation and spend without looking up to the matter on hand."]

Leo = ["You will be filled with positive energy on most of the days.",
        "It is seen that some of your long-standing aims and ambitions can come to fruition.",
        "There will be positive vibrations that will help you in strengthening."]

Virgo = ["Use logic in the right direction and for constructive reasons, and you shall attain wisdom and success for sure.",
         "You will remain energetic and fit.",
         "There will be positive vibrations that will help you in strengthening."]

Libra = ["You will be happy with the support of luck",
         "Reduction of obstacles that were following you for a long time.",
         "There will be positive vibrations that will help you in strengthening."]
        
Scorpio = ["You shall get a better state in society and shall make you proud of your achievements in career.",
           "Reduction of obstacles that were following you for a long time.",
           "There will be positive vibrations that will help you in strengthening."]

Sagittarius = ["You will be filled with positive energy on most of the days.",
               "You will see the cash balance improving and this will enhance your fortune.",
               "You must seek an expert option before taking this position."]

Capricorn = ["Again, if planning to marry, then the year is very good to decide the same.",
             "You can automatically develop an inclination to gain good wealth.",
             "You are advised to be careful this year."]

Aquarius = ["You are keen on starting an enterprise, then there is a high possibility.",
            "You may pursue your dream and start your own business.",
            "You are particular to your diet and even make sure you take the food at the appropriate time during the day."]

Pisces = ["You will have to double your efforts to bring betterment in your career.",
          "You can put the saved money to better use during the year.",
          "your personal relationship and can put your plans to tie."]
# Runs endless
next = True
while next:
    print('''
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagittarius
    10) capricorn 
    11) Aquarius
    12) Pisces
    ''')
    s = input("Pick your sign number and Press enter.\n")
    ## Type casting str -> int
    # print(type(s))
    try:
        s = int(s)
    except :
        print("\nHey make sure with the number\n\n\n")

    # print(type(s))

    ############### THE MAIN LOGIC ###############


    # 1) Aries
    if s == 1:
        print(random.choice(Aries))

    # 2) Tauras
    elif s == 2:
        print(random.choice(Tauras))

    # 3) Gemini
    elif s == 3:
        print(random.choice(Gemini))

    # 4) Cancer
    elif s == 4:
        print(random.choice(Cancer))

    # 5) Leo
    elif s == 5:
        print(random.choice(Leo))

    # 6) Virgo
    elif s == 6:
        print(random.choice(Virgo))

    # 7) Libra
    elif s == 7:
        print(random.choice(Libra))

    # 8) Scorpio
    elif s == 8:
        print(random.choice(Scorpio))

    # 9) Sagittarius
    elif s == 9:
        print(random.choice(Sagittarius))

    # 10) capricorn 
    elif s == 10:
        print(random.choice(Capricorn))

    # 11) Aquarius
    elif s == 11:
        print(random.choice(Aquarius))

    # 12) Pisces
    elif s == 12:
        print(random.choice(Pisces))

    else :
        print("\n\n\nHey make sure the number range (1-12).")
    
    # break the loop
    if input("\n\n\nShall we do again? (y,[N]) ") == "y":
        pass
    else:
        next = False




