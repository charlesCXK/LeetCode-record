class Solution:
    def validIPAddress(self, IP: str) -> str:
        def judgeIPV4(s):
            seg = s.split('.')
            if len(seg) != 4:
                return False
            for num in seg:
                if len(num)>1 and num.startswith('0') or len(num) == 0:
                    return False
                
                # It is not a number
                for s in num:
                    if not (ord(s)>=ord('0') and ord(s)<=ord('9')):
                        return False
                
                number = int(num)

                if number<0 or number > 255:
                    return False
            return True
    
        def judgeIPV6(s):
            seg = s.split(':')
            if len(seg) != 8:
                return False
            
            for num in seg:
                if len(num)>4 or len(num)<=0:
                    return False

                for s in num.upper():
                    if not (ord(s)>=ord('0') and ord(s)<=ord('9') or ord(s)>=ord('A') and ord(s)<=ord('F')):
                        return False
            return True
        
        if judgeIPV4(IP):
            return 'IPv4'
        elif judgeIPV6(IP):
            return 'IPv6'
        else:
            return 'Neither'