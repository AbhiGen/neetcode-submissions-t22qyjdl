class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for _ in range(32):
            lastbit=n&1
            res=res<<1 | lastbit
            n=n>>1
        return res