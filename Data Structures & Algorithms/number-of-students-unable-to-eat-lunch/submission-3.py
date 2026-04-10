from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = sum(students)
        # Use a counter to track how many times we've cycled without a match
        count = 0
        
        while students:
            # If we have cycled through all remaining students and 
            # nobody wanted the top sandwich, we are stuck.
            if count == len(students):
                break
                
            cur = students.pop(0)
            
            if cur == sandwiches[0]:
                # Student eats: update the sandwich stack and the sum
                x = sandwiches.pop(0)
                s -= x
                count = 0  # Reset the 'stuck' counter because someone ate
            else:
                # Student goes to the back
                students.append(cur)
                count += 1
        
        return len(students)