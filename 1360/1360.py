class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 > date2:
            date1, date2 = date2, date1
        # print(date1, date2)
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def runyear(n):
            if (n%4==0 and n%100!=0) or n%400==0:
                return True
            return False
        
        year1, month1, day1 = date1.split('-')
        year2, month2, day2 = date2.split('-')
        
        year1, month1, day1, year2, month2, day2 = int(year1), int(month1), int(day1), int(year2), int(month2), int(day2)
        
        ret = 0
        
        # 处理中间的年份
        for y in range(year1+1, year2):
            ret += 365
            if runyear(y):
                ret += 1
        
        if year1 == year2:
            this_month = months.copy()
            if runyear(year1):
                this_month[2] += 1
            if month1 == month2:
                ret += (day2-day1)
            else:
                for m in range(month1+1, month2):
                    ret += this_month[m]
                ret += (this_month[month1]-day1)
                ret += day2
        else:
            ret += self.daysBetweenDates(date1, str(year1)+'-'+'12-31')
            ret += self.daysBetweenDates(str(year2)+'-'+'01-00', date2)
        return ret
                