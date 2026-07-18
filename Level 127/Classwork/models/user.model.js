const mongoose = require('mongoose');

// Schema for users collection (What fields are going to be in document and their types)
const userScema = new mongoose.Schema({
    username: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true 
    },
    password: {
        type: String,
        required: true
    }
})

// model for users collection, allowing us to create, read, update and delete
// data in base. basically is used to manipulate data in mongo from code (crud)
const User = mongoose.model("users", userScema);

module.exports = User;