import React from 'react';

export default function Logout(){
    return <button
        onClick = { e => {
            e.preventDefault()
            e.stopPropagation()
            localStorage.clear()
            
        }}> ๋ก๊ทธ์์
    </button>}

