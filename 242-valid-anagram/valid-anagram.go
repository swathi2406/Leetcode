func isAnagram(s string, t string) bool {
    res:=false
    res1:=false
    res2:=false
    sCount := make(map[string]int)
    tCount := make(map[string]int)
    for _,v :=range s{
        sCount[string(v)]+=1   
    }
    for _,v :=range t{
        tCount[string(v)]+=1   
    }

    for i,_ :=range sCount{
        if strings.Contains(t,i) && sCount[i] == tCount[i] {
            res = true
        }else{
            return false
        }
    }
    for i,_ :=range tCount{
        if strings.Contains(s,i) && tCount[i] == sCount[i]{
            res1 = true
        }else{
            return false
        }
    }
    if res == res1{
        res2 =  true
    }else{
        res2 =  false
    }
    return res2
}