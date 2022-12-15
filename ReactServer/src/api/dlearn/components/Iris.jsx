import { iris } from "../api"
import { useState } from "react"
const Iris = ()=> {
    const [inputs, setInputs] = useState({})
    const {SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm} = inputs;
    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target
        setInputs({...inputs, [name]: value})
    }
    const onClick = e =>{
        e.preventDefault()
        const request = {SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm}
        alert(`꽃잎,받침 길이/너비 : ${JSON.stringify(request)}`)
        iris(request)
        .then((res)=>{
            alert(`찾는 품종 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('꽃잎,받침 길이/너비를 다시 입력해주세요')
        })
    }
    return (
    <form method="post">
        꽃잎 폭 : <input type="text" name="PetalWidthCm" onChange={onChange} /><br/>
        꽃잎 길이 : <input type="text" name="PetalLengthCm" onChange={onChange} /><br/>
        꽃받침 폭 : <input type="text" name="SepalWidthCm" onChange={onChange} /><br/>
        꽃받침 길이 : <input type="text" name="SepalLengthCm" onChange={onChange} />
        <button onClick={onClick}> 실행 </button>
    </form>
    )
}
export default Iris