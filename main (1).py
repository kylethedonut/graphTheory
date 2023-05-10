# input; must be in descending order w/ all degrees > 0
inputSequence = [5,2,2,2,1,1,1,1,1]

# fun starting output
message = "input sequence: " + str(inputSequence)
print(message)

# need to sort the seq after each iteration
# since deg(v) = deg(u) is possible
def sortB(array): 
    n = len(array) 
    for i in range(n):
      for j in range(0, n-i-1):
        if array[j] < array[j+1] : 
          array[j], array[j+1] = array[j+1], array[j]
    print(array)
  
# plucks out largest degree, working
def rHD(array):
  for i in range(array[0]+1):
    array[i] = array[i] - 1
  del array[0]
  inputSequence.append(0)
  sortB(array)

# test if degree sequence is graphical
def gTest(array):
  while array[0] > 0:
    rHD(array)
    # sum of deg is even -- 2m + 1 % 2 = 1
    if sum(array) % 2 == 1:
      print("not graphical")
      break
    elif array[0] == 0:
      print("graphical")
      break

gTest(inputSequence)