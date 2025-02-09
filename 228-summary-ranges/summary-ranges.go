func summaryRanges(nums []int) []string {
    res := []string{}
    rangeres :=[]int{}
    // res_string := ""
    for i:=0;i<len(nums);i++{
        // i  =4 len(nums) = 6
        if i == len(nums)-1{ //5
            rangeres = append(rangeres,nums[i])
            rangenew := slices.Clone(rangeres)
            if len(rangenew) == 1{
                res_string :=strconv.Itoa(rangenew[0])
                res = append(res, res_string)
            fmt.Println(res_string)
            }else{
                res_string :=strconv.Itoa(rangenew[0])+"->"+strconv.Itoa(rangenew[len(rangenew)-1])
                res = append(res, res_string)
            fmt.Println(res_string)
            }
            
        }else if nums[i+1] == nums[i]+1{ //nums[i+1] = 5, nums[i] = 4
            rangeres = append(rangeres,nums[i]) //[4]
        }else{
            rangeres = append(rangeres,nums[i]) //[]
            rangenew := slices.Clone(rangeres) //rangenew = [0,1,2]
            if len(rangenew) == 1{
                res_string :=strconv.Itoa(rangenew[0])
                res = append(res, res_string)
            fmt.Println(res_string)
            }else{
                res_string :=strconv.Itoa(rangenew[0])+"->"+strconv.Itoa(rangenew[len(rangenew)-1])
                res = append(res, res_string)
            fmt.Println(res_string)
            }
            rangeres = slices.Delete(rangeres,0,len(rangeres))// []

        }
        // j++
    }
    return res
}