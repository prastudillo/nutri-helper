import math
import random

# food exchange class
class foodExchange:
    def __init__(self, name, cho, pro, fat):
        self.name = name
        self.cho = cho
        self.pro = pro
        self.fat = fat

#for rounding to the nearest 5
def mround(x):
    return 5*round(x/5)
def roundto50(x):
    return 50*round(x/50)



#getting the BMI 


#getting the inputs
# height = float(input("Enter height in cm: "))
# tannhausers = (height - 100)-(0.10*(height-100))
# activityFactor = float(input("Enter activity factor: "))
# calBudget = roundto50(tannhausers*activityFactor)
calBudget = float(input("Enter caloric budget: "))

print(calBudget)
carbs = float(input("Please enter carbs percentage: "))/100
protein = float(input("Please enter protein percentage: "))/100
fat = float(input("Please enter fat budget: "))/100

carbsGrams = mround((calBudget*carbs)/4)
proteinGrams = mround((calBudget*protein)/4)
fatGrams = mround((calBudget*fat)/9)
 
print("Carbs (g): " + str(carbsGrams) + "\nProtein (g): " + str(proteinGrams) + "\nFat (g): " + str(fatGrams))

#food exchange list
foodxl = list()
#food exchanges objects
#Vegetables
vegA = foodExchange("vegA",3,1,0)
foodxl.append(vegA)
vegB = foodExchange("vegB",3,1,0)
foodxl.append(vegB)
#Fruits
fruits = foodExchange("fruits",10,0,0)
foodxl.append(fruits)
#Milk
wholeMilk = foodExchange("wholeMilk",12,8,10)
foodxl.append(wholeMilk)
lowfatMilk = foodExchange("lowfatMilk",12,8,5)
foodxl.append(lowfatMilk)
skimmedMilk = foodExchange("skimmedMilk",12,8,0)
foodxl.append(skimmedMilk)
#Rice
rice = foodExchange("rice",23,2,0)
foodxl.append(rice)
#Meat
lowfatMeat = foodExchange("lowfatMeat",0,8,1)
foodxl.append(lowfatMeat)
medfatMeat = foodExchange("medfatMeat",0,8,6)
foodxl.append(medfatMeat)
highfatMeat = foodExchange("highfatMeat",0,8,10)
foodxl.append(highfatMeat)
#Fat
fatGrp = foodExchange("fatGrp",0,0,5)
foodxl.append(fatGrp)
#Sugar
sugar = foodExchange("sugar",5,0,0)
foodxl.append(sugar)

#Preferences
preferences = list()
print("Enter 1 if YES, 0 if NO ")

for i in foodxl:
    answer = int(input("Do you want " + str(i.name) + ": "))
    if(answer == 1):
        preferences.append(i)
    
print("Preferences: " + str([o.name for o in preferences]))

#Distribution

# carbsGrams= 245
# proteinGrams = 95
# fatGrams = 15
currCho = 0
currPro = 0
currFat = 0

""" for i in preferences:
    for j in range(1,random.randint(1,5)):
        if currCho < carbsGrams and currPro < proteinGrams and currFat < fatGrams:
            currCho += i.cho
            currPro += i.pro
            currFat += i.fat
            print(i.name)
            print(currCho, currPro, currFat)
        
 """

#filter the preferences
#cho and pro only
choAndPro = list()
for i in preferences:
    if i.fat == 0 and i.name != "fruits":
        choAndPro.append(i)
#pro and fat only
proAndFat = list()
for i in preferences:
    if i.cho == 0:
        proAndFat.append(i)
#fat only
fatOnly = list()
for i in preferences:
    if i.cho and i.pro == 0:
        fatOnly.append(i)
#cho only
choOnly = list()
for i in preferences:
    if i.pro == 0 and i.fat == 0:
        choOnly.append(i)

meatOnly = list()
for i in preferences:
    if i.name == "lowfatMeat" or i.name == "medfatMeat" or i.name =="highfatMeat":
        meatOnly.append(i)


outputList = list()

