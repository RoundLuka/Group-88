import React from 'react'

const productContainer = async ({params}: { params: {id: string} }) => {
    const paramsData = await params;
    return (
        <div>
            <h1>Product {paramsData.id}</h1>
        </div>
    )
}

export default productContainer
