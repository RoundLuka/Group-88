import { Outlet } from "react-router-dom";

const ProductDashboard = () => {
    return (
        <>
            <h1>This one of the products pages</h1>
            <Outlet context={ { username: "Luka" } } />
        </>
    )
}

export default ProductDashboard;