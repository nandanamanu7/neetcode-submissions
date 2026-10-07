class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m_s = {}
        m_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            m_s[s[i]] = m_s.get(s[i], 0) + 1
            m_t[t[i]] = m_t.get(t[i], 0) + 1
        
        return m_s == m_t


        
            

            
        