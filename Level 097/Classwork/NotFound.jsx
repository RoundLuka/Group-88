import { useEffect } from 'react';
import { useNavigate, Navigate } from 'react-router-dom';

const NotFound = () => {
    const navigate =  useNavigate();

    const state = null;

    useEffect(() => {
        setTimeout(() => {
        navigate("/")
    }, 2000)

    })

    
    return (
        <h1>Page doesn't exsist: Error 404</h1>
    )
}

export default NotFound;