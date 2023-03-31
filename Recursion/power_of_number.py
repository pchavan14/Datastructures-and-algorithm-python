def power_of_number(number,power):
    assert power>=0 and int(number)==number, "The number should be integer and power should be positive"
    if power == 0:
        return 1
    else:
        return(number * power_of_number(number,power-1))
        
    

print(power_of_number(-2,1))