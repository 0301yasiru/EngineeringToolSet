from numpy import log

n = int(input("Enter number of variables -> ").strip())


def equation(V):
    a = V[0]
    b = V[1]
    c = V[2]
    d = V[3]
    e = V[4]

    result = ((not a) and (not b) and c) or ((not b) and (not c) and e) or (b and c and d) or ((not c) and d and (not e))
    return result


for i in range (n):
    strr = list(bin(i)[2:].zfill(int(log(n)/log(2))))
    r =  list(map(bool, map(int, strr)))
    result = equation(r)

    if result:
        temp = " <--->"
    else:
        temp = "     "

    string = (" | ".join(strr)) + "\t|  " + str(result)  + temp + "[" + str(i).zfill(2) + "]"
    print(string)
