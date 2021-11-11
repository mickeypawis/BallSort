import copy

initials_state = []
def is_goal(s):
  for e in s:
    for i in range(3):
      if e[i] != e[i+1]:
        return False
  return True



# def swap(initial_stack,target_stack):
#   ball
def findingtop(s):
    for q in range (4):
        if s[q] == "_":
            continue
        else:
            return s[q]
        break
    return ("_")
    
def successors(s):
  list_of_successor=[]
  temp=0
  index_changingstack = -1
  for i in (s):#stack
    index_changingstack += 1
    

    tmp_stack=copy.deepcopy(i)
  
    if i==["_","_","_","_"]:
        continue
    ball= findingtop(i)#choose ball
    index_target =-1

    for k in (s):#target stack
        index_target +=1
        top=0
            
        temp_s=copy.deepcopy(s)
        tmp_targetstack=copy.deepcopy(k)
        if tmp_targetstack.count("_") == 0: # check full stack or (not condition 3)
            continue
        if index_changingstack==index_target:#same stack or not (condition1)
            continue
        for u in range (4): #หาตัวบนสุด ก่อนหน้า = '_' หรือ 'A'ตัวแรก และ มันไม่ใช่ = '_'
            if k[u] == "_":#ถ้่าใช่ _ ไปต่อ
                top=u #ถ้่าเต็มtop =4 ถ้าเต็มไม่เข้าconditionสุดท้าย
            
        if findingtop(k).isalpha():        
          if ball != findingtop(k): # Av
              continue
        else:
          if ball == findingtop(k): # Av
              continue
            
            
        if k[top]=="_":
            tmp_stack[i.index(ball)]=tmp_targetstack[top]#เปลี่ยนตัวใน chagingstack
            tmp_targetstack[top] = ball#เปลี่ยนตัวใน targetstack
            temp_s[index_changingstack]=tmp_stack
            temp_s[index_target]=tmp_targetstack
            list_of_successor.append(temp_s)
            continue
  return(list_of_successor)  
    
        