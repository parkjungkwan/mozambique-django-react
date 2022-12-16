import { useState } from "react"
import { fashion } from "../api"
const Fashion = () => {
    const [inputs, setInputs] = useState({})
    const {id} = inputs
    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }
    const onClick = e => {
        e.preventDefault()
        alert(`사용자 이름: ${JSON.stringify(request)}`)
        fashion(id)
        .then((res)=>{
            alert(`옷의 카테고리 : ${JSON.stringify(res.data.result)}`)
        })
        .catch((err)=>{
            console.log(err)
            alert('숫자를 다시 입력해주세요.')
        })
    }
    return(<form method="get">
    <h1>FASHION</h1>
    <p>카테고리를 알고 싶은 옷의 번호를 입력해주세요.</p>
    <input type="text" placeholder="테스트할 옷 번호" name="id" onChange={onChange}/>
    <button onClick={onClick}>옷의 카테고리 찾기</button>
    </form>)
}
export default Fashion