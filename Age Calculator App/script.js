const form = document.getElementById("dateForm");
const submitBtn = document.getElementById("submit");

const daysP = document.getElementById("daysText");
const monthsP = document.getElementById("monthsText");
const yearsP = document.getElementById("yearsText");

const dayErrorP = document.getElementById("dayError");
const monthErrorP = document.getElementById("monthError");
const yearErrorP = document.getElementById("yearError");


function getDate(){
    const day = Number(form.elements.Day.value);
    const month = Number(form.elements.Month.value);
    const year = Number(form.elements.Year.value);

    yearsP.textContent = '--';
    monthsP.textContent = '--';
    daysP.textContent = '--';

    dayErrorP.textContent = '';
    monthErrorP.textContent = '';
    yearErrorP.textContent = '';

    let noMistake = true;

    if(day > 31){
        dayErrorP.textContent = 'Must be a valid day';
        noMistake = false;
    }
    if(month >= 13){
        monthErrorP.textContent = 'Must be a valid month'
        noMistake = false;
    }
    if(year > 2026 || year < 0){
        yearErrorP.textContent = 'Must be in the past'
        noMistake = false;
    }

    const currentDate = new Date();

    const bornDate = new Date(year, month - 1, day);

    let years = currentDate.getFullYear() - bornDate.getFullYear();
    let months = currentDate.getMonth() - bornDate.getMonth();
    let days = currentDate.getDate() - bornDate.getDate();

    if(days < 0){
        months -= 1;
        lastMonth = new Date(currentDate.getFullYear(),currentDate.getMonth(),0)
        days += lastMonth.getDate();
    }
    if(months < 0){
        years -= 1;
        months += 12;
    }

    if((bornDate.getDate() !== day) || (bornDate.getMonth() + 1 !== month) || (bornDate.getFullYear() !== year)){
        dayErrorP.textContent = 'Invalid date'; 
    }


    const dayTime = {
        year:years,
        month: months,
        day: days
    }

    
    if(noMistake){
        yearsP.textContent = years;
        monthsP.textContent = months;
        daysP.textContent = days;
    }
}  

submitBtn.addEventListener("click", getDate);