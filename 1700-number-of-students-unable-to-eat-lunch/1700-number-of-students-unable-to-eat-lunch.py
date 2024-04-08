class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while len(sandwiches) > 0:
            # Check if no more preferred sandwiches
            if sum(students) == len(students) and sandwiches[0] == 0:
                return len(students)
            if sum(students) == 0 and sandwiches[0] == 1:
                return len(students)
            
            # There are still students that can eat preferred sandwiches
            curr_student = students.pop(0)
            # If student likes top sandwich
            if curr_student == sandwiches[0]:
                sandwiches.pop(0)
            # Else student doesn't like top sandwich
            else:
                students.append(curr_student)
 
        return 0
            

    
    
# Students: [1,1,1]
# Sandwich: [0,1,1]

# to check if impossible:
# if sum(students) == len(studnets) and sandwich[0] == 0
# or 
# if sum(students) == 0 and sandwich[0] == 1