import { useState } from 'react';

// React-ში არსებობს hooks კაუჭები რომლებიც ყველა თითქმის თავისებურ პრობლემას წყვეტს
// react-ისეულ ღრმა ლოგიკას გვისრულებს, დახმარება ფუნქციის როლს ასრულებს


// hook-ს react-ში აქვთ დასახელების წესი: useHook

// კაუჭების გამოყენების ძირითადი წესები:
// 1. ყოველთვის კომპონეტის შიგნით იწერება
// 2. არ შეიძლება if-else loop ან რაიმე სტრქუტურაში ჩაშენება

// useState - კაუჭა რომელის მეშვეობითაც ვქმნთ მდგოამრეობას 

// როდესაც მდგომარეობის მნიშვნელობა შეიცვლება, სადმე თუკია გამოყენებული ეს მდგომარეობა თქვენს აპლიკაციაში ყველგან თავიდან მოხდება მისი განახლებული მნიშვნელობის დარენდერება

// useState-ის გამოყენებისას თქვენ გიბრუნდებათ მასივი 2 მნიშვნელბოით: პირველი არის თვითონ მდგომარეობის მნიშვნელობა, ხოლო მეორე არის მისი setter ფუნქცია (რომლის გამოძახებისას count თუ შეიცვალა თავიდან რადრენდერება ყველგან), მდგოამრეობის შეცვლა მხოლოდ თავის setter ფუნქციით, useState გადაეცემა ერთი არგუმენტი რაც არის თავდაპირველი მდგოამრეობის მნიშვნელობა

function App () {
    
    const [task, setTask] = useState([])

    const handleSubmit = (e) => {
        e.preventDefault();
        let newTask = e.target.elements.username.value;
        setTask((prev) => [...prev, newTask])
        console.log(task)
        e.target.elements.username.value = ""
    } 

    return (
        <>
            <form onSubmit={handleSubmit}>
                <input placeholder='Task' name='username' />
                <button type='submit'>Add Task</button>
            </form>
            <h2>Tasks</h2>
            <ul>
                {task.map((value, index) => <li key={index}>{value}
                    <button onClick={() => setTask(task.filter((_, i) => index !== i))}>Delete</button>
                </li>)}
            </ul>
        </>
    )
}


export default App;