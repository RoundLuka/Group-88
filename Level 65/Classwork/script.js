const form = document.querySelector("form")

const userField = form.elements.username;
const emailField = form.elements.email;
const passwordField = form.elements.password;

let loggedUser = "";

function loadData () {
    let savedUser = localStorage.getItem("Username")

    if (savedUser) {
        loggedUser = savedUser
    }
}

loadData()
checkLoggedIn()

function saveData(user, email, pass) {
    localStorage.setItem("Username", user);
    localStorage.setItem("Email", email);
    localStorage.setItem("Password", pass);
}

function logOut() {
    localStorage.removeItem("Username")
}

function checkLoggedIn() {
    if (loggedUser) {
        document.body.innerHTML = `
            <h2>Username: ${loggedUser}</h2>
            <h2>Email: ${localStorage.getItem("Email")}</h2>
            <h2>Password: ${localStorage.getItem("Password")}</h2>
            <button onClick="${logOut()}">Logout</button>
        `
    }
}

function handleSubmit (e) {
    e.preventDefault()
    
    let username = userField.value;
    let email = emailField.value;
    let password = passwordField.value;

    if (username.length < 4) {
        alert("Username must be 8 characters")
        return
    }

    if(username.includes(" ")) {
        alert("Must not contain space")
        return;
    }

    if(password.length < 8) {
        alert("Password must be 8 characters long")
        return 
    }

    loggedUser = username

    saveData(username, email, password)

    alert("Account created succesfully")

    checkLoggedIn()
}

form.addEventListener("submit", handleSubmit)

