func canConstruct(ransomNote string, magazine string) bool {
    alphaCount:= make(map[string]int)
    alphaMagCount:= make(map[string]int)
    res := false
    for _,v :=range ransomNote{
        // fmt.Println(string(v))
        alphaCount[string(v)] +=1
        if strings.Contains(magazine,string(v)){
            alphaMagCount[string(v)] =strings.Count(magazine,string(v))
        }else{
            return false
        }
    }
    for i,_ :=range alphaCount{
        if alphaMagCount[i] >=alphaCount[i]{
            res = true
        }else{
            return false
        }
    }
    fmt.Println(alphaCount)
    fmt.Println(alphaMagCount)
    return res
}