# 15 3Sum
import timeit

class Solution:

    def threeSum_prev(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        previous = None
        for i, a in enumerate(nums):
            if previous == a:
                continue
            previous = a
            l = i+1
            r = len(nums) - 1

            l_prev_val = None
            r_prev_val = None
            while (l < r):
                #print (f"l: {l}, l_prev_val: {l_prev_val} , r : {r} , r_prev_val: {r_prev_val}")
                if l_prev_val == nums[l]:
                    l_prev_val = nums[l] 
                    l +=1
                    continue
                if r_prev_val == nums[r]:
                    r_prev_val = nums[r]
                    r -=1
                    continue
    
                threesum = a+nums[l] + nums[r]
                #print(f"sum: {twosum}")
                if threesum == 0:
                    result.append([a, nums[l] , nums[r]])
                    l_prev_val = nums[l] 
                    r_prev_val = nums[r]
                    r -= 1
                    l += 1
                elif threesum > 0:
                    r_prev_val = nums[r]
                    r -= 1
                elif threesum < 0:
                    l_prev_val = nums[l]
                    l += 1

        return result

    def threeSum_idx(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        #print(nums)
        for i, a in enumerate(nums):
            if i>0 and nums[i-1] == nums[i]:
                continue

            l = i+1
            r = len(nums) - 1
            while (l < r):
                #print(f"a:{a} l:{l} r:{r}")
                if l > i+1 and nums[l-1] == nums[l]:
                    l +=1
                    continue
                if r < len(nums)-1 and nums[r+1] == nums[r]:
                    r -=1
                    continue
                threesum = a+nums[l] + nums[r]
                #print(f"sum: {threesum}")
                if threesum == 0:
                    result.append([a,nums[l] , nums[r]])
                    r -= 1
                    l += 1
                elif threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1

        return result

    def twoSum_idx(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        l = 0
        r = len(nums) - 1
        #print(nums)
        while (l < r):
            if l > 0 and nums[l-1] == nums[l]:
                l +=1
                continue
            if r < len(nums)-1 and nums[r+1] == nums[r]:
                r -=1
                continue
            twosum = nums[l] + nums[r]
        #    print(f"sum: {twosum}")
            if twosum == 0:
                result.append([nums[l] , nums[r]])
                r -= 1
                l += 1
            elif twosum > 0:
                r -= 1
            elif twosum < 0:
                l += 1
        return result

    def twoSum_prev(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        l_prev_val = None
        r_prev_val = None
        l = 0
        r = len(nums) - 1
        #print(nums)
        while (l < r):
            #print (f"l: {l}, l_prev_val: {l_prev_val} , r : {r} , r_prev_val: {r_prev_val}")
            if l_prev_val == nums[l]:
                l_prev_val = nums[l] 
                l +=1
                continue
            if r_prev_val == nums[r]:
                r_prev_val = nums[r]
                r -=1
                continue

            twosum = nums[l] + nums[r]
            #print(f"sum: {twosum}")
            if twosum == 0:
                result.append([nums[l] , nums[r]])
                l_prev_val = nums[l] 
                r_prev_val = nums[r]
                r -= 1
                l += 1
            elif twosum > 0:
                r_prev_val = nums[r]
                r -= 1
            elif twosum < 0:
                l_prev_val = nums[l]
                l += 1

        return result

    def nSum_rec(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        self.nums = nums
        print(self.nums)
        self.targetsum = 0
        self.nsum = 3
        self.result = []
        locallist = []
        #self.previous = None
        self.rec_sum(locallist,0,self.targetsum,self.nsum, None)
        return self.result
    
    def rec_sum(self, locallist,lidx,targetsum,nsum, previous):
 
        remain_targetsum = targetsum
        l = lidx
        r = len(self.nums)-1
        print(f"-:   {remain_targetsum}; {locallist} {self.nums[l:]}, {nsum}, [{l} {r}]")
        if nsum == 2:
            l_prev_val = None
            r_prev_val = None
            #print(f"--:  {remain_targetsum}; {locallist} {self.nums[l:]}, {nsum}")
            while (l < r):
                if l_prev_val == self.nums[l]:
                    l_prev_val = self.nums[l] 
                    l +=1
                    continue
                if r_prev_val == self.nums[r]:
                    r_prev_val = self.nums[r]
                    r -=1
                    continue
    
                twosum = self.nums[l] + self.nums[r]
                if twosum == remain_targetsum:
                    print(f"---> {remain_targetsum}; {locallist},{self.nums[l]}, {self.nums[r]}")
                    
                    tmp = []
                    tmp= locallist.copy()
                    tmp.append(self.nums[l])
                    tmp.append(self.nums[r])
                    self.result.append(tmp)

                    l_prev_val = self.nums[l] 
                    r_prev_val = self.nums[r]
                    r -= 1
                    l += 1
                elif twosum > remain_targetsum:
                    r_prev_val = self.nums[r]
                    r -= 1
                elif twosum < remain_targetsum:
                    l_prev_val = self.nums[l]
                    l += 1
            return
            
        elif lidx <= (len(self.nums) - nsum):
            remain_targetsum = remain_targetsum - self.nums[lidx]
            print("first rec call")
            if previous != self.nums[lidx]:
                previous = self.nums[lidx]
                self.rec_sum(locallist+[self.nums[lidx]],lidx+1,remain_targetsum,nsum-1, previous)

        if lidx <= (len(self.nums) - nsum): #and self.nums[lidx+1] != self.nums[lidx]:
            print(f"second rec call")
            self.rec_sum(locallist,lidx+1,self.targetsum,nsum, previous)

def main():
    #nums = [-1, 0, 1, 2, -1, -4]  # Output: [[-1,-1,2],[-1,0,1]]
    #nums = [-1,0,1,2,-1,-4]
    nums= [-1,0,4,2,-4,2,-2,-4] 
    #nums = [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10] #output  [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]
    #nums=[0,0,0]
    #nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    #4sum
    #nums = [-1,1,2,-2,0,4]
    #nums = [1,2,3,4,5,6,1,2]  #targetsum = 15

    sol = Solution()

    t1 = timeit.default_timer()
    result1 = sol.threeSum_prev(nums)
    t2 = timeit.default_timer()
    #result2 = sol.threeSum_idx(nums)
    #t3 = timeit.default_timer()
    result3 = sol.nSum_rec(nums)
    t4 = timeit.default_timer()

    print("******")    
    print(sorted(result1))
    print(t2 - t1)
    print("******")
    #print(result2)
    #print(t3 - t2)

    print(sorted(result3))
    print(t4 - t2)

    #assert(result1 == result3)

if __name__ == "__main__":
    main()
