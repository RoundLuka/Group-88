import React, { useState, useEffect, useCallback } from 'react';

const products = [
    {id: 0, title: "Laptop"},
    {id: 1, title: "Router"},
    {id: 2, title: "Modem"},
    {id: 3, title: "Server"},
    {id: 4, title: "PC"},
    {id: 5, title: "Smartphone"}
]


export default function App () {
    const [index, setIndex] = useState(0);
    const [otherState, setOtherState] = useState(0)

    const nextProduct = useCallback(() => {
        return products[index]
    }, [index])

    return (
        <>
            <button onClick={() => setIndex((prev) => prev + 1)}>Increment Index</button>
            <p>Index: {index}</p>
            <button onClick={() => setOtherState(otherState + 1)}>Change other state</button>
            <p>Other state: {otherState}</p>

            <hr />

            <ProductList productToRender={nextProduct} />
        </>
    )
}

function ProductList({productToRender}) {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        setProducts([...products, productToRender()])
    }, [productToRender])

    return (
        <div>
            {products.map((value, _) => {
                return <p key={value.id}>{value.title}</p>
            })}
        </div>
    )
}