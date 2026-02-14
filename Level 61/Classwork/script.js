const products = [
    {name: 'Product1', price: 100, desc: "this is product1, most developed featurwe tertyerty"},
    {name: 'Product2', price: 200, desc: "truyryet, most developed featurwe tertyerty"},
    {name: 'Product3', price: 300, desc: "ttyututyd featurwe tertyerty"},
    {name: 'Product4', price: 400, desc: "thrturturtuduct1, most developed featurwe tertyerty"},
];

const productsContainer = document.getElementById("productsContainer");
const cartContainer = document.getElementById("cartContainer");

function addProduct (currentProduct) {
    cartContainer.innerHTML += `
        <div class='productDiv' >
            <h2>${currentProduct.name}</h2>
            <p>Price $${currentProduct.price}</p>
            <p>Description: ${currentProduct.desc}</p>
            <img width='200px' height='200px' />
            <button onclick=${addProduct(currentProduct)}>Buy</button>
        </div>
    `
}

function renderProduct(currentProduct) {
    productsContainer.innerHTML += `
        <div class='productDiv' >
            <h2>${currentProduct.name}</h2>
            <p>Price $${currentProduct.price}</p>
            <p>Description: ${currentProduct.desc}</p>
            <img width='200px' height='200px' />
            <button onclick=${addProduct(currentProduct)}>Buy</button>
        </div>
    `
}

for(let i = 0; i < products.length; i++) {
    let currentProduct = products[i];

    renderProduct(currentProduct)
}
