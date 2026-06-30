// class Square {
//     constructor(width) {
//         this.width = width;
//         this.height = width;
//     }

//     get area () {
//         return this.width * this.height
//     }

//     set area(val) {
//         this.height = Math.sqrt(val);
//         this.width = this.height;
//     }
// }


// setter/getter მეთოდები კლასებში რომლებიც კუთვნილებებივით იქცევიან

// let square1 = new Square(4);

// console.log(square1.area)

// square1.area = 36

// console.log(square1.width)


// ობიექტებში გვაქვს დაცული კუთვნილებები 2 ტიპის
// protected რომელიც იწერება ერთი _ თავსართით რეალურად ფუნქცინოალურად არანაირი ცვლილება არ არის
// private კუთვნილება არის დაფარული და კლასის გარეთ არაა ხელმისაწვდომი, მისი წამოღება შეიძლება კლასის გარეთ მხოლოდ getter მეთოდის გავლით და შეცვლა კი setter-ით


let myAccount = new Bank("wtyerye", "wryery", "eryer", 400)

class Bank {
    #balance = 0;

    constructor(user, email, password, balance) {
        this.user = user,
        this.email = email,
        this.password = password,
        this.#balance = balance
    }
    
    get balance () {
        return `Account balance is ${this.#balance}`;
    }

    set balance (newBalance) {
        if (newBalance < 0) {
            console.log("Balance must be positive")
        } else {
            this.#balance = newBalance
        }
    }

}

let account1 = new Bank("Luka", 'Luka@gmai..com', "luka1234", 500)
console.log(account1.balance)
account1.balance = 300;
console.log(account1.balance)



// class, method, static
// getter/setter, private
