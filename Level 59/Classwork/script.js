// let myNumber = 15;

// let newNumber = myNumber;

// newNumber = 20;

// console.log(myNumber)

// let person = {
//     firstName: "John",
//     gender: "Male"
// }

// let newPerson = person;

// newPerson.firstName = "Mark"

// console.log(person)

// primitive data types (პრიმიტიული) number, string, boolean
// complex data types (კომპლექსური) array, object, function

// stack over flow როდესაც stack გადაივსება
// გამომწვევი მიზეზი ხშირად არის memory leak

// let count = 0;

// function storeBook() {
//     storeBook()
// }

// storeBook()

// literal method
// const gameProject = {
//     title: "Do game project challange",
//     desc: "Have to make unique game out creativity",
//     state: true,
// }

// constructor
// function task(title, desc, state, deadline) {
//     this.title = title;
//     this.desc = desc;
//     this.state = state;
//     this.deadline = deadline;
// }


// const doGroupWork = newtask("group work")

// const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// ----------------------------------------------

// console.log(Math.random())
// console.log(Math.abs(-4))
// console.log(Math.ceil(2.1))
// console.log(Math.floor(5.7))
// console.log(Math.round(4.4))
// console.log(Math.PI)
// console.log(Math.pow(2, 5))
// console.log(Math.trunc(3.7))
// console.log(Math.sign(5))
// console.log(Math.sqrt(15))
// console.log(Math.min(...[2, 3, 4]))
// console.log(Math.max(2, 3, 4))
// console.log(Math.log(4, 2))

// console.log(Math)

// let givenNumber = prompt("Enter a number: ")

// alert('Root of ' + givenNumber + ' is '  + Math.sqrt(givenNumber))

// const hireData = new Date('2025-12-23');

// console.log(hireData.getFullYear())
// console.log(hireData.getMonth())
// console.log(hireData.getDay())
// console.log(hireData.getHours())
// console.log(hireData.getMinutes())
// console.log(hireData.getSeconds())
// console.log(hireData.getSeconds())
// console.log(Date.UTC())


const taskField = document.getElementById("taskField");
const send = document.getElementById("send");
const tasksUl = document.getElementById("tasks");

send.onclick = function() {
    const task = taskField.value;

    // node
    const newLi = document.createElement('li');
    newLi.textContent = task;

    tasksUl.appendChild(newLi)

    newLi.onclick = function () {
        tasksUl.removeChild(newLi)
    }
}