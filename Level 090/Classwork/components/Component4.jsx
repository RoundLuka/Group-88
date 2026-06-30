import './Components.css';
import { useContext } from 'react';
import { nameContext } from './Component1';


export default function Component4 () {
    const data = useContext(nameContext)

    return (
        <div className='componentDiv'>
            <h2>Component 4</h2>
            <h2>Username: {data}</h2>
        </div>
    )
}