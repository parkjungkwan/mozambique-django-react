import { NextPage } from "next"
import { useState } from "react"
import { LoginHome } from "@/components/user"

interface Props{ article: string }

const LoginHomePage: NextPage<Props> = ({docs}: any) => {
    const [email, setEmail] = useState("")
    return (<LoginHome email={email}/>)
}
export default LoginHomePage