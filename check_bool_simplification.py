#define global variables
alphabet = list("ABCDEFGHIJK")
n_inputs = int(input("Enter number of inputs -> ").strip())
definition = []

def Fg(state):

    state = list(map(int, state.split()))
    a,b,c,d = state

    m0 = (not b) and (not c)
    m1 = (not d) and (not b)
    m2 = (c) and (not d) and (not a)
    m3 = 0
    m4 = 0
    m5 = 0


    return int(m0 or m1 or m2 or m3 or m4 or m5)




print( " ".join(alphabet[:n_inputs]) + "\tF")

for i in range(2**n_inputs):
    state = " ".join(list(bin(i)[2:].zfill(n_inputs)))
    
    print(state, end="")
    F = int(bool(int(input("\t").strip())))

    definition.append([state, F, Fg(state)])


print( " ".join(alphabet[:n_inputs]) + "\tF\tR\tStatus")

for row in definition:
    print("\t".join(list(map(str,row))), end="\t")
    status = not(row[1] ^ row[2])

    if status:
        print(status)
    else:
        print("YOU ARE DOOMED")


