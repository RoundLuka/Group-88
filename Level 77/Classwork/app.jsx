// 2) შექმენით კომპონენტი, გექნებათ ცვლადი 50/50-ზე math.random-ის დახმარებით რომლის მიხედვითაც საიტზე გამოიტანთ ან ფორმას ან დაულაგებელ სიას სადაც იქნება ღილაკი. როდესაც მოხდება ფორმის ღილაკზე / დაუალგებელ სიის ღილაკზე დაჭერა უნდა გამოიძახეთ handler ფუნქცია (უნდა გქონდეთ ორივე ღილაკისთვის სადასხვა handleSubmit, handleClick) alert-ის გამოიტანეთ რაიმე და თქვენი ცოდნით კიდევ თუ შეძლებ რაიმე ლოგია გაუწერეთ

function App () {
  const signedIn = Math.random() > 0.5;
  
  function handleSubmit (e) {
    e.preventDefault();
    alert("Form submitted")
  }

  function handleClick () {
    alert("Clicked")
  }


  if (signedIn) {
    return (
      <form onSubmit={handleSubmit}>
        <h2>{`SignedIn: ${signedIn}`}</h2>
        <input placeholder="Username" type="text" />
        <button type="submit">Send</button>
      </form>
    )
  } else {
    return (
      <div>
        <h2>{`SignedIn: ${signedIn}`}</h2>
        <ul>
          <li>Georgia</li>
          <li>Germany</li>
          <li>Greenland</li>
        </ul>
        <button onClick={()=>{alert("Purchase Complete")}}>Purchase</button>
      </div>
    )
  }
}


export default App;