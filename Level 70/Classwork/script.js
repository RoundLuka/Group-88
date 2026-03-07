// map, filter, forEach, reduce

// iterable - მონცამეთა ტიპია რომელსაც შეგიძლია ციკლით გადაუაროთ
// iterable.map(function) 
// ყველა iterable-ის ელემენტზე გამოიძახებს ფუქნციას და ამ ფუნქციის მიერ დაბრუნბულ შედეებს შეინახავს ახალ iterable
// არ ცვლის თავდაპირველ მნიშვნელობას

// let myArr = [4, 5, 6, 11, 20, 12, 13, 15]

// let newArr = myArr.map(element => element ** 2);
// let filteredArr = myArr.filter(num => num % 2 === 0);

// let highest = 0;

// myArr.forEach((num) => {
//     if (num > highest) {
//         highest = num
//     }
// })


// console.log(highest)
// let total = myArr.reduce((prevValue, currentValue) => {
//     return prevValue + currentValue;
// })

// console.log(total)

// 

// class MyArray {
//     constructor(value) {
//         this.value = value;
//     }

//     manualMap(callback) {
//         let result = [];

//         for(let item of this.value) {
//             result.push(callback(item))
//         }
//         return result;
//     }
// }

// let array1 = new MyArray([4, 5, 6, 11, 20, 12, 13, 15])

// console.log(array1.manualMap(num => num * 2))

// function manualFilter(iterable, callback) {
//     let result = [];

//     for(let item of iterable) {
//         if (callback(item)) {
//             result.push(item)
//         }
//     }

//     return result;
// }

// 

// import Account, {getAccountFullName as getUsername, getAccountEmail} from './user.js'

// let user1 = new Account("Luka", "Gurgenidze", "luka@gmail.com", "1234")

// console.log(getAccountFullName(user1))
// console.log(getAccountEmail(user1))


// sync vs async

// async & await

async function getData () {
    try {
        const reponse = await fetch("https://jsonplaceholder.typicode.com/todos/")
        const data = await reponse.json();
        data.map((object) => {
            document.body.innerHTML += `
                <h2>${object.title}</h2>
            `
        })
    } catch (error) {
        console.log(`Error ${error}`)
    }
}

getData()
