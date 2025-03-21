from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0: 
            return True

        count = 0
        length = len(flowerbed)

        for i in range(length):
            # Check if the current spot is empty and both neighbors (if they exist) are empty
            if flowerbed[i] == 0 and \
               (i == 0 or flowerbed[i - 1] == 0) and \
               (i == length - 1 or flowerbed[i + 1] == 0):
                
                # Place a flower
                flowerbed[i] = 1
                count += 1

                # Skip the next spot since you can't plant adjacent flowers
                i += 1  

            # Early exit if enough flowers are placed
            if count >= n:
                return True

        return count >= n

        