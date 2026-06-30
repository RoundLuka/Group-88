function Product (props) {
    return (
        <div className="products">
            <h2>{props.productName}</h2>
            <p>Product description: {props.desc}</p>'
            <img width="200px" height="200px" src={props.src} />
            <button>Buy</button>
        </div>
    )
}

export default Product;

// props - properties