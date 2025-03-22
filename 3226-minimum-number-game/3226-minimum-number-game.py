class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        bob = []
        alice = []
        while len(nums) != 0:
            alice.append(min(nums))
            nums.remove(min(nums))
            bob.append(min(nums))
            nums.remove(min(nums))

        while len(alice) != 0 or len(bob) != 0:
            nums.append(min(bob))
            bob.remove(min(bob))
            nums.append(min(alice))
            alice.remove(min(alice))
        return nums   