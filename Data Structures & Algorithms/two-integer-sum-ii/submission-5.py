class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        diff_dict = defaultdict(int)

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in diff_dict:
                return [diff_dict[diff], i + 1]
            else:
                diff_dict[n] = i + 1

        return []