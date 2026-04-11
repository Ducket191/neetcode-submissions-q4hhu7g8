class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = sum(students)
        while students:
            if not students:
                return 0
            cur = students.pop(0)
            if cur == sandwiches[0]:
                x = sandwiches.pop(0)
                s -= x
            else:
                students.append(cur)
                if s == len(students) or s == 0:
                    break
        
        return len(students)