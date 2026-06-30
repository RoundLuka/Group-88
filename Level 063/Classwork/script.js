// let inputField = document.querySelector("textarea");
// let statsP = document.querySelector('p');

// addEventListener - დაამატე მოვლენის მსმენელი

// let characterLimit = 200;

// function manageCharacterLimit () {
//     let currentMessage = inputField.value;
//     let messageLength = currentMessage.length;

//     if (messageLength < characterLimit) {
//         statsP.style.color = 'green'
//         statsP.textContent = 'Characters: ' + messageLength + '/' + characterLimit
//     } else {
//         statsP.style.color = 'red'
//         statsP.textContent = "Character LIMIT EXCEEDED"
//     }
// }

// addEventListener

// callback


// inputField.addEventListener

// inputField.addEventListener("keydown", manageCharacterLimit, false)

// let btn = document.querySelector("button")

// function press() {
//     console.log("pressed")
// }

// function up() {
//     console.log('released')
// }


// btn.addEventListener("mousedown", press)

// btn.addEventListener("click", up)


// const div = document.querySelector("div")
// const p = document.querySelector("p")


// როდესაც კონკრეტული მოვლენა ხდება რამდენიმე ელემენტზე ერთდროულად რადგანაც ისინი არიან ერთმანეთდან დაკავშრებული
// ერთ-ერთი მშობელი და მეორე შვილი, ასეთ შემთხვევაში რომელი მოვლენა უნდა გაეშვას პირველი?

// bubbling - false (default) მოვლენა უნდა მოდეს ჯერ შვილ ელემენტებიდან / ქვემოდან აყვება დომს
// capturing - true მოვლენა უნდა მოხდეს ჯერ მშობელი ელემენტის / DOM-იდან მოყვება ქვემოთ

// function divHandler () {
//     console.log("Div got clicked")
// }

// function clickHandler () {
//     console.log("P got clicked")
//     }

// div.addEventListener("click", divHandler, false)

// p.addEventListener("click", clickHandler, false)