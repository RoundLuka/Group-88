// function sumArray(array) {
  
//   if (array.length <= 1) {
//     return 1
//   }
//   if (array === null) {
//     return 1
//   }
  
//   let smallest = array[0];
//   let biggest = array[1];
//   let total = 0;
  
//   for(let i = 0; i < array.length; i++) {
//     let current = array[i];
//     total += current
//     if (current < smallest ) {
//       smallest = current
//     } 
    
//     if (current > biggest) {
//       biggest = current;
//     };
//   }
//   return total - biggest - smallest;
// }

// console.log(sumArray(undefined))
// console.log(sumArray(null))

// console.log(sumArray([2, 26, 1, 5, 2]))
//          -3  -2  -1

// let word = "Something"
// let reversed = "";

// for(let i = word.length - 1; i >= 0; i--) {
//     reversed += word[i]
// }

// console.log(reversed)

// 21-2

// for (let i = 22; i >= 2; i -= 1) {
//     console.log(i)
// }

let answer = ""
let desiered = "yes master"

while (answer !== desiered) {
    answer = prompt("Enter YOUR ANSWER: ")
}