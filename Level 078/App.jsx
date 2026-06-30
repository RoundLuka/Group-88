import DashBoard from "./Dashboard";
import Product from "./Product";

function App () {
    return (
        <>
            <DashBoard link1="wetywer">
                <h2>very cool site</h2>
            </DashBoard>
            <Product productName="Apple" desc="Basic red apple" src="https://www.paperandtea.com/cdn/shop/articles/Apfel_7ebe153a-a4ac-473a-9217-658894dfc968.jpg?v=1765535477&width=1500" />
            <hr></hr>
            <Product productName="Grapes" desc="qartuli kaxuri yurdzeni" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9NNnTM0-k5i23AukVycCGR_Poj-6wQL6qfg&s" />
            <hr></hr>
            <Product productName="Soviet" desc="ryuer uetuy bn wl bla" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMG0rln6ezolHjQq_MPFKq7mi9R0W0X5iXCQ&s" />
        </>
    )
}


export default App;