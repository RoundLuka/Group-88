"use client";

import React from 'react'
import { useRouter } from 'next/navigation'

const layout = ({children}) => {
    const router = useRouter();

    return (
        <div>
            <ul>
                <li><button onClick={router.back}>Back</button></li>
                <li><button onClick={router.forward}>Forward</button></li>
            </ul>
            {children}
        </div>
    )
}

export default layout
