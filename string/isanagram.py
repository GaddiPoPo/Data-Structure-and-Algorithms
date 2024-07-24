def isAnagram(s,t):
        counts,countt={},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            counts[s[i]]=1+counts.get(s[i],0)
            countt[t[i]]=1+countt.get(t[i],0)
        return counts==countt
k=isAnagram("anagram", "nagaram")
print(k)

