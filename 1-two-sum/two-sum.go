func twoSum(nums []int, target int) []int {
    arr := []int{}
    for i,n := range nums{
        for j,k := range nums{
                if i !=j && n +k == target {
                    arr = append(arr,i,j)
                    break
                }
            }
        }
    return arr[0:2]
}