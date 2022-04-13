from numpy import log

a0 = float(input("Enter a0 -> "))
b0 = float(input("Enter b0 -> "))
accuracy = int(input("Accuracy 10^? -> "))

def f(x):
    return pow(x,4) - x - 1

sign = f(a0) < 0 # assuming that a0 is lesser than 0

itter = int((log(pow(10, accuracy)) - log(abs(a0 - b0)))/log(0.5))

print("{0:^10} | {1:^25} | {2:^25} | {3:^25} | {4:^25}".format("k", "a_k", "b_k", "x_k", "f(k)"))
print("-------------------------------------------------------------------------\n")

for k in range(itter + 1):
    xk = (a0 + b0)/2
    print("{0:^10} | {1:^25} | {2:^25} | {3:^25} | {4:^25}\n".format(k, a0, b0, xk, f(xk)))

    if sign:
        if f(xk) < 0: a0 = xk
        else: b0 = xk
    else:
        if f(xk) < 0: b0 = xk
        else: a0 = xk
