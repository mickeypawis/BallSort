# from problem as problem

# #A A C C
# #A A C B
# #D D D B
# #C B D B
# # A     A     C     C
# ans11,ans12,ans13,ans14 =input("Enter the first row :").split()
# # A     A     C     B
# ans21,ans22,ans23,ans24 = input("Enter the second row :").split()
# # D     D     D     B
# ans31,ans32,ans33,ans34 = input("Enter the third row :").split()
# # C     B     D     B
# ans41,ans42,ans43,ans44 = input("Enter the fourth row :").split()
# # reverse list for pop
# #แบกไม่กลับ/แนวนอน
# # tower1 = [ans11,ans12,ans13,ans14]
# # tower2 = [ans21,ans22,ans23,ans24]
# # tower3 = [ans31,ans32,ans33,ans34]
# # tower4 = [ans41,ans42,ans43,ans44]
# #แบบกลับ/แนวตั้ง
# tower1 = [ans41,ans31,ans21,ans11]
# tower2 = [ans42,ans32,ans22,ans12]
# tower3 = [ans43,ans33,ans23,ans13]
# tower4 = [ans44,ans34,ans24,ans14]
# tower5 =["_","_","_","_"]
# tower6 =["_","_","_","_"]
# #nested list
# list=[]
# list.append(tower1)
# list.append(tower2)
# list.append(tower3)
# list.append(tower4)
# list.append(tower5)
# list.append(tower6)

list_of_successor=[]
s=[["A","B","C","D"],["A","B","C","D"],["A","B","C","D"],["A","B","C","D"],["_","_","_","_"],["_","_","_","_"]]

# def swap(initial_stack,target_stack):
#   ball

def successors(s):
  for i in (s):#stack
    for j in range(len(i)): # element inside stack
      if s[i][j] != "_":
        ball= s[i][j] #choose ball
    for k in (s):#target stack
      for u in range (4): #หาตัวบนสุด
        if s[k][u] != "_":
          top = u
      if s[k].count["_"] == 0: # check full stack or (not condition 3)
        continue
      if s[i]==s[k]:#same stack or not (condition1)
        continue
      if ball == s[k][top]:
       s[k][top]=ball
       s[i][j]="_"

      list_of_successor.append(s)
successors(s)
print(list_of_successor)
