// ecmascript 6 objects

// let lastName = "username"

// function deposit(amount) {
//     return this.balance += amount
// }

// reference


// let account1 = {
//     username: "Luka",
//     score: 20
// }

// let account1Duplicate = Object.assign({}, account1)

// console.log(account1)

// account1Duplicate.username = "John"

// console.log(account1Duplicate)

// let acccount2 = {
//     balance: 200
// }

// let account3 = {
//     email: "luka@gmail.com",
//     username: "Irakli"
// }

// let combined = Object.assign(account3, acccount2, account1)
// console.log(combined)


// account.deposit(25)
// account.deposit(50)

// console.log(account)

// es6 arrow functions

// function fullName(fname, lname) {
//     return fname + " " + lname
// }

// const fullName = fname => fname + "!"

// console.log(fullName("Luka", "Gurgenidze"))

// es6 destrucutring

// const dataArr = ["weryhretyq", "yerye", "gfjrtjyut"];

// let [data1, data2, data3="duherturur", data4="eryuerue"] = dataArr;

// console.log(data1)
// console.log(data2)
// console.log(data3)

// console.log(dataArr)

// const personAccount = {
//     username: "Luka",
//     dinosaur: false,
//     height: 1.77
// }

// const {username: firstName, dinosaur, height} = personAccount


// console.log(firstName)
// console.log(dinosaur)
// console.log(height)

// let height, dinosaur, username;
// ({height, dinosaur, username} = personAccount);
// console.log(personAccount)


// spread

// const values = [11, 36, 67]

// const numbers = [52, 236, 35, ...values, 37, 264]

// console.log(numbers)

// const [num1, num2, ...others] = numbers

// console.log(num1)
// console.log(num2)
// console.log(others)

// *args

// rest

// function anything(argument1, ...otherArguments) {
//     console.log(`First: ${argument1}`)
//     console.log(`Others: ${otherArguments}`)
// }

// anything("twryer", true, 2345, "erwtyer")

// function magic(...nums) {
//   let sum = 0;
//   nums.filter(n => n % 2 == 0).map(el => sum+= el);
//   return sum;
// }
// console.log(magic(1, 2, 3, 4, 5, 6));

// function construcotr

// oop

class Account {

    static accounts = 0;

    constructor(firstName, lastName, email, password, balance) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this._password = password;
        this.balance = balance

        Account.accounts += 1;
    }

    // static || method
    static logAccounts () {
        console.log(`Currently there are ${Account.accounts} accounts`)
    }

    deposit () {
        this.balance += 100
    }

    get password() {
        return this._password;
    }
}

let obj1 = new Account("Luka", "Gurgenidze", "luka@gmail.com", "luka1234", 500)
let obj2 = new Account("John", "Doe", "doe@gmail.com", "1234", 1000)



Account.logAccounts()

obj1.deposit()
obj1.deposit()

// console.log(obj1)
console.log(obj2.password)
