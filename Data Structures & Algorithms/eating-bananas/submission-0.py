class Solution:
    def verify_speed(self,piles:List[int],h, speed:int):
        total = sum(math.ceil(p/speed) for p in piles)
        return total<=h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        n = len(piles)
        max_speed = max(piles)
        while min_speed<max_speed:
            mid = (max_speed + min_speed)//2
            if self.verify_speed(piles,h,mid):
                max_speed = mid
            else:
                min_speed = mid + 1 
        return min_speed

