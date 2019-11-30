class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list(map(str, range(1, n + 1)))
        
        for inx in range(2, n, 3):
            result[inx] = 'Fizz'
            
        for inx in range(4, n, 5):
            try:
                int(result[inx])
                result[inx] = 'Buzz'
            except:
                result[inx] += 'Buzz'
                
        return result