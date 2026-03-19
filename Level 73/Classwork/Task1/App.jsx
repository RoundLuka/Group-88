// React-ში კომპონენტია ფუნქცია რომელიც აბრუნებს JSX-ს

import Card from "./Card";
import Header from "./Header";

import './App.css'
import Navbar from "./Navbar";
import Info from "./Info";
import Footer from "./Footer";

// html, css, js

function App() {

  function handleSubmit (username) {
    alert(username)
  }

  return (
    // fragments <> </>
    <>
      <Header />

      <form onSubmit={(e) => {
        e.preventDefault();
        console.log(e)
        handleSubmit(e.target.elements.user.value)
      }}>
        <input placeholder="Username" name="user" />
        <button type="submit">Send</button>
      </form>

      <Navbar />
      <Card />
      <Info />
      <Footer />

    </>
  )
}


// function App () {
//   let darkMode = false;

//   return (
//     {darkMode ? "ryer" : "eryre"}
//   )
// }

export default App;