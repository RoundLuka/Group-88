import pfp from './assets/pfp.jpg'

function Card () {
    return (
        <div className='card'>
            <h2>My Card</h2>
            <img src={pfp} />
            <h3>Luka Gurgenidze</h3>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Labore, dolore dolores numquam excepturi eius ea ex eligendi porro nulla ad aliquid magnam illo nam neque impedit. Est harum velit quas.</p>
        </div>
    )
}

export default Card;