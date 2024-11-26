class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n  # Result array to store exclusive time for each function
        stack = []  # Stack to track active functions
        prev_time = 0  # Keeps track of the last timestamp

        for log in logs:
            func, f_type, ts = log.split(":")
            func, ts = int(func), int(ts)

            if f_type == "start":
                # Update the current top of the stack's time
                if stack:
                    res[stack[-1]] += ts - prev_time
                stack.append(func)
                prev_time = ts
            else:  # "end" case
                # Pop the current function and update its exclusive time
                res[stack.pop()] += ts - prev_time + 1
                prev_time = ts + 1  # Move to the next timestamp

        return res
