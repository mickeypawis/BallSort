import problem
import utils
import ucs
import copy
# #A A C C
# #A A C B
# #D D D B
# #C B D B
# # A     A     C     C
ans11,ans12,ans13,ans14 =input("Enter the first row :").split()
# # A     A     C     B
ans21,ans22,ans23,ans24 = input("Enter the second row :").split()
# # D     D     D     B
ans31,ans32,ans33,ans34 = input("Enter the third row :").split()
# # C     B     D     B
ans41,ans42,ans43,ans44 = input("Enter the fourth row :").split()
# # reverse list for pop
# #แบกไม่กลับ/แนวนอน
tower1 = [ans11,ans21,ans31,ans41]
tower2 = [ans12,ans22,ans32,ans42]
tower3 = [ans13,ans23,ans33,ans43]
tower4 = [ans14,ans24,ans34,ans44]
# #แบบกลับ/แนวตั้ง
# # tower1 = [ans41,ans31,ans21,ans11]
# # tower2 = [ans42,ans32,ans22,ans12]
# # tower3 = [ans43,ans33,ans23,ans13]
# # tower4 = [ans44,ans34,ans24,ans14]
tower5 =["_","_","_","_"]
tower6 =["_","_","_","_"]
# #nested list
all_tower=[]
all_tower.append(tower1)
all_tower.append(tower2)
all_tower.append(tower3)
all_tower.append(tower4)
all_tower.append(tower5)
all_tower.append(tower6)
problem.initials_state=copy.deepcopy(all_tower)


goal_node, n_visits = ucs.uniform_cost_graph_search(problem)
if goal_node is not None:
  print("Solution")
  print("========")
  
  utils.print_solution(goal_node)
  print("========")
  print("Path cost = %d" % goal_node[2])
  print("Number of Visited States = %d" % n_visits)
  
   
  
else:
  print("No solutions found")()