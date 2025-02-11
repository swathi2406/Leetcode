func productExceptSelf(nums []int) []int {
    res :=[]int{}
    leftProduct :=[]int{1}
    rightProduct := []int{}
    ans:=1
    for i:=0;i<len(nums)-1;i++{
        ans *=nums[i]
        leftProduct = append(leftProduct,ans)
    }
    fmt.Println(leftProduct)
    ans = 1
    rightProduct = append(rightProduct,ans)
    for i:=len(nums)-1;i>=0;i--{
        
        if i == 0{
            continue
        }else{
            ans *=nums[i]
        }
        rightProduct = append(rightProduct,ans)
    }
    slices.Reverse(rightProduct)
    for i:=0;i<len(nums);i++{
        res = append(res,leftProduct[i]*rightProduct[i])
    }
    fmt.Println(rightProduct)
    return res
    
}