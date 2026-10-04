class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        freq = [[] for _ in range(1+len(nums))]

        for key, value in hash_map.items():
            freq[value].append(key)

        answer = []

        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for num in freq[i]:
                    answer.append(num)
                    if len(answer) == k:
                        return answer
