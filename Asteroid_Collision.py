# https://leetcode.com/problems/asteroid-collision/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = -1
        arr =asteroids
        x = [] 
        y = []
        while i < len(arr) -1 : 
            i+=1
            if arr[i] > 0 : 
                x.append(arr[i])
                # print(x,arr)
            elif arr[i] < 0 :
                if len(x) == 0 :
                    y.append(arr[i])
                    arr.pop(i)
                    i-=1
                else :
                    m = abs(x[-1])
                    n = abs(arr[i])
                    if m> n : 
                        pass
                    elif m < n :
                        x.pop(-1)
                        i-=1
                    else : 
                        x.pop(-1)
                        arr.pop(i)
                        i-=1
            
        return y+x
#             
                        
            
        
        