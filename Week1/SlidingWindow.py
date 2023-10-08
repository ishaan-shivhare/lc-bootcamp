class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = r = 0
        q = collections.deque() # only add indexes here
        output = []

        while (r < len(nums)):

            # popping and comparing step 
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if (l > q[0]): # if element is out of bound of window, pop it
                q.popleft()

            if (r + 1) >= k: #check if window is at least size k 
                output.append(nums[q[0]])
                l += 1

            r += 1
        
        return output

