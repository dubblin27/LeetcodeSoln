def la(heights):
    n = len(heights)
    x = 0 
    y = n -1 
    arr = []
    while x < n and y > -1 :
        if arr[x] > arr[y] : 
            arr.append(arr[y]*(abs(y-x)+1))
            y -= 1
        elif arr[x] < arr[y] : 
            arr.append(arr[x]*(abs(y-x)+1))
            x+=1
        else : 
            arr.append(arr[x]*(abs(y-x)+1))
            x+=1
        print(arr)
la([2,1,5,6,2,3])
                