const fs = require('fs');
const path = require('path');

const file_url = path.join(__dirname, "../Database/accounts.json");

const readData = () => {
    const data = fs.readFileSync(file_url, 'utf-8', (err, info) => {
        if(err) {
            console.log(err)
        }
        return info
    })
    return JSON.parse(data)
}

const writeData = (data) => {
    const info = readData();
    info.push(data)
    fs.writeFileSync(file_url, JSON.stringify(info))
}

module.exports = {readData, writeData}