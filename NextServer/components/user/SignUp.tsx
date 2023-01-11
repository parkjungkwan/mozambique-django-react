import '../styles/SignUp.css'
import { useState } from "react"


export default function SignUp() {
    const [inputs, setInputs] = useState({})

    const validateFormWithJS = () => {
        // const name = document.querySelector('#name').value
        // const rollNumber = document.querySelector('#rollNumber').value
        const name = ""
        const rollNumber = ""
        if (!name) {
          alert('Please enter your name.')
          return false
        }
    
        if (rollNumber.length < 3) {
          alert('Roll Number should be at least 3 digits long.')
          return false
        }
      }


   
    return (<>
        <h2>회원가입</h2>
            <form action="/send-data-here" method="post">
                <label htmlFor="first">User Email:</label>
                <input type="text" id="user_email" name="user_email" />
                <label htmlFor="last">Password:</label>
                <input type="text" id="password" name="password" />
                <button type="submit">Submit</button>
            </form>
        </>)
}
