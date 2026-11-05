class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        for num in nums:
            if not num in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        answer = []

        for key, value in freq.items():
            bucket[value].append(key)


        for i in range(len(nums), -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    answer.append(num)
                    if len(answer) == k:
                        return answer
