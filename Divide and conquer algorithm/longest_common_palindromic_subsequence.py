def longest_common_palandromic_string(s,start,end):
    if start > end:
        return 0
    
    elif (start,end) in recurring_values:
        return recurring_values[(start,end)]


    elif start == end:
        return 1
    
    elif s[start] == s[end]:
        return 2 + longest_common_palandromic_string(s,start+1,end-1)
    else:
        op1 = longest_common_palandromic_string(s,start+1,end)
        op2 = longest_common_palandromic_string(s,start,end-1)
      
        if (start,end) not in recurring_values:
            recurring_values[(start,end)] = max(op1,op2)


       
        return max(op1,op2)







recurring_values = {}
s = "abcb"
print(longest_common_palandromic_string(s,0,len(s)-1))