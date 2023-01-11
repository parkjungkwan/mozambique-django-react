import Link from "next/link"
import 'bootstrap/dist/css/bootstrap.css'
export default function Navbar(){

  return (
    <div>
      <ul>
        <li><a href="/home">홈</a></li>
        <li><a href="/counter">카운터</a></li>
        <li><a href="/todos" >할일</a></li>
        <Link href="/user/join">회원가입</Link><br/>
        <Link href="/user/login">로그인</Link>
        <li><a href="/stroke" >뇌졸증</a></li>
        <li><a href="/iris" >붓꽃</a></li>
        <li><a href="/fashion" >패션</a></li>
        <li><a href="/naver-movie" >영화크롤링</a></li>
        <li><a href="/naver-movie-review" >영화리뷰</a></li>
        <li><a href="/user-list" >사용자목록</a></li>
      </ul>
    </div>
  );
}

