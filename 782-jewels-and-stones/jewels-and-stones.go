func numJewelsInStones(jewels string, stones string) int {
    // var m map[string]int
    m := make(map[string]int)
    for _,v :=range stones{
        if strings.Contains(jewels,string(v)){
        m[string(v)] += 1
        }
    }
    count :=0
    for _,v := range m{
       count +=v
    }
    return count
}