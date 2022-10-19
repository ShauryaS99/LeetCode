class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lst = []
        for i in range(1, n + 1):
            lst.append(str(i))
        lst.sort()
        return lst
        