# reaches the fat requirement
print("Food Exchange generation...")
while currFat < fatGrams:
    for i in preferences:
        for j in range(1,random.randint(1,5)):
            if currFat < fatGrams:
                currCho += i.cho
                currPro += i.pro
                currFat += i.fat
                outputList.append(i)
                print(i.name)
                print(currCho, currPro, currFat)     


print("CHO AND PRO")
#reaches the carbs requirement
while currCho < carbsGrams:
    for i in choAndPro:

        for j in range(1,random.randint(1,5)):
            
            
            if currCho < carbsGrams:
                currCho += i.cho
                currPro += i.pro
                outputList.append(i)

                print(i.name)
                print(currCho, currPro, currFat)   

# protein is not reached
while currPro < proteinGrams:
    for i in meatOnly:
    
        for j in range(1,random.randint(1,5)):
            
            
            if currPro < proteinGrams:
                currPro += i.pro
                currFat += i.fat
                outputList.append(i)

                print(i.name)
                print(currCho, currPro, currFat)  



# protein is reached but cho and fat exceeded
#subtract cho and fat

vegaCount = 0
vegbCount = 0
fruitCount = 0
wholemilkCount = 0
lowfatmilkCount = 0
skimmedmilkCount = 0
riceCount = 0
lfmeatCount = 0
mfmeatCount = 0
hfmeatCount = 0
fCount = 0
sCount = 0
for i in outputList:
    if i.name == "vegA":
        vegaCount += 2
    elif i.name == "vegB":
        vegbCount += 1
    elif i.name == "fruits":
        fruitCount += 1
    elif i.name == "wholeMilk":
        wholemilkCount += 1
    elif i.name == "lowfatMilk":
        lowfatmilkCount += 1
    elif i.name == "skimmedMilk":
        skimmedmilkCount += 1
    elif i.name == "rice":
        riceCount += 1
    elif i.name == "lowfatMeat":
        lfmeatCount += 1
    elif i.name == "medfatMeat":
        mfmeatCount += 1
    elif i.name == "highfatMeat":
        hfmeatCount += 1
    elif i.name == "fatGrp":
        fCount += 1
    else: #sugar
        sCount += 1



