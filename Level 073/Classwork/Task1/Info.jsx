let domainNames = ["com", "org", "net", "ge"]

// map

export default function Info () { 

    return (
        <ul>
            {domainNames.map((value, index) => <li key={index}>{value}</li>)}
        </ul>
    )
}
