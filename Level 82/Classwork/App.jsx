import { useState } from 'react';

function App () {
    const [formState, setFormState] = useState({});
    const handleChange = ( {name, value} ) => {
        setFormState((prev) => {
            return {...prev, [name]: value}
        })
        console.log(formState)
    }
    return (
        <>
            <input onChange={(e) => handleChange(e.target)} value={formState.username} name="username" type='text' placeholder='Username' />
            <input onChange={(e) => handleChange(e.target)} value={formState.password} name='password' type='password' placeholder='Password' />
        </>
    )
}


export default App;