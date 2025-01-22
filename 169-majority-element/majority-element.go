func majorityElement(nums []int) int {

	var maps = make(map[int]int)

	for _, num := range nums {
		maps[num] = maps[num] + 1
	}

	max := 0
	val := 0
	for index, freq := range maps {
		if max < freq {
			max = freq
			val = index
		}
	}
	return val

}
