func mergeAlternately(word1 string, word2 string) string {
   str :=""
   var i,j int
   if len(word1) <len(word2){
    for i,j =0,0;i<len(word1);i,j =i+1,j+1 {
        str += string(word1[i]) + string(word2[j])
    }   
    str = str + word2[j:]
   }else{
    for i,j=0,0;i<len(word2);i,j =i+1,j+1 {
        str += string(word1[i]) + string(word2[j])
    }  
    str = str + word1[i:]
   }
    return str
}