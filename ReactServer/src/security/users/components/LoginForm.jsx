import '../styles/Login.css'
import { useState } from "react"
import { userLogin } from '../api'

export default function LoginForm(){
    const [inputs, setInputs] = useState({})
    const {user_email, password} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        const request = {user_email, password}
        alert(`사용자 이름: ${JSON.stringify(request)}`)
        userLogin(request)
        .then((res)=>{
            alert(`Response is ${JSON.stringify(res.data)}`)
            
        })
        .catch((err)=>{
            console.log(err)
            alert('아이디와 비밀번호를 다시')
        })

    }

    return (
    <>
        EMAIL: <input type="text" name="user_email" onChange={onChange} /><br/>
        PASSWORD: <input type="text" name="password" onChange={onChange} /><br/>
        <button onClick={onClick}> 로그인 </button>

    
    </>
)}
