class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        size = len(arr)

        for x in range(size):
            for y in range(x+1,size):
                for z in range(y+1, size):
                    if abs(arr[x] - arr[y]) <= a and abs(arr[y] - arr[z]) <= b and abs(arr[x] - arr[z]) <= c:
                                count += 1

        return count

        