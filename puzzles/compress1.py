## Example

data1 = [1,2,3,5,10,11] #out = ["1->3", "5", "10->11"]
data2 = [1,3,4,8,9] #out = ["1", "3->4", "8->9"]

out = []
temp = []

data = data2

for i,j in enumerate(data):

    #print("i = " + str(i) + " j = " + str(j))
    print("temp = " + str(temp))

    if i == 0 or (i != 0 and len(temp) == 0):
        print("Initial case, first = " + str(j))
        temp.append(j)
        continue

    if j == data[i-1] + 1:
        #print("Iterative case, j = " + str(j) + " Len(temp) = " + str(len(temp)))
        temp.append(j)
        #print("Iterative case, j = " + str(j) + " Len(temp) = " + str(len(temp)))
        if i == len(data) -1:
            out.append( temp )
        continue
    else:
        if len(temp) == 0:
            out.append( [data[i-1]] )
            continue
        else:
            out.append( temp )
        temp = [j]
        continue

    #first = j
    
print("")
print(out)
