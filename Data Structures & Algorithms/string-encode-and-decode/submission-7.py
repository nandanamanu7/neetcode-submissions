from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s

        return encoded_string


    def decode(self, encoded_string: str) -> List[str]:
        decoded_strs = []
        p1 = 0

        while p1 < len(encoded_string):
            j = p1

            while encoded_string[j] != "#":
                j += 1

            length = int(encoded_string[p1:j])
            start = j + 1
            end = start + length

            decoded_strs.append(encoded_string[start:end])
            p1 = end

        return decoded_strs