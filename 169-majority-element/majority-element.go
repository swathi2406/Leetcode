func majorityElement(nums []int) int {

	var maps = make(map[int]int)
    max := 0
	val := 0
	for _, num := range nums {
		maps[num] = maps[num] + 1
        if max < maps[num]{
            max = maps[num]
            val = num


        }
	}
	return val

}
