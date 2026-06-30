import { useState, useEffect } from 'react';

const useAuth = () => {
    const [user, setUser] = useState(null);
    const [accounts, setAccounts] = useState([]);

    useEffect(() => {
        const storedUser = JSON.parse(localStorage.getItem("user") || null)
        const storedAccounts = JSON.parse(localStorage.getItem("accounts") || "[]")
        setUser(storedUser)
        setAccounts(storedAccounts)
    }, [])

    const register = (username, password) => {
        setUser({username, password})
        setAccounts((prev) => [...prev, {username, password}])
        localStorage.setItem("user", JSON.stringify({username, password}))
    } 
    
    const login = (username, password) => {
        const accountFound = accounts.find((acc) => acc.username === username && acc.password === password)
        setUser({username, password})
    }

    const logout = () => {
        setUser(null)
        localStorage.setItem("user", null)
    }

    return {user, register, login, logout}
}

const useProduct = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const storedProducts = JSON.parse(localStorage.getItem('products') || '[]');
        setProducts(storedProducts);
    }, [])

    const addProduct = (product) => {
        setProducts((prev) => [...prev, product])
        localStorage.setItem('products', JSON.stringify(products))
    }

    return { products, addProduct }
}

const Registration = ( { register } ) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleRegister = (e) => {
        e.preventDefault();
        register(username, password)
    }

    return (
        <form onSubmit={handleRegister}> 
            <input type='text' placeholder='Username' onChange={(e) => setUsername(e.target.value)} value={username} required />
            <input type='password' placeholder='Password' onChange={(e) => setPassword(e.target.value)} value={password} required />
            <button type='submit'>Register</button>
        </form>
    )
}

const Login = ( { login } ) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handeLogin = (e) => {
        e.preventDefault();
        login(username, password)
    }

    return (
        <form onSubmit={handeLogin}> 
            <input type='text' placeholder='Username' onChange={(e) => setUsername(e.target.value)} value={username} required />
            <input type='password' placeholder='Password' onChange={(e) => setPassword(e.target.value)} value={password} required />
            <button type='submit'>Log in</button>
        </form>
    )
}

const AdminPanel = ({logout, products, addProduct}) => {
    const [product, setProduct] = useState("");
    const [price, setPrice] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        addProduct({product, price})
    }

    return (
        <div>
            <h2>Admin Panel</h2>
            <button onClick={logout}>Logout</button>

            <form onSubmit={handleSubmit}>
                <input type='text' placeholder='Product' onChange={(e) => setProduct(e.target.value)} required />
                <input type='text' placeholder='Price' onChange={(e) => setPrice(e.target.value)} required />
                <button type='submit'>Add Product</button>
            </form>
            <br />
            <table border="1px solid black">
                <thead>
                    <th>Product Name</th>
                    <th>Product Price</th>
                </thead>
                <tbody>
                    {products.map((product, index) => {
                        return (
                            <tr key={index}>
                                <td>{product.product}</td>
                                <td>{product.price}</td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )
}

function App () {
    const {user, register, login, logout} = useAuth();
    const {products, addProduct} = useProduct();

    return (
        <>
            {!user ? (
                <div>
                    <h2>Registration</h2>
                    <Registration register={register} />
                    <h2>Login</h2>
                    <Login login={login} />
                </div>
            ) : (
                <AdminPanel logout={logout} products={products} addProduct={addProduct} />
            )}
        </>
    )
}


export default App;