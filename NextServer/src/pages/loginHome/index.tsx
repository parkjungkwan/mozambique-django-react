import { NextPage } from "next"
import { useState, useEffect } from "react"
import { LoginHome } from "@/components/user"

interface Props{ article: string }

const LoginHomePage: NextPage<Props> = ({docs}: any) => {
    const [loginUser, setLoginUser] = useState({user_emai:''})
    useEffect(() => {
        // 브라우저 API를 이용하여 문서 타이틀을 업데이트합니다.
        const s = localStorage.getItem('loginUser') ;
        alert("결과: "+JSON.stringify(s))
        
      },);

    return (<div>로그인 정보 : </div>)
}
export default LoginHomePage