import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

const Product = () => {
    const { id } = useParams();

    const [product, setProduct] = useState(null);


    useEffect(() => {
        fetch(`https://fakestoreapi.com/products/${id}`)
            .then(res=>res.json())            
            .then(json=>setProduct(json))
    }, [id])
    
    if (!product) {
        return
    }

    return (
        <>
            <h1>Product: {id}</h1>
            <h2>{product.title}</h2>
            <p>price: ${product.price}</p>
            <p>description {product.description}</p>
            <p>category: {product.category}</p>
            <p>rating: {product.rating.rate}</p>
            <button>Buy</button>
        </>
    )
}

export default Product;