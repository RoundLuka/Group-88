const difficultySelect = document.getElementById("difficulty")
const modeSelect = document.getAnimations("mode");

const startBtn = document.getElementById("start");

const preTest = document.getElementById("pre-test");

const testDiv = document.getElementById("test");

const typingField = document.getElementById("typingField");

function getWords(sentence) {
    const words = sentence.split(" ")
    return words
}

startBtn.addEventListener("click", () => {
    const allTests = tests[difficultySelect.value]

    const randomIndex = Math.floor(Math.random() * 9)


    const testObj = allTests[randomIndex];

    const sentence = testObj.text

    const words = getWords(sentence);
    
    const wordsDiv = document.createElement("div");
    wordsDiv.id = "wordsDiv"


    const charIndex = 0;

    for (let i = 0; i < words.length; i++) {
        let word = words[i]
        const newSpan = document.createElement("div")
        newSpan.className = "wordDiv"
        newSpan.id = `word-${i}`
        for(let j = 0; j < word.length; j++) {
            let char = word[j]
            const charSpan = document.createElement("span");
            charSpan.className = 'charSpan';
            charSpan.id = `char-${j}`
            charSpan.textContent = char
            newSpan.appendChild(charSpan)
        }
        wordsDiv.appendChild(newSpan)
        const spaceSpan = document.createElement("span");
        spaceSpan.textContent = " "
        wordsDiv.appendChild(spaceSpan)
    }


    preTest.style.display = 'None'
    testDiv.style.display = "Block"
    


    testDiv.appendChild(wordsDiv)

    typingField.addEventListener("input", (e) => {
        if(e.data === null) {
            charIndex--;
        } else {
            

            charIndex++;
        }
    })
})