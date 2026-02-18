let images = [
    "http://www.sololearn.com/uploads/slider/1.jpg", 
    "http://www.sololearn.com/uploads/slider/2.jpg", 
    "http://www.sololearn.com/uploads/slider/3.jpg"
];

const nextBtn = document.getElementById("nextBtn");
const prevBtn = document.getElementById("prevBtn");
const image = document.querySelector('img');

let currentImageIndex = 0;

image.src = images[currentImageIndex]

nextBtn.onclick = function () {

    if (currentImageIndex > images.length - 1) {
        currentImageIndex = 0
    }

    image.src = images[currentImageIndex]
    currentImageIndex++;
}

prevBtn.onclick = function () {

    if(currentImageIndex < 0 ) {
        currentImageIndex = images.length - 1;
    }

    image.src = images[currentImageIndex]
    currentImageIndex--;
}

// localstorage-ის & sessionStorage მეთოდები
// setItem - ელემენტის ჩამატება
// getItem - ელემენტის წამოღება
// removeItem - ელემენტის წაშლა

localStorage.setItem("Name", "John")
localStorage.setItem("Surname", "Doe")

let Name = localStorage.getItem("Name")

localStorage.removeItem("Surname")

document.cookie = ""