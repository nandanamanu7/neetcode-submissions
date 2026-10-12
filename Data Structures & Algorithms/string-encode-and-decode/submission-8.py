from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "#" + s
    
        return encoded_string;

    

    def decode(self, encoded_string: str) -> List[str]:
        res = []
        i = 0

        while (i < len(encoded_string)):
            j = i

            while (encoded_string[j] != "#"):
                j += 1
            
            length = int(encoded_string[i:j])

            res.append(encoded_string[j+1:j+1+length])

            i = j + 1 + length
    
        return res


        