from collections import deque
def create_node(state, parent, path_cost):
    return (state, parent, path_cost)


def print_solution(n):
    r = deque()
    step=0
    while n is not None:
        r.appendleft(n[0])
        n = n[1]
    for s in r:
      print("Step",step)
      for i in range(0,4):
        print(s[0][i],end=" ")
        print(s[1][i],end=" ")
        print(s[2][i],end=" ")
        print(s[3][i],end=" ")
        print(s[4][i],end=" ")
        print(s[5][i],end=" ")
        print("")
      step += 1
      print("")


