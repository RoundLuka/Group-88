import { useState, useEffect } from 'react';
import './App.css'
import useLocalStorage from './hooks/useLocalStorage';


function App () {
    const [text, setText] = useState("")

    return (
        <>
            <input className='bg-' value={text} onChange={(e) => setText(e.target.value)} />
        </>
    )
}


export default App;

