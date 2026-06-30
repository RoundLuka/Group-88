class Account {
    constructor(firstName, lastName, email, password) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.password = password;
    }
}

function getAccountFullName (user) {
    return `${user.firstName} ${user.lastName}`
}

function getAccountEmail (user) {
    return user.email;
}

export {getAccountFullName, getAccountEmail};      


export default Account;