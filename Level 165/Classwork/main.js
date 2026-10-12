"use strict";
// type Color = "Red" | 'Blue';
let academy;
academy = {
    students: 5,
    deparatments: 5,
    controllers: [{ username: "Luka", influence: 5 }]
};
let strategy = {
    creator: 22,
    adminList: [5],
    visits: 52
};
function doSomething(param1, param2) {
    let result = [];
    for (let i = 0; i < param2; i++) {
        result.push(i);
    }
    return result;
}
console.log(doSomething("Luka", 5));
