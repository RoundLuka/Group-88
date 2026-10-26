import React from 'react'

export default function MyUserPage( { params } : { params: { userIds: string[] }}) {
    const userIds = params.uids   // access params property with our dynamic segment data.
    return (
        <section>
            {userIds.map((id) => {
                return (
                    <p key={id}>{id}</p>
                )
            })}
        </section>
    )
}
