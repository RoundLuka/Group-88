const andOperand1 = document.getElementById("and1");
const andOperand2 = document.getElementById("and2");
const andBtn = document.getElementById("andSend");
const andResult = document.getElementById("andRes");

const orOperand1 = document.getElementById("or1");
const orOperand2 = document.getElementById("or2");
const orBtn = document.getElementById("orSend");
const orResult = document.getElementById("orRes");


andBtn.onclick = function () {
    let val1 = andOperand1.checked;
    let val2 = andOperand2.checked;
    let logicalResult = val1 && val2;
    andResult.textContent = 'Result of operation: ' + String(val1) + ' && ' + String(val2) + ' = ' + logicalResult;
}

orBtn.onclick = function () {
    let val1 = orOperand1.checked;
    let val2 = orOperand2.checked;
    let logicalResult = val1 || val2;
    orResult.textContent = 'Result of operation: ' + String(val1) + ' && ' + String(val2) + ' = ' + logicalResult;
}