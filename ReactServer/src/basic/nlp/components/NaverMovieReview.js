import naverMovieReviewService from "../api"
import { useState } from "react"

const NaverMovieReview = ()=> {
    const [inputs, setInputs] = useState({})
    const [positive, setPositive] = useState('')
    const onChange = e => {
      e.preventDefault()
      const {value, name} = e.target
      setInputs({...inputs, [name]: value})
    }

    const onClick = e =>{
        e.preventDefault()
        naverMovieReviewService.classifyPositiveAboutReview(inputs).then(res => {
            const json = JSON.parse(res)
            setPositive(json["result"])
        })
        let arr = document.getElementsByClassName('box')
        for(let i=0; i<arr.length; i++) arr[i].value = ""
    }

    return (<>
    <h5>네이버 Imdb</h5>
    <form method="post">확인할 리뷰 : 
    <input type="text" className="box" placeholder="리뷰" name="inputs" onChange={onChange}
    />
    <button type="submit" onClick={onClick}>리뷰 긍정도 확인</button></form>
    <table>
        <thead>
            <tr>
                <th>긍정도</th>
            </tr>
        </thead>
        <tbody>
        {positive && 
            <tr ><td>{Math.floor(positive*100, 3)} %</td></tr>
        }    
        </tbody>
    </table>     
    </>)
}
export default NaverMovieReview