while currCho != carbsGrams or currPro != proteinGrams or currFat != fatGrams:

    #Output exchanges
    print("")
    print("FOOD EXCHANGES")
    print("Vegetable A: " + str(vegaCount/2))
    print("Vegetable B: " + str(vegbCount))
    print("Fruit: " + str(fruitCount))
    print("Whole Milk: " + str(wholemilkCount))
    print("Low Fat Milk: " + str(lowfatmilkCount))
    print("Skimmed Milk: " + str(skimmedmilkCount))
    print("Rice: " + str(riceCount))
    print("Low Fat Meat: " + str(lfmeatCount))
    print("Medium Fat Meat: " + str(mfmeatCount))
    print("High Fat Meat: " + str(hfmeatCount))
    print("Fat: " + str(fCount))
    print("Sugar: " + str(sCount))


    print("")
    print("TARGET STATS: ")
    print("Target cho: " + str(carbsGrams) + "    Target pro:" + str(proteinGrams) + "    Target fat: " + str(fatGrams))
    print("")
    print("CURRENT STATS: ")
    print("Current cho: " + str(currCho) + "    Current pro: " + str(currPro) + "    Current fat: " + str(currFat))

    decision = input("Do you want to add or lessen?: ")
    if decision == "lessen":
        toBeRemoved = input("Enter the name of the food exchange that will be lessen: ")
        if toBeRemoved == "vegA":
            vegaCount -= 2
            currCho -= vegA.cho
            currPro -= vegA.pro
            currFat -= vegA.fat
        elif toBeRemoved == "vegB":
            vegbCount -= 1
            currCho -= vegB.cho
            currPro -= vegB.pro
            currFat -= vegB.fat
        elif toBeRemoved == "fruits":
            fruitCount -= 1
            currCho -= fruits.cho
            currPro -= fruits.pro
            currFat -= fruits.fat
        elif toBeRemoved == "wholeMilk":
            wholemilkCount -= 1
            currCho -= wholeMilk.cho
            currPro -= wholeMilk.pro
            currFat -= wholeMilk.fat
        elif toBeRemoved == "lowfatMilk":
            lowfatmilkCount -= 1
            currCho -= lowfatMilk.cho
            currPro -= lowfatMilk.pro
            currFat -= lowfatMilk.fat
        elif toBeRemoved == "skimmedMilk":
            skimmedmilkCount -= 1
            currCho -= skimmedMilk.cho
            currPro -= skimmedMilk.pro
            currFat -= skimmedMilk.fat
        elif toBeRemoved == "rice":
            riceCount -= 1
            currCho -= rice.cho
            currPro -= rice.pro
            currFat -= rice.fat
        elif toBeRemoved== "lowfatMeat":
            lfmeatCount -= 1
            currCho -= lowfatMeat.cho
            currPro -= lowfatMeat.pro
            currFat -= lowfatMeat.fat
        elif toBeRemoved== "medfatMeat":
            mfmeatCount -= 1
            currCho -= medfatMeat.cho
            currPro -= medfatMeat.pro
            currFat -= medfatMeat.fat
        elif toBeRemoved== "highfatMeat":
            hfmeatCount -= 1
            currCho -= highfatMeat.cho
            currPro -= highfatMeat.pro
            currFat -= highfatMeat.fat
        elif toBeRemoved== "fatGrp":
            fCount -= 1
            currCho -= fatGrp.cho
            currPro -= fatGrp.pro
            currFat -= fatGrp.fat
        elif toBeRemoved== "sugar":
            sCount -= 1
            currCho -= sugar.cho
            currPro -= sugar.pro
            currFat -= sugar.fat

        else: 
            print("Please enter correct exchange name")
    elif decision == "add":
        toBeIncreased = input("Enter the name of the food exchange that will be increased: ")
        if toBeIncreased == "vegA":
            vegaCount += 2
            currCho += vegA.cho
            currPro += vegA.pro
            currFat += vegA.fat
        elif toBeIncreased == "vegB":
            vegbCount += 1
            currCho += vegB.cho
            currPro += vegB.pro
            currFat += vegB.fat
        elif toBeIncreased == "fruits":
            fruitCount += 1
            currCho += fruits.cho
            currPro += fruits.pro
            currFat += fruits.fat
        elif toBeIncreased == "wholeMilk":
            wholemilkCount += 1
            currCho += wholeMilk.cho
            currPro += wholeMilk.pro
            currFat += wholeMilk.fat
        elif toBeIncreased == "lowfatMilk":
            lowfatmilkCount += 1
            currCho += lowfatMilk.cho
            currPro += lowfatMilk.pro
            currFat += lowfatMilk.fat
        elif toBeIncreased == "skimmedMilk":
            skimmedmilkCount += 1
            currCho += skimmedMilk.cho
            currPro += skimmedMilk.pro
            currFat += skimmedMilk.fat
        elif toBeIncreased == "rice":
            riceCount += 1
            currCho += rice.cho
            currPro += rice.pro
            currFat += rice.fat
        elif toBeIncreased== "lowfatMeat":
            lfmeatCount += 1
            currCho += lowfatMeat.cho
            currPro += lowfatMeat.pro
            currFat += lowfatMeat.fat
        elif toBeIncreased== "medfatMeat":
            mfmeatCount += 1
            currCho += medfatMeat.cho
            currPro += medfatMeat.pro
            currFat += medfatMeat.fat
        elif toBeIncreased== "highfatMeat":
            hfmeatCount += 1
            currCho += highfatMeat.cho
            currPro += highfatMeat.pro
            currFat += highfatMeat.fat
        elif toBeIncreased== "fatGrp":
            fCount += 1
            currCho += fatGrp.cho
            currPro += fatGrp.pro
            currFat += fatGrp.fat
        elif toBeIncreased== "sugar":
            sCount += 1
            currCho += sugar.cho
            currPro += sugar.pro
            currFat += sugar.fat
        else: 
            print("Please enter correct exchange name")
    elif decision == "done":
        print("")
        print("Your final calorie count is :")
        print("CHO:" + str(currCho*4))
        print("PRO:" + str(currPro*4))
        print("FAT:" + str(currFat*9))
        print("Total caloric count: " + str((currCho*4)+(currPro*4)+(currFat*9)))

        #table generation
        
        quit()
    else:
        print("Please answer correctly")
        

