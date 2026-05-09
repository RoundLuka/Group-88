import { useState, useEffect } from "react";
import { useOutletContext, useParams } from "react-router-dom";

const Product = () => {
    const { id } = useParams();
    const { username } = useOutletContext()

    const [products, setProducts] = useState(null);


    useEffect(() => {
        fetch(`https://fakestoreapi.com/products/`)
            .then(res=>res.json())            
            .then(json=>setProducts(json))
    }, [id])
    
    if (!products) {
        return
    }

    return (
        <>
            <h1>{username}</h1>
            {products.map((product, index) => {
                return (
                    <div>
                        <h2>{product.title}</h2>
                        <p>price: ${product.price}</p>
                        <p>description {product.description}</p>
                        <p>category: {product.category}</p>
                        <p>rating: {product.rating.rate}</p>
                        <button>Buy</button>
                        <hr />
                    </div>
                )
            })}
        </>
    )
}

export default Product;