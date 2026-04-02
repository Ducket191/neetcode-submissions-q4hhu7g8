class Solution:

    def encode(self, strs: List[str]) -> str:
        count = []
        for item in strs:
            count.append([item, str(len(item))])
        res = []
        for item in count:
            res.append(item[1])
            res.append("#")
            res.append(item[0])
        return "".join(res)
    
    def decode(self, s: str) -> List[str]:
        res2 = []
        while len(s) > 0:
            delimiter_pos = s.find('#')
            length = int(s[:delimiter_pos])
            chars = s[delimiter_pos+1 : delimiter_pos+1+length]
            res2.append(chars)
            s = s[delimiter_pos+1+length:]
        return res2

