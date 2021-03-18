
n, pkt_limit, fine = list(map(int,input().split()))

arr1 = sorted(list(map(int,input().split())))
arr2 = sorted(list(map(int,input().split())))

curr_perm = []
curr_fine = 0
for i in range(n):
    curr_perm.append([arr1[i],arr2[~i]])
for i in curr_perm :
    if sum(i) > pkt_limit:
        curr_fine += (sum(i) - pkt_limit)*fine 
print(curr_fine) 

