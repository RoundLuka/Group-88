// type Color = "Red" | 'Blue';

// let myTheme: Color;

// myTheme = 'Red'

// let something;

// something = 7
// something ="wryw"

// arrays in typescript

// type numArr = [string?, number?, string?];

// let grades: numArr = [];

// grades.push("wreyer")
// grades.push(5)
// grades.push("Luka")


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

// enum Axis {
//     x = "North",
//     y,
//     z
// }

// let objectLengthPlane: Axis = Axis

// console.log(objectLengthPlane)

// string enum
// enum Roles {
//     user = "User",
//     staff = "Staff",
//     admin = "Admin"
// }

// let dachi: Roles = Roles.staff;

// console.log(dachi)

// numeric enum
// enum Rank {
//     Corporal,
//     Sergeant, // 1
//     Officer,
//     Lietenaunt,
//     Captain, // 5
//     Major,
//     Colonel,
//     General
// }

// let ryan: Rank = Rank.Sergeant

// let nelson: Rank = Rank.Major

// console.log(ryan)
// console.log(nelson)

// object strict typing

// type alias

type myNum = number
type person = {username: string, influence: number}[]

let academy: {
    students: myNum,
    deparatments: number,
    controllers: person
}

academy = {
    students: 5,
    deparatments: 5,
    controllers: [{username: "Luka", influence: 5}]
}

// type lukaType = "luka" | "luksona" | boolean



// type stringsToNum = (arg1: string, arg2: string) => number

// const addStringLengths: stringsToNum = (word1, word2) => {
//     return word1.length + word2.length
// }

// const multiplyStringLengths: stringsToNum = (word1, word2) => {
//     return word1.length * word2.length
// }

// let result = addStringLengths("dachi", "giorgi")
// console.log(result)

// result = multiplyStringLengths("dachi", "giorgi")
// console.log(result)

// type Family<T> = {
//     parents: [T, T], mate: T, children: T[]
// };


// let myFamily: Family<string> = {
//     parents: ["Tazo", "Tamo"],
//     mate: "Giorgi",
//     children: ["weytwtyw", "wtwetw", "ewqtwetew"]
// }


// let someData: Family<number> = {
//     parents: [5, 1],
//     mate: 5,
//     children: [7, 7, 7]
// }

// type Office<T> = {
//     CEO: T, 
//     employees: T[],
//     Managers: [T, T]
// }

// interface newPerson {
//     username: string,
//     age: number
// }

// const goa: Office<newPerson> = {
//     CEO: {username: "Nika", age: 25},
//     Managers: [{username: "Nika", age: 25}, {username: "Nika", age: 25}],
//     employees: [{username: "Nika", age: 25}]
// }

// console.log(goa)

// function getFilledArray<T>(value: T, n: number): T[] {
//     return Array(n).fill(value);
// }

// console.log(getFilledArray("hi", 6) )

// enum Status {
//     Open = true,
//     Closed = false
// }

// let shopStatus: Status = Status.Open

// console.log(shopStatus)

// type numStringUnion = string | number;

// let something: numStringUnion = 5;
// something = 'qtewtw'


// type something = boolean[] | number[]

// let boolArr: something = [true, false]

// type game<T> = {
//     creator: T,
//     adminList: T[],
//     visits: number
// }

// let strategy: game<number> = {
//     creator: 22,
//     adminList: [5],
//     visits: 52
// }

// function doSomething<T>(param1: T, param2: number) : T[] {
//     let result = []
//     for(let i = 0; i < param2; i++) {
//         result.push(i)
//     }
//     return result
// }

// console.log(doSomething("Luka", 5))

let doSomething = <T>(param1: T, param2: number): T[] => {
    return [param1, param2]
}

