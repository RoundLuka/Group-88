const form = document.querySelector("form");
const usernameField = form.elements.username;
const emailField = form.elements.email;
const telephoneField = form.elements.number;

// default refersh

const dataTable = document.querySelector("tbody")


function container (eventObject) {
    eventObject.preventDefault();
    
    const username = usernameField.value;
    const email = emailField.value;
    const telephone = telephoneField.value;

    form.reset()

    const acocunt = {
        username: username,
        email: email,
        telephone: telephone
    }

    presentatioal(acocunt)
}

function presentatioal(account) {
    dataTable.innerHTML += `
            <tr>
                <td>${account.username}</td>
                <td>${account.email}</td>
                <td>${account.telephone}</td>
            </tr>
        `
}

form.onsubmit = container

