# import random
# tries=0
# original=random.randint(0,2)
# while True:
#      tries=tries+1
#      if tries==3:
#           print("you lost")
#           break
#      print(f"try-{tries}") #2=scissor
#      guess=int(input("press 0-paper,1-stone,2-scissor"))#1=stone
#      if original==guess:#0=paper
#           print("draw")
#      elif original==0 and guess==1:
#           print("you lost")
#      elif original==1 and guess==2:
#           print("you lost")   
#      elif original==2 and guess==0:
#           print("you lost")   
#      elif original==0 and guess==2 :
#           print("you won")
#      elif original==1 and guess==0:
#           print("you won")       
#      elif original==2 and guess ==1:
#           print("you won")           
#      print(original)     

#      import random
#      comp=random.randint(1,3)
#      us=int(input("press 1-rock ,2-paper,3-scissor"))
#      if us==1 and comp==3:
#           print("u won")
#      elif us==2 and comp ==1:
#           print("u won")    
#      elif us ==3 and comp==2:
#           print("u won")
#      elif us ==comp:
#           print("its draw")       
#      else:
#           print("comp win")

#      import random
#      comp=random.randint(1,3)
#      us=int(input("press 1-rock ,2-paper,3-scissor"))
#      if (us==1 and comp==3) or (us==2 and comp ==1) or (us ==3 and comp==2 ):
#           print("u won") 
#      elif us ==comp:
#           print("its draw")       
#      else:
#           print("comp win")

import random
comp=random.randint(1,3) 
human_score=0
comp_score=0
while True:
    if human_score==5:
        print("u won the game")
        break
    if comp_score==5:
        print("computer wins")
        break
    us=int(input("press 1-for rock ,2- for paper,3- for scissor")) 
    if us>3 or us<1:
        print("wrong input choosen ")
        continue
    elif (us==1 and comp==3) or (us==2 and comp ==1) or (us ==3 and comp==2 ):
        human_score+=1
        print(f"u won ..ur score{human_score} & {comp_score}")
    elif us==comp:
        print(f"its a draw \n current score-us{human_score} & comp{comp_score }")
    else:
        comp_score+=1
        print(f"comp wins current score-us-{human_score} & {comp_score}")
         
        
        #streamlit
