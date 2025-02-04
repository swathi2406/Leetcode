func longestCommonPrefix(strs []string) string {
    if len(strs) == 0 {
        return ""
    }
    ans := ""
    terminate := false
    for idx := 0; idx < len(strs[0]); idx++ {
        commonChar := ""
        for j := 0; j < len(strs); j++ {
            if idx >= len(strs[j]) {
                terminate = true
                break
            }
            if j == 0 {
                commonChar = string(strs[0][idx])
            }
            if commonChar != string(strs[j][idx]) {
                terminate = true
                break
            }
        }
        if !terminate {
            ans += commonChar
        } else {
            break
        }
    }
    return ans
}
