# I wrote and debugged this code with all the convoluted "EAT" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes

def Eating(eat):
    return str(int(eat) * EATEATEAT)

def EAt(eat, eats):
    print(eat, eats)
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = ""
    while eat1 < len(eat) and eat2 < len(eats):
        if eateat%EATEATEAT == EATEATEATEATEAT//EATEATEATEAT:
            eAt += eats[eat2]
            eat2 += 1
        else:
            eAt += eat[eat1]
            eat1 += 1
        eateat += 1
    return eAt

def aten(eat):
    return eat[::EATEATEAT-EATEATEATEAT]

def eaT(eat):
    return Eating(eat[:EATEATEAT]) + aten(eat)

def aTE(eat):
    return eat#*eAT(eat)

def Ate(eat):
    return "Eat" + str(len(eat)) + eat[:EATEATEAT]

def Eat(answer):
    if len(answer) == 9:
        if str.isdigit(answer[:EATEATEAT]) and\
            str.isdigit(answer[len(answer) - EATEATEAT + 1:]):  # answer format: (0-9)(0-9)(0-9)(3 letters)(0-9)(0-9)(0-9)
                eateat = EAt(eaT(answer), Ate(aTE(aten(answer))))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + answer
                    print("absolutely EATEN!!! CTFlearn{",flag,"}")
                else:
                    print("thats not the answer. you formatted it fine tho, here's what you got\n>>", eateat)
        else:
            print("thats not the answer. bad format :(\
            \n(hint: 123abc456 is an example of good format)")
    else:
        print("thats not the answer. bad length :(")

print("what's the answer")
password = input()
EATEATEAT = len(password) // 3
EATEATEATEAT = EATEATEAT+1
EATEATEATEATEAT = EATEATEAT-1
Eat(password)
