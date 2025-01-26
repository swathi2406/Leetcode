func absolute(i int)int{
    if i<0{
        i = -i
    }
    return i
}

func findClosestNumber(nums []int) int {
    min := nums[0]
    for i:=0;i<len(nums);i++{
        if absolute(min) > absolute(nums[i]){
            min = nums[i]
        }
    }
    fmt.Println(min)
    if min <0 && slices.Contains(nums,absolute(min)){
        return absolute(min)
    }else{
        return min
    }
    return min
}