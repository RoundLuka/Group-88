import { Link, NavLink, useNavigate, useSearchParams } from 'react-router-dom';
import "./navbar.css"
import { useEffect } from 'react';

const Navbar = () => {
    const navigate = useNavigate()
    const [searchParams, setSearchParams] = useSearchParams();

    useEffect(() => {
        alert(searchParams.get("user"))
    }, [searchParams])

    return (
        <nav>
            <button onClick={() => navigate(-1)} >Previous</button>
            <button onClick={() => navigate(1)}>Next</button>
            <ul>
                <li><NavLink>Home</NavLink></li>
                <li><Link to='/about' >About</Link></li>
                <li><Link to='/products' >Products</Link></li>
                <li><Link to='/products/1' >Product 1</Link></li>
                <li><Link to='/products/2' >Product 2</Link></li>
            </ul>
        </nav>
    )
}

export default Navbar;