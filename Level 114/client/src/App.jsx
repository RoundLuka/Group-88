import { useEffect } from "react";
import useAuth from "./context/AuthContext";

function App () {
  const { user, register } = useAuth();


  const handleRegister = (e) => {
    e.preventDefault();

    const account = {
      username: e.target.username.value,
      email: e.target.email.value,
      password: e.target.password.value
    }
    
    register(account)
  }

  return (
    <form onSubmit={handleRegister}>
      <input type="text" placeholder="Username" name="username" required />
      <br />
      <input type="email" placeholder="Email" name="email" required />
      <br />
      <input type="password" placeholder="Password" name="password" required />
      <br />
      <button>Sign up</button>
    </form>
  )
}

export default App;