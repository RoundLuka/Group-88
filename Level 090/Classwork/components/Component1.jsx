import { useState, createContext } from 'react';
import './Components.css';
import Component2 from './Component2';

// Context - api რომელიც საშვალებას გვაძლევას რომ რაიმე 

export const nameContext = createContext();

export default function Component1 () {
    const [name, setName] = useState('Luka');

    return (
        <div className='componentDiv'>
            <h2>Component 1</h2>
            <nameContext.Provider value={name} >
                <Component2 />
            </nameContext.Provider>
        </div>
    )
}