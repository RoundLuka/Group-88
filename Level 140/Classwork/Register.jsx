import { useEffect, useState } from 'react';


import { createUserWithEmailAndPassword, signOut, signInWithPopup } from 'firebase/auth';
import { auth, googleProvider } from "../config/auth";


const Register = () => {
    const [email, setEmail] = useState(null);
    const [password, setPassword] = useState(null);

    useEffect(() => {
        console.log(auth?.currentUser?.email)
    })

    const signUp = async () => {
        try {
            await createUserWithEmailAndPassword(auth, email, password)
        } catch (err) {
            alert(err)
        }
    }

    const logout = async () => {
        try {
            await signOut(auth)
        } catch(err) {
            alert("Couldn't log out")
        }
    }

    const googleSignup = async () => {
        try {
            await signInWithPopup(auth, googleProvider)
        } catch(err) {
            alert(err)
        }
    }

    return (
        <>
            <h1>Register</h1>
            <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)}  />
            <input type="password"  placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={signUp}>Sign up</button>

            <br />
            <button onClick={logout}>Logout</button>
            <br />
            <button onClick={googleSignup}>Sign up with google</button>
        </>
    )
}

export default Register;