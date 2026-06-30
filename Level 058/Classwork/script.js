// object literal
// let book = {
//     title: "Ivanhoe",
//     author: "Walter Scott",
//     getAuthor: function() {
//         console.log("Author of the book " + this.author)
//     }
// }

// console.log(book.title)
// console.log(book.author)
// console.log(book.getAuthor())

// function readBook() {
//     if (readPages < pages) {
//         this.readPages += 1;
//     } else {
//         console.log("You have finished reading the book")
//     }
// }

// function book(title, author, year, pages,) {
//     this.title = title;
//     this.author = author;
//     this.year = year;
//     this.pages = pages;
//     this.readPages = 0;
//     this.readBook = readBook;
//     this.bookName = function () {
//         console.log("Book name " + this.title)
//     }
// }

// const ww2 = new book("World Wars 2", "Hitler", 1939, 500)
// const sovietUnion = new book("The Soviet Union", "Stalin", 1922, 500)


// console.log(ww2.title)
// console.log(ww2.author)

// let book = {
//     title: "Ivanhoe",
//     author: "Walter Scott"
// }

// let book2 = book;
// book.title = "Robin Hood";
// console.log(book2.title)

// let languages = ["HTML", "CSS", "JS"]
// langauges

let DataBase = [];

const sendBtn = document.getElementById("sendBtn");
const registerForm = document.getElementById("registrationForm");

function account(name, email, password, age) {
    this.name = name;
    this.email = email;
    this.password = password;
    this.age = age;
}

sendBtn.onclick = function() {
    const name = registerForm.elements.username.value;
    const password = registerForm.elements.password.value;
    const email = registerForm.elements.email.value;
    const age = registerForm.elements.value;

    const newAccount = new account(name, password, email, age);
    DataBase.push(newAccount)
    console.log(DataBase)
}