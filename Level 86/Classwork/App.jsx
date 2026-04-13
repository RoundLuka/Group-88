import { useState, useEffect } from 'react';
import './App.css'

// Container - არ ფოკუსირებული jsx-ის დაბრუნებაზე, მისი მთავარია მოცანაა 
// გამოთვლების შესრულება & მონაცამების წამოღება და საბოლოოდ რაიმე presnetational
// კომპონენტის გამოძახება რომელსაც გადასცემს თავის ინფორმაციას props-ის საშვალებით

// Presentional - კომპონენტი რომელიც უბრალოდ იღებს ინფორმაციას და ამის მიხედვით
// არენდრებს შედეგს & გამოაქვს ვიზიალურად მონაცემები


    
function Presentional ( { productInfo, index } ) {
    return (
        <div className='product' key={index} >
            <h2 className='bg-green-700'>{productInfo.title}</h2> 
            <p>Price: {productInfo.price}$</p>
            <p>Description: {productInfo.description}</p>
            <p>Category: {productInfo.category}</p>
            <div>
                <p>Rating</p>
                <p>Rate: {productInfo.rating.rate}</p>
                <p>Total reviews: {productInfo.rating.count}</p>
            </div>
            <hr />
        </div>
    )
}


function App () {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchInfo () {
            const respones = await fetch("https://fakestoreapi.com/products")
            const data = await respones.json()
            setProducts(data)
            setLoading(false)
        }
    fetchInfo()
    }, [])

    if (loading) {
        return <p>Loading...</p>
    }

    return (
        <>
            <div className='products'>
                {products.map((product, index) => {
                    return (<Presentional productInfo={product} index={index} />)
                })}
            </div>
        </>
    )
}


export default App;