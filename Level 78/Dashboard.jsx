function DashBoard ( { children, link1} ) {
    return (
        <div>
            {children}
            <nav>
                <ul>
                    <li><a href="#">{link1}</a></li>
                    <li><a href="#">Link 2</a></li>
                    <li><a href="#">Link 3</a></li>
                </ul>
            </nav>
        </div>
    )
}

export default DashBoard;