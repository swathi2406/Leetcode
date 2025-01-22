func singleNumber(nums []int) int {
 
 maps := make(map[int]int)

 for _,freq :=range nums{
    maps[freq] +=1
 }   

 for index,freq := range maps{
    if freq ==1{
        return index
    }
 }
 return 0
}