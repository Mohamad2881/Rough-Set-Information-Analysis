# REDUCTION WITH CSV

import numpy as np
import csv


Cond_attr = []
Dec_attr = []

################ Reading Data ################
with open("Missing value.csv") as f:
    reader = csv.reader(f)
    data = [r for r in reader]
for i, d in enumerate(data[0]):
    if d == "Condition Attributes":
        Cond_attr.append(data[1][i])
    elif d == "Decision Attributes":
        Dec_attr.append(data[1][i])

# print(Dec_attr)
# print(Cond_attr)

U = np.array(data[1:])  # Exclude first row (Decision Attr,"condition Attr")
nc = len(Cond_attr)  # No. of condition attributes
nd = len(Dec_attr)  # No. of Decision attributes
rows, cols = U.shape

################ Convert Data into Binary ################
Encoded = []
for col in range(1, cols - nd):  # Exclude first col (P1,P2,...P24)
    distinct_attr = list(set(U[1:, col]))  # can't index a set
    # print(len(distinct_attr))

    res = np.array([[U[:, col][0] + '(' + x + ')' for x in distinct_attr]])  # HEADER ROW

    for ele in U[1:, col]:
        a = np.eye(len(distinct_attr), dtype='int32')[distinct_attr.index(ele)]
        res = np.vstack([res, a])
    Encoded.append(res)

Encoded_Data = np.array(Encoded[0])
for i in Encoded[1:]:
    Encoded_Data = np.hstack([Encoded_Data, i])

Encoded_Data = np.hstack([Encoded_Data, U[:, -nd].reshape(rows, -1)])
# print(Encoded_Data)


################# Split into Complete Table and Incomplete Table ################
idx = Encoded_Data[:, -nd] != '?'
complete_table = Encoded_Data[idx]
incomplete_table = Encoded_Data[~idx]

# Add index col.
complete_table = np.hstack([U[idx, 0].reshape(len(idx[idx]), -1), complete_table])
incomplete_table = np.hstack([U[~idx, 0].reshape(len(idx[~idx]), -1), incomplete_table])


# print(complete_table)
# print(incomplete_table)


################# Find most common decision values ################
decision_count = {}
for des in complete_table[1:, -nd]:
    decision_count[des] = decision_count.get(des, 0) + 1
# print(decision_count)


################# Calculate distance between complete data and incomplete data ################
for i in incomplete_table:
    distances = []
    for j in complete_table[1:]:
        # i and j are 1D array
        # print(i[:-nd])
        # print(j[:-nd])
        Euc_dist = np.linalg.norm(i[1:-nd].astype('int32') - j[1:-nd].astype('int32'))
        distances.append(Euc_dist)
    # print(distances)

    min_distances = [idx for idx, v in enumerate(distances) if v == min(distances)]  # Indexes of min values
    # print(min_distances)
    decisions = complete_table[1:, -nd][min_distances]

    # Check if all decisions are the same
    if np.all(decisions == decisions[0]):
        i[-nd] = decisions[0]  # Update decision

    # If there are different values, choose the most common decision
    else:
        common = -1
        for des in decisions:
            if decision_count[des] > common:
                common = decision_count[des]
                i[-nd] = des
            # print(des)
incomplete_table=np.vstack([complete_table[0,:],incomplete_table])
print(incomplete_table)
