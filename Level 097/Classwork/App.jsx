import React from 'react';
import { Routes, Route } from 'react-router-dom';
import About from './About';
import ProductList from './ProductList';
import Product from './Product';
import ExoticProduct from './ExoticProduct';
import Navbar from './Navbar';
import ProductDashboard from './ProductDashboard';
import NotFound from './NotFound';
import Home from './HOme';

export default function App () {


    return (
        <>
            <Navbar />
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/about' element={<About />} />

                <Route path='/products' element={<ProductDashboard />}>
                    <Route index element={<ProductList />} />
                    <Route path=':id' element={<Product />} />
                    <Route path='exotic' element={<ExoticProduct />} />
                </Route>

                <Route path='*' element={<NotFound />}  />
            </Routes>
        </>
    )
}
