"use strict";
// type Color = "Red" | 'Blue';
let grades = [];
grades.push("wreyer");
grades.push(5);
grades.push("Luka");
// annoation
// type numStr = "luka" | 5
// interface person {
//     firstname: numStr,
//     lastname: string,
//     age: number
// }
// const luka: person = {
//     firstname: "luka",
//     lastname: "gurgenidze",
//     age: 18,
// }
// function addNumbers(num1: number, num2: number): string {
//     return (num1 + num2).toString()
// };
// const sum = addNumbers(2, 3);
// console.log(sum);
// function doSomething(num1?: number): void {
//     if (num1) {
//         console.log(num1)
//     }
//     console.log("No number")
// } 
// doSomething()
// type numStr = string | number | boolean;
// let username: numStr = "Luka";
// username = 5
// Tuple ეს არის მასივი რომელშიც თითოეულ ელემენტის ტიპს ვაკონკრეტებთ
// typescript-ში tuple-ს აქვს შეზღუდული რაოდენობის ელემენტები
// const tuple: [number, number, number, string] = [2, 5, 1, 'wetwe'];
// // ჩვეულებრივ typescript-ის მასივში
// const numArr: any[] = [1, 2, 3];
var Axis;
(function (Axis) {
    Axis["x"] = "North";
    Axis[Axis["y"] = void 0] = "y";
    Axis[Axis["z"] = void 0] = "z";
})(Axis || (Axis = {}));
let objectLengthPlane = Axis;
console.log(objectLengthPlane);
