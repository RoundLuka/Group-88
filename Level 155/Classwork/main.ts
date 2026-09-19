// type Color = "Red" | 'Blue';

// let myTheme: Color;

// myTheme = 'Red'

// let something;

// something = 7
// something ="wryw"

// arrays in typescript

type numArr = [string?, number?, string?];

let grades: numArr = [];

grades.push("wreyer")
grades.push(5)
grades.push("Luka")


// annoation
type numStr = "luka" | 5

interface person {
    firstname: numStr,
    lastname: string,
    age: number
}

const luka: person = {
    firstname: "luka",
    lastname: "gurgenidze",
    age: 18,
}

function addNumbers(num1: number, num2: number): string {
    return (num1 + num2).toString()
};

const sum = addNumbers(2, 3);
console.log(sum);