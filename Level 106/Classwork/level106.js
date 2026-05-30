// let numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
// let secretValue = (Math.floor(Math.random() * 9)).toString()

// function testNumber (input) {
//     if (input === "quit") {
//         console.log("Ok. Bye!\n")
//     }

//     if (!numbers.includes(input)) {
//         console.log("Please pick a number 1 through 10\nIs the number ...")
//     } else if (input === secretValue) {
//         console.log("You guessed the number")
//     } else {
//         console.log("Incorrect, try again")
//     }
// }

// const playGame = (inputData) => {
//     testNumber(inputData.toString().trim())
// }

// process.stdin.on('data', playGame)

// const { Buffer } = require("buffer");

// const dataStream = Buffer.alloc(10, "a", "b")

// console.log(dataStream)

// const stringBuffer = Buffer.from("luka")

// console.log(Buffer.concat([dataStream, stringBuffer], 14))

// const fs = require('fs');
// const path = require('path');


// if(!fs.existsSync("./newFolder")) {
//     fs.mkdir("./newFolder", (err) => {
//     if (err) console.log("couldn't be created")
//     else console.log('folder created succesfully')
//     })
// } else {
//     fs.rmdir("./newFolder", (err) => {})
// }


// const file_path = path.join(__dirname, 'data', 'message.txt')

// async function processingFile() {
//     try {
//         const readData = await fs.promises.readFile(file_path, 'utf8')
//         console.log(readData)
//         await fs.promises.writeFile('./data/input.txt', 'something new i just wrote')
//         await fs.promises.appendFile('./data/input.txt', '\n\nnew text appended')
//         await fs.promises.rename('./data/input.txt', './data/output.txt')
//     } catch (err) {
//         console.log(err)
//     }
// }

// processingFile()


// fs.readFile(file_path, 'utf-8', (err, data) => {
//     if (err) {
//         throw new Error()
//     } else {
//         console.log(data.toString())
//     }
// })

// fs.writeFile('./data/input.txt', "wtreyeuyeurtururur", (err) => {
//     if (err) {
//         console.log(err)
//     } else {
//         console.log("wrote in file succesfully")
//     }

//     fs.appendFile('./data/input.txt', "weryrreyeyer", (err) => {
//         console.log(err)

//         fs.renameSync('./data/input.txt', './data/wertyeryeye.txt')
//     })
// })


// process.on("uncaughtException", (err) => {
//     console.log("Couldn't read data")
// })

const readline = require('readline');
const fs = require('fs');

// const readInterface = readline.createInterface({
//     input: fs.createReadStream("text.txt")
// })

// readInterface.on('line', (line) => {
//     console.log(line)
// })

const writeableStream = fs.createWriteStream("text.txt")

writeableStream.write("chunky monkey\n")
writeableStream.write("funky donkey\n")
writeableStream.write("monkey donkey\n")

writeableStream.end()