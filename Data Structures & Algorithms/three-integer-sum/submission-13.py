class Solution:
   def threeSum(self, nums: List[int]) -> List[List[int]]:
       comp_map = defaultdict(int)
       result = []
       seen_triplets = set()  # To avoid duplicates
       
       # Build frequency map
       for num in nums:
           comp_map[num] += 1
       
       for i in range(len(nums)):
           for j in range(i + 1, len(nums)):
               complement = -1 * (nums[i] + nums[j])
               
               # Check if complement exists
               if complement in comp_map:
                   # Count how many times we need each number
                   needed = defaultdict(int)
                   needed[nums[i]] += 1
                   needed[nums[j]] += 1
                   needed[complement] += 1
                   
                   # Check if we have enough of each number
                   valid = True
                   for num, count in needed.items():
                       if comp_map[num] < count:
                           valid = False
                           break
                   
                   if valid:
                       # Create sorted triplet to avoid duplicates
                       triplet = tuple(sorted([nums[i], nums[j], complement]))
                       if triplet not in seen_triplets:
                           seen_triplets.add(triplet)
                           result.append(list(triplet))
       
       return result