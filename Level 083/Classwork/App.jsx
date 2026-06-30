import { useState, useEffect } from 'react';


function App () {
    const [accounts, setAccounts] = useState();
    const [loggedUser, setLoggedUser] = useState(null);
    const [students,  setStudents] = useState([])

    useEffect(() => {
        setAccounts(JSON.parse(localStorage.getItem("accounts")) || [])
        setLoggedUser(JSON.parse(localStorage.getItem("loggedUser")) || null)
        setStudents(JSON.parse(localStorage.getItem("students")) || [])
    }, [])

    
    const handleRegister = (e) => {
        e.preventDefault();

        let account = {
            username: e.target.username.value,
            password: e.target.password.value
        }  

        const alreadyExists = accounts.some(acc => acc.username === account.username)
        
        if (alreadyExists) {
            alert("Same account is created")
            return
        }

        setAccounts((prev) => [...prev, account])
        localStorage.setItem("accounts", JSON.stringify(accounts))
    }

    const handeLogin = (e) => {
        e.preventDefault();

        const username = e.target.username.value;
        const password = e.target.password.value;

        const correctInfo = accounts.some(acc => acc.username === username & acc.password === password)

        if (correctInfo) {
            setLoggedUser(username)
        }
        localStorage.setItem("loggedUser", JSON.stringify(username) || null)
    }

    const addStudent = (e) => {
        e.preventDefault();
        const studentName = e.target.student.value;
        const grade = e.target.grade.value;
        const studentClass = e.target.class.value;

        setStudents((prev) => [...prev, {studentName, grade, studentClass}])
        localStorage.setItem("students", JSON.stringify(students))
    }

    if (loggedUser) {
        return (
            <>
                <h1>Greetings {loggedUser}</h1>
                <button onClick={() => {
                    setLoggedUser(null)
                    localStorage.setItem("loggedUser", null )
                }}>Logout</button>
                <form onSubmit={addStudent}>
                    <input placeholder='Student Name' name='student' type='text' required />
                    <input placeholder='Grade' name='grade' type='text' required />
                    <input placeholder='Class' name='class' type='text' required />
                    <button type='submit'>Send</button>
                </form>
                <table border={1}>
                    <thead>
                        <tr>
                            <th>Student Name</th>
                            <th>Grade</th>
                            <th>Class</th>
                            <th>Delete</th>
                        </tr>
                    </thead>
                    <tbody>
                        {students.map((student,  index) => {
                            return (
                                <tr key={index}>
                                    <td>{student.studentName}</td>
                                    <td>{student.grade}</td>
                                    <td>{student.studentClass}</td>
                                    <td><button onClick={() => setStudents((prev) => prev.filter((_, i) => i !== index))}>Delete</button></td>
                                </tr>
                            )
                        })}
                    </tbody>
                </table>
            </>
        )
    }


    return (
        <>
            <h2>Register</h2>
            <form onSubmit={handleRegister}>
                <input placeholder='Username' name='username' type='text' required />
                <input placeholder='Password' name='password' type='password' required />
                <button type='submit'>Send</button>
            </form>
            <h2>Log in</h2>
            <form onSubmit={handeLogin}>
                <input placeholder='Username' name='username' type='text' required />
                <input placeholder='Password' name='password' type='text' required />
                <button type='submit'>Send</button>
            </form>
        </>
    )
}


export default App;