def square_digits(num):
    output=''    
    for digit in str(num):   
      squared = int(digit) ** 2      
      output += str(squared)   
    return int(output)

square_digits(0)