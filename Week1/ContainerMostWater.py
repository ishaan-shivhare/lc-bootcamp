class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height) - 1
    
        maxVol = 0

        while (i < j):
            h1 = height[i]
            h2 = height[j]
            vol = min(h1, h2)*(j-i)
            maxVol = max(maxVol, vol)
            
            if (h1 > h2):
                j = j-1
                continue
            if (h1 < h2):
                i = i+1
                continue
            if (h1 == h2):
                i = i+1
                j = j-1
                continue

                # nxt_h1 = height[i+1]
                # nxt_h2 = height[j-1]
                # if (nxt_h1 > nxt_h2):
                #     i = i+1
                #     continue
                # if (nxt_h1 < nxt_h2):
                #     j = j-1
                #     continue
                # if (nxt_h1 == nxt_h2):
                #     i = i+1
                #     continue
            
        return maxVol

        
        # maxVol = 0
        # for i in range(len(height)):
        #     h1 = height[i]
        #     for j in range(i+1, len(height)):
        #         h2 = height[j]
        #         vol = min(h1, h2)*(j-i)
        #         maxVol = max(maxVol, vol)
        # return maxVol
