function makeSentence(parts) {
  let result = "";
  
  for (let i = 0; i < parts.length; i++) {
  
    if (parts[i + 1] === ".") {
      result += parts[i]
      break
    }
    
    if (i === parts.length - 1) {
      result += parts[i]
      break;
    }
    
    if (parts[i + 1] === ",") {
      result += parts[i]
    } else {
      result += parts[i] + " "
    }
  }
  return result + ".";
}