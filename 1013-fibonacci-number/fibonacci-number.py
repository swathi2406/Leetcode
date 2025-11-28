class Solution:
    def fib(self, n: int) -> int:
        first, second = 0,1
        # fib1 = 0
        if n ==0:
            return 0
        elif n ==1:
            return 1
        else:
            fib1 = first + second
            for i in range(2,n):
                first = second
                second = fib1
                fib1 = first+second
        return fib1 
