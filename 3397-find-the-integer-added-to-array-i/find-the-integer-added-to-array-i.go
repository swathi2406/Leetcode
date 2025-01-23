func addedInteger(nums1 []int, nums2 []int) int {
    // take both the arrays and sort them. 
    // Subtract the elements of nums2 by num1 and if all the diff value are same, print it out
    sort.Ints(nums1)
    sort.Ints(nums2)
    diff := nums2[0] - nums1[0]
    for i :=0;i<len(nums1);i++{
        if nums2[i] - nums1[i] != diff{
            break
            return -1
        }else{
            continue
        }
    }
    return diff
}