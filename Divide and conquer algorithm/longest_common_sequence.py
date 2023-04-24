 #The problem can be divided into three subproblems
#1. They are matching
#2.


def common_subsequence(s1,s2,index1,index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    elif (index1,index2) in recurring_values:
        return recurring_values[(index1,index2)]
    elif s1[index1] == s2[index2]:
        return 1 + common_subsequence(s1,s2,index1+1,index2+1)
    else:
        op1 = common_subsequence(s1,s2,index1+1,index2)
        op2 = common_subsequence(s1,s2,index1,index2+1)

        if (index1,index2) not in recurring_values:
            recurring_values[(index1,index2)] = max(op1,op2)
        return max(op1,op2)





s1 = 'elephant'
s2 = 'erephat'
recurring_values = {}
print(common_subsequence(s1,s2,0,0))
