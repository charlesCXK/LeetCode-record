class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def filter(s):
            sp = s.split('@')
            res = ''
            localname, domain = sp[0], sp[1]
            localname = localname.replace('.', '')
            
            if '+' in s:
                plus_index = localname.index('+')
                localname = localname[:plus_index]
            
            res = localname + '@' + domain
            
            return res
        
        ret = set()
        for s in emails:
            ret.add(filter(s))
        return len(ret)