class Solution:
    def calculate(self, s: str) -> int:
        res = prev = 0
        operation = "+"
        i = 0
        while i < len(s):
            while i < len(s) and s[i] == " ":
                i += 1
            curr_digit = ""
            while i < len(s) and s[i].isdigit():
                curr_digit += s[i]
                i += 1
            curr_digit = int(curr_digit)
            
            if operation == "+":
                res += curr_digit
                prev = curr_digit
            elif operation == "-":
                res -= curr_digit
                prev = -curr_digit
            elif operation == "*":
                res -= prev
                res += prev * curr_digit
                prev = prev * curr_digit
            else:
                res -= prev
                res += int(prev / curr_digit)
                prev = int(prev / curr_digit)
            while i < len(s) and s[i] == " ":
                i += 1
            if i < len(s) and not s[i].isdigit():
                operation = s[i]
            i += 1
        return res