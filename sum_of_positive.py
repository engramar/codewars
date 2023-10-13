def positive_sum(arr):    
    sum = 0 
    for i in arr:
      if (float(i) > 0):
          sum = sum + float(i)
    print(sum)
    return sum


positive_sum ([1,-4,7,12])