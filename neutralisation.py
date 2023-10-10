def neutralise(s1, s2):           
    result = list()
    cnt = 0
    for char_val in s1:
        if s2[cnt] == char_val:            
            if char_val == "+":
                result[cnt:1] = "+"
            else:
                result[cnt:1] = "-"
        else:
            result[cnt:1] = "0"    
        cnt += 1 

    print (''.join(result))
    return
    
neutralise("--++--","++--++")