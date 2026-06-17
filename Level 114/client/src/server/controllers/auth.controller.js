const { writeData } = require("../util/file");

const handleRegister = (req, res) => {
    const {username, email, password} = req.body;

    if (!username || !email || !password) {
        res.status(400).json({message: "All the info is required"})
    }

    const account = {
        id: Date.now(),
        username,
        email,
        password
    }

    writeData(account)
    res.status(200).json({
        id: Date.now(),
        username,
        email
    })
}

module.exports = { handleRegister }