function remove (integer_list, values_list){
  let result = [];
  for(let i = 0; i < values_list.length; i++) {
    
    let targetValue = values_list[i]
    
    for(let j = 0; j < integer_list.length; j++) {
      
      let toBeChecked = integer_list[j]
      
      if(targetValue != toBeChecked) {
        result.push(toBeChecked)
      }
      
    }
    return result;
  }
}

console.log(remove([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]))

Bol

function password(str) {
  
  if (str.length < 8) {
    return false;
  }
  
  let digits = "0123456789"
  let hasDigit = false;
  for(let i = 0; i < digits.length; i++) {
    if(str.includes(digits[i])) {
        hasDigit = true
    }
  }
  
  return !(str === str.toUpperCase() ) && !(str === str.toLowerCase()) && hasDigit
}