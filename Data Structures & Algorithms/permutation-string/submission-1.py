class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
    
        freq = {}
        window = {}

        for s in s1:
            freq[s] = freq.get(s, 0) + 1

        lo = 0

        for hi in range(len(s2)):
            
            # Adding the newest char 
            window[s2[hi]] = window.get(s2[hi], 0) + 1

            # Window gets longer than len(s1)
            if hi - lo + 1 > len(s1):
                window[s2[lo]] -= 1

                if window[s2[lo]] == 0:
                    del window[s2[lo]]

                lo += 1

            # If at some point in sliding window
            if window == freq:
                return True 
        
        return False
        