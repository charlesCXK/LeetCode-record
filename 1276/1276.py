class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo, small = 0, cheeseSlices
        delta = tomatoSlices-cheeseSlices*2
        if delta<0 or delta%2==1 or tomatoSlices>cheeseSlices*4:
            return []
        else:
            return [delta//2, cheeseSlices-delta//2]