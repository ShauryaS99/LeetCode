class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        prev = res = 0
        operation = "+"
        
        while i < len(s):
            # Skip spaces
            if s[i] == " ":
                i += 1
                continue
            
            curr_num = ""
            # Read the entire number, skipping spaces if necessary
            while i < len(s) and s[i].isdigit():
                curr_num += s[i]
                i += 1
            
            if curr_num:
                curr_num = int(curr_num)
                
                # Perform the operation
                if operation == "+":
                    res += curr_num
                    prev = curr_num  # Update prev to current number
                elif operation == "-":
                    res -= curr_num
                    prev = -curr_num  # Update prev as negative for subtraction
                elif operation == "*":
                    res -= prev  # Remove prev from result
                    res += prev * curr_num  # Add updated value
                    prev = prev * curr_num  # Update prev
                elif operation == "/":
                    res -= prev  # Remove prev from result
                    res += int(prev / curr_num)  # Add updated value (integer division)
                    prev = int(prev / curr_num)  # Update prev
            
            # Update the operation (make sure to skip spaces again)
            if i < len(s) and s[i] != " ":
                operation = s[i]
            i += 1

        return res
