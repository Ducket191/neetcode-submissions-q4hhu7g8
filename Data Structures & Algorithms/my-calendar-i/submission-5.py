class MyCalendar:
    
    def __init__(self):
        self.data = []
        self.size = 0

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.data:
            self.data.append([startTime, endTime])
            self.size += 1
            return True

        def binary(s, e):
            if s > e:
                self.data.insert(s, [startTime, endTime])
                self.size += 1
                return True
            
            m = (s+e) // 2
            if startTime >= self.data[m][1]:
                return binary(m+1, e)
            elif endTime <= self.data[m][0]:
                return binary(s, m-1)
            else:
                return False

        return binary(0, self.size - 1)
# param_1 = obj.book(startTime,endTime)