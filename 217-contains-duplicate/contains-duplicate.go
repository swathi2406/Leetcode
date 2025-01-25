func containsDuplicate(nums []int) bool {
    //  we are given an integers of arrays
    //  check for any duplicate values
    //  create a map and store the values along with its frequencies
    //  if any of the frequencies is more than 2 return true
    //  else return false

    numMaps := map[int]int{}
    ch := false
    for i:=0;i<len(nums);i++{
        // fmt.Println(nums[i])
        numMaps[nums[i]]   = numMaps[nums[i]] +1
        // if numMaps[n] >1{
        //     ch = true
        // }else{
        //     ch = false
        // }
    }

    for i,v :=range numMaps{
        fmt.Println(i," ",v)
        
        if v >1{
            return true 
        }
    }
    return ch
}