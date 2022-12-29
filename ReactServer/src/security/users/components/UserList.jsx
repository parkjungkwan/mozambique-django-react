import '../styles/Login.css'
import {useState, useEffect} from 'react'
import axios from 'axios'
export default function UserList(){
    const [list, setList] = useState([])
    useEffect(()=>{
        axios
        .get('http://localhost:8000/security/users/user-list')
        .then(res => {
            console.log(" 회원목록 들어옴 ")
            console.log(res.data)
            setList(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }, [])
    return <>
    
    </>
}


