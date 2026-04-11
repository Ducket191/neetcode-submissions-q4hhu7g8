class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        o = sum(students)
        z = len(students) - o
        o1 = sum(sandwiches)
        z1 = len(sandwiches) - o1
        if o < o1:
            cnt = o
            c = 0
            for item in sandwiches:
                if item == 1:
                    if cnt == 0:
                        return len(sandwiches) - c
                    cnt -= 1
                c += 1
        elif z < z1:
            cnt = z
            c = 0         
            for item in sandwiches:
                if item == 0:
                    if cnt == 0:
                        return len(sandwiches) - c
                    cnt -= 1
                c += 1
                
        return 0