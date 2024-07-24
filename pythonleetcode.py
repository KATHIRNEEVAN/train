class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                st=''
                for k in s[i:j]:
                    if s[i:j].count(k)==1:
                        st+=k
                    else:
                        break
                l.append(len(st))
        if not l:
            return 0
        else:
            return max(l)
