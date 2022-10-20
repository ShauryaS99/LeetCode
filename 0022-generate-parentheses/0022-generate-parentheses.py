class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def combo(num_open, num_closed, curr_combo):
            if num_open == 0 and num_closed == 0:
                res.append(curr_combo)
                return
            elif num_open == 0:
                curr_combo += ')'
                combo(num_open, num_closed - 1, curr_combo)
            elif num_open == num_closed:
                curr_combo += '('
                combo(num_open - 1, num_closed, curr_combo)
            else:
                option_1 = curr_combo + '('
                combo(num_open - 1, num_closed, option_1)
                option_2 = curr_combo + ')'
                combo(num_open, num_closed - 1, option_2)

        combo(n, n, '')
        return res