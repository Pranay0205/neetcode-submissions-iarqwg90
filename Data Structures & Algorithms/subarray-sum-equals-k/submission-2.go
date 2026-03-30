func subarraySum(nums []int, k int) int {
    prefixSum := map[int]int{ 0 : 1 }
    currSum := 0
    count := 0
    for _, n := range nums {
        currSum += n
        diff := currSum - k

        if v, found := prefixSum[diff]; found {
           count += v
        }

        prefixSum[currSum]++
    }

    return count
}