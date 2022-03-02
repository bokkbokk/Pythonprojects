import random
kg = True 
person = ["Dad","mom","sister","brother","aunt","uncle","grandma","grandpa"]
insultw1 = ["smelly ","stinky ","sucky ","stupid ","ugly ","dumb ","arrogant ","bossy ","boring ","fussy ","grumpy ","moody ","toasty "]
insultst = ["You are a ","ur a ","you suck ","I hate you becuase ur a ","Ew, a ","well well well if it isnt the ","woah, look at the ","AAAA ITS A "]
insultw2 = ["peasant","idiot","coward","baby sniffer","scallywag","leg licker ","milk before cereal eater ","uncooked spagetti eater","frozen pasta gulper","knee taster","fool","dummy","always cold idiot","grandpa stealer"]
while kg == True:
  awnser = input("Are you ready? (y/n)")
  if awnser == "n":
    print("ok bye")
  else:
    print(random.choice(insultst) + random.choice(insultw1) + random.choice(insultw2)) 
    print("There ya go!")
    kga = input("more? (y/n)")
    if kga == "n":
        kg = False
    
    
