import { useState, useEffect } from 'react';
import './App.css'
import useToggle from './hooks/useToggle';

function App () {
    const [username,  setUsername] = useState("");
    const [showAlert, setShowAlert] = useState(true);
    const [darkMode, turnDarkMode] = useToggle(false);


    useEffect(() => {
        if(username.length > 4) {
            setShowAlert(true)
        } else {
            setShowAlert(false)
        }
    }, [username])


    return (
        <div className={darkMode ? "dark" : "light"}>
            <button onClick={turnDarkMode}>{!darkMode ? 'dark mode 🌙' : 'light mode ☀️'}</button>
            <input type='text' placeholder='Username' name='username' onChange={(e) => setUsername(e.target.value)} value={username}  />
            {showAlert || <p>Username must contain at least 4 characters</p>}
        </div>
    )
}


export default App;

