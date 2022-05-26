import csv
from operator import add

Cond_attr = []
Dec_attr = []

######## Reading Data  ################
with open("Reduction with decision.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]
for i, d in enumerate(data[0]):
    if d == "Condition Attributes":
        Cond_attr.append(data[1][i])
    elif d == "Decision Attributes":
        Dec_attr.append(data[1][i])
U = data[2:]

print("Input >>> ")
for x in data[1:]:
    print(x)


n = len(U)  # No. of objects
nc = len(Cond_attr)  # No. of condition attributes
nd = len(Dec_attr)  # No. of Decision attributes


# Calculating Dicernibility Matrix
discM = []  # list of sets
for i in range(n - 1):
    # Compare ith row with every other rows
    for j in range(i + 1, n):
        a = U[i]
        b = U[j]

        # Ensure that decisions are different
        if a[-nd:] != b[-nd:]:
            #  find the dissimilar elements in evey pairwise rows
            r = [Cond_attr[x] for x in range(nc) if a[x] != b[x]]
            if r != []:
                discM.append(set(r))
# print(discM)

# To Ensure that elements of "f" will be a subset of disM not vice versa
discM = sorted(discM, key=len)


# Calculate Dicernibility Function
f = []
f.append(discM[0])
for x in range(1, len(discM)):
    flag = False
    for y in range(len(f)):
        # append discM elements to "f" iff all elements of "f" not a subset of disM[x]
        if f[y].issubset(discM[x]):
            flag = False
            break
        else:
            flag = True

    if flag:
        f.append(discM[x])

print("\nDiscernibility Function :-\n", f)
print()


# Simplify
while True:
    f2 = []
    f2.append(f[0])

    for i in range(1, len(f)):
        flag = False
        for j in range(len(f2)):
            inter = f[i].intersection(f2[j])

            if inter:
                # (AuB)n(AuC) = AuBC = "r"
                a = f[i].difference(inter)
                b = f2[j].difference(inter)
                r = set(map(add, a, b))
                r.update(inter)
                f2[j] = r
                flag = False
            else:
                flag = True
        # no intersection between "f[i]" and any element of "f2"
        if flag:
            f2.append(f[i])
    if f2 == f:
        break

    f = f2.copy()
print("Output:\nRED >> ", f)

