// #private
// _protected

// setter
// getter


// class Human {
//     constructor(username) {
//         this.username = username;
//     }

//     heal () {
//         console.log(`First aid`)
//     }
// }

// class Doctor extends Human {
//     constructor(username, rank) {
//         super(username)

//         this.rank = rank;
//     }

//     heal () {
//         console.log(`${this.username} is currently `)
//     }
// }

// let person1 = new Human("Joe")
// person1.heal()

// let house = new Doctor("Dr.House", "Medical director")
// house.heal()
// console.log(house)

// set - წყობა, მასივი არ შეიძლება ელემენტების განმრეობა
// let myArray = [1, 2, 3, 4, 5, 5000]
// let mySet = new Set(myArray)

// mySet.add(6)
// mySet.delete(5000)
// mySet.has()
// // mySet.clear()
// console.log(mySet.size)

// console.log(mySet)

// map data type

// const myMap = new Map(
//     [
//         ["username", "Pavle"],
//         ["Giorgi", 6],
//         ["Nika", 4],
//         [true, 5],
//         [3, "ika"]
//     ]
// )

// console.log()

// myMap.set("key", "value")
// myMap.set({ hello: "World" }, 5)
// let result = myMap.delete(true)
// console.log(myMap.keys())
// console.log(myMap.has("username"))
// myMap.clear()


// console.log(myMap)
// const a = () => { console.log("a") }
// const b = () => { console.log("a") }

// let testObject = {
//     a: a,
//     b: b
// }

// console.log(testObject)

// const testMap = new Map(
//     [
//         [a, 226],
//         [b, 12]
//     ]
// )

// console.log(testMap.get(a))
// console.log(testMap.get(b))

// 1 thread

// promise 
// pending

// const promise = new Promise((resolve, reject) => {
//     let myNumber = 11;
//     setTimeout(() => {
//     }, 4000)

//     if (myNumber === 10) {
//         resolve("Promise fulfiled")
//     } else {
//         reject("Failed")
//     }
// })

// promise
// .then((result) => {
//     console.log(result)
// })

// javascript object notation

// fetch,

let main = document.querySelector("main");
let input = document.querySelector("input")
let button = document.querySelector("button");

button.addEventListener("click", fetchInfo)

function renderInfo(info) {
    console.log(info)

    main.innerHTML = `
        <div>
            <h2>${info.name}</h2>
            <img src="${info.avatar_url}" />
            <p>Bio: ${info.bio}</p>
            <p>Followers: ${info.followers}</p>
            <p>Following ${info.following}</p>
            <p>Repositiories: ${info.public_repos}</p>
        </div>
    `
}

function fetchInfo () {
    let username = input.value;
    let promise = fetch(`https://api.github.com/users/${username}`)

    promise
        .then(response => response.json())
        .then(data => renderInfo(data))
}

