func isPossibleToSplit(nums []int) bool {
    //  the main array nums, should be have elements whose counts should be atmost 2 . 
    //  the length of nums should be a even number or be divisible by 2 so that it can be easily split in half
    // The sub arrays should have distinct values in them
    numMaps := map[int]int{}
    if len(nums)%2 != 0{
        return false
    }else{
    for _, n :=range nums{
        numMaps[n] +=1
        if numMaps[n] >2{
            return false
        }
    }
    return true
    }
}