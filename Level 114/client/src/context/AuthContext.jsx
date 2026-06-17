import { createContext, useContext, useState } from "react";

const AuthContext = createContext();

const useAuth = () => useContext(AuthContext)

export default useAuth;

const API_URL = 'http://localhost:3000/root/auth'

export const AuthContextProvider = ({children}) => {
    const [user, setUser] = useState(null)

    const register = (account) => {
        try {
            const response = fetch(API_URL + '/signup', {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                }, 
                body: JSON.stringify(account)
            })
        } catch (err) {
            console.log(err)
        }
    }
    

    return (
        <AuthContext.Provider value={{user, register}}>
            {children}
        </AuthContext.Provider>
    )
}