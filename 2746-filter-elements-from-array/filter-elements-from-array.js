/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let filteredArray = new Array();
    let j =0;
    for(let i=0;i<arr.length;i++){
        if ( fn(arr[i],i)){
            filteredArray[j] = arr[i];
            j +=1;
        }else{
            continue;
        }
    }
    // console.log(filteredArray);
    return filteredArray;
    
};