
// global ცვლადი ხელმისაწვდომია ყველგან კოდში
// local ცვლადი ხელისმაწვოდმია მხოლოდ ადგილობრივ კოდის ბლოკში და მის ქვემოთ

// let, const, var 

// for (let i = 0; i < 5; i++) {
//     var user = "luka"
// }

// Hoisting - javascript თვისება რომლის მიხედვითაც პირველ რიგში ხდება ფუნქციების შექმნა,
// შემდეგ var ცლვადების დეკლარაცია (და არა ინციალიზება) ხოლო ამის შემდეგ სხვა ყველაფერი ეშვებას ზევიდან ქვევით თანმიმდევრობით


// console.log(user)

// function OuterScope() {
//     let username = "LUKA";

//     function InnerScope() {
//         for(let i = 0; i < 10; i++) {
//             username = username.toLowerCase()
//         }
//     }
//     InnerScope()
//     console.log(username)
// }

// closure

// function makeCounter() {
//     let count = 0;

//     return function() {
//         return count++;
//     };
// }

// let counter = makeCounter();

// alert( counter() ); // 0
// alert( counter() ); // 1
// alert( counter() ); // 2

// greet()

// function greet() {
//     console.log("Hello World")
// }

// declaration 
// initlization

// while (password !== "luka1234") {
//     var password = prompt("Enter a password")
// }

// 1ms = 1/1000s

// Timers function

// let welcomeHim = false;

// const greetTimer = setTimeout(greet, 2000, "Luka")

// function greet(username) {
//     if (!welcomeHim) {
//         console.log("Cancelled")
//         clearTimeout(greetTimer)
//     }

//     console.log(`Hello ${username}`)
// }

// timeout ფუნქცია callback-ს გამოიძახებს გარკვეული დროის შემდეგ

// let count = 0;

// function counter() {
//     count++;
//     console.log(count)

//     if(count >= 15) {
//         clearInterval(counterInterval)
//     }
// }

// setInterval ფუნქცია callback ფუნქციას გამოიძახებს ყოველი გარკვეული დროის ინტერვალით 

// const counterInterval = setInterval(counter, 200)

// let btn = document.querySelector("button")

// function wrapper() {
//     setTimeout(welcome, 2000)
// }

// function welcome() {
//     alert("You clicked on button")
// }

// btn.onclick = wrapper

const box = document.getElementById("child");

let positionX = 0;
let positionY = 0;
let direction = "right"


function Animate() {

    if(direction === "right") {
        positionX++;

        if(positionX >= 150) {
            direction = 'bottom'
        }
    }
    
    if(direction === 'bottom') {
        positionY++;

        if(positionY >= 150) {
            direction = "left"
        }
    }

    if(direction === 'left') {
        positionX--;

        if(positionX <= 0) {
            direction = 'top'
        }
    }

    if(direction === 'top') {
        positionY--;

        if(positionY <= 0) {
            direction = 'right'
        }
    }

    box.style.left = `${positionX}px`
    box.style.top = `${positionY}px`
}

setInterval(Animate, 5)

