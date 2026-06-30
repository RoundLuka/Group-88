import { useState, useEffect} from 'react';

function getSavedValue (key, initalValue) {
    const saved = JSON.parse(localStorage.getItem(key))

    if (!saved) {
        return initalValue
    }

    return saved
}

export default function useLocalStorage(key, initalValue) {
    const [value, setValue] = useState(() => {
        return getSavedValue(key, initalValue)
    })

    useEffect(() => {
        localStorage.setItem(key, JSON.stringify(value))
    }, [value])

    return [value, setValue]
}