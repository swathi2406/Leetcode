func addedInteger(nums1 []int, nums2 []int) int {
	// take both the arrays and sort them.
	// Subtract the elements of nums2 by num1 and if all the diff value are same, print it out
	return slices.Min(nums2) -slices.Min(nums1)
 }