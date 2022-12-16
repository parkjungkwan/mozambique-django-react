import axios from "axios";
import {server, dlearn, vision} from 'context'
const dlearnService = {
    iris, getFashion, postFashion 
}
function handleResponse(response) {
    return response.text()
        .then(text =>{
            const data = text && JSON.parse(text)
            if(!response.ok){
                if(response.status === 401){
                    window.location.reload()
                }
                const error = (data && data.message) ||
                    response.statusText
                return Promise.reject(error)
            }
            return data
        })
}
async function iris(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    return fetch(`${server}${dlearn}iris`, requestOption).then(handleResponse)
}
async function getFashion(id){
    return await axios.get(`${server}${dlearn}fashion?id=${id}`)
                        .then((res)=>{
                            alert(`옷의 카테고리 : ${JSON.stringify(res.data.result)}`)
                        })
                        .catch((err)=>{
                            console.log(err)
                            alert('숫자를 다시 입력해주세요.')
                        })
} 
async function fashion(id){
    const requestOption = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(id)
    }
    return fetch(`${server}${dlearn}fashion`, requestOption).then(handleResponse)
}
export default dlearnService
