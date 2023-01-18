import Link from "next/link"
import 'bootstrap/dist/css/bootstrap.css'
import { useDispatch } from "react-redux"
import { logoutRequest } from "@/modules/slices"
import {useAppDispatch, useAppSelector} from '@/hooks'
export default function Navbar(){
    const dispatch = useAppDispatch()

    const logout = (e : React.FormEvent<HTMLInputElement> )=>{
        e.preventDefault()
        alert(`1 로그아웃 버튼 클릭`)
        const token = localStorage.getItem("session")
        alert(`Navbar 에 저장된 토큰 ${token}`)
        dispatch(logoutRequest({"token":token}))
    }

  return (
    <div className="container-fluid">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <ul className="navbar-nav me-auto mb-2 mb-lg-0">
        <li className="nav-item"><Link href="/">홈</Link></li><span style={{width:10}}/>
        <li className="nav-item"><Link href="/counter">카운터</Link></li><span style={{width:10}}/>
        <li className="nav-item"><Link href="/user/list" >사용자목록</Link></li><span style={{width:10}}/>
        <li className="nav-item"><Link href="/article/write">글쓰기</Link></li><span style={{width:10}}/>
        
      </ul>
      <input type="button" id="logout" value="로그아웃" onClick={logout}/>
      </nav>
    </div>
  );
}

