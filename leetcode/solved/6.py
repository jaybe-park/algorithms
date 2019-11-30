class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        
        rows = [[] for __ in range(numRows)]

        inx, is_increase = 0, True

        for c in list(s):
            rows[inx].append(c)
            inx, is_increase = self.get_next_inx(inx, numRows, is_increase)

        result = ''
        for sub_s in rows:
            result += ''.join(sub_s)
        
        return result

    def get_next_inx(self, inx, n, is_increase):
        if is_increase:
            inx += 1
            if inx == n - 1:
                is_increase = False
        else:
            inx -= 1
            if inx == 0:
                is_increase = True
        return inx, is_increase