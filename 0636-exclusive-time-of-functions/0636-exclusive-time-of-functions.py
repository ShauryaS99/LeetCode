class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        #O(N) for time and space
        function_lst = [0] * n
        call_stack = []
        prev_start = 0
        for log in logs:
            function, call_type, ts = log.split(":")
            function = int(function)
            ts = int(ts)
            # 2 types of calls
            if call_type == "start":
                # If start: add to call stack, calculate prev func time elapsed
                if call_stack:
                    last_call = call_stack[-1]
                else:
                    last_call = function
                function_lst[last_call] += ts - prev_start
                call_stack.append(function)
                prev_start = ts
            else:
                # If end: pop from call stack, calculate func time elapsed
                last_call = call_stack.pop()
                function_lst[last_call] += ts - prev_start + 1
                prev_start = ts + 1
        return function_lst