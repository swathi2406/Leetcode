func isSubsequence(s string, t string) bool {
    S :=len(s)
    T :=len(t)
    R :=0
    j :=0
    for i:=0;i<S;i++{
        for j<T{
            if s[i]==t[j]{
                R++
                j++
                break
            }else{
                j++
            }
        }
    }
    if R == S{
        return true
    }else{
        return false
    }

}