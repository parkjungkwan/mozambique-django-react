import axios from "axios";
import {useState, useEffect} from "react"
import Pagination from "./admin/Pagination";



export default function Home(){

   const [list, setList] = useState([])
   const [rowCnt, setRowCnt] = useState(0)
   const [requestPage, setRequestPage] = useState(0)
   const [startRowPerPage, setStartRowPerPage] = useState(0)
   const [endRowPerPage, setEndRowPerPage] = useState(0)
   const [startPagePerBlock, setStartPagePerBlock] = useState(0)
   const [endPagePerBlock, setEndPagePerBlock] = useState(0)
   const [rows, setRows] = useState<Number[]>([])
   const [pages, setPages] = useState<Number[]>([])

    useEffect(()=>{
        axios
        .get('http://localhost:8000/users/page/22')
        .then(res => {
            setRowCnt(Number(res.data.pager.row_cnt))
            setStartRowPerPage(Number(res.data.pager.start_row_per_page))
            setEndRowPerPage(Number(res.data.pager.end_row_per_page))
            setStartPagePerBlock(Number(res.data.pager.start_page_per_block))
            setEndPagePerBlock(Number(res.data.pager.end_page_per_block))
            setRequestPage(Number(res.data.pager.request_page))
            setList(res.data.users.items)
            console.log(" ### 페이지 내용 표시 ### ")
            let rows:Number[] = []
            let pages:Number[] = []
            for(let i =startRowPerPage; i <= endRowPerPage; i++){
                rows.push(i)
            }
            setRows(rows)
            console.log(" ### 블록 내용 표시 ### ")
            for(let i =startPagePerBlock; i <= endPagePerBlock; i++){
              pages.push(i)
           }
           setPages(pages)
          console.log(` 사용자가 요청한 페이지 번호: ${requestPage}`)
        })
        .catch(err => {console.log(err)})
    }, [])

  return (
    <>
    <h2>회원목록 </h2>
    <h6>회원수: {rowCnt}</h6>
    <h6></h6>
    <h6></h6>
    <h6></h6>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>비번</th><th>이름</th><th>전화번호</th>
                <th>생년월일</th><th>주소</th><th>직업</th><th>관심사항</th>
                </tr>
            </thead>
            <tbody>
            {list && list.map(({userid, email, password, username, phone, birth, address, job, interests})=>(
                <tr key={userid}>
                    <td>{userid}</td><td>{email}</td><td>{password}</td><td>{username}</td>
                    <td>{phone}</td><td>{birth}</td><td>{address}</td>
                    <td>{job}</td><td>{interests}</td>
                </tr>
            ))}
            </tbody>
        </table>
        <div>
          {rows && rows.map((idx) => (<span style={{"border": "1px solid black"}} >{idx+1}</span>))}
        </div>
        <div className="page-container">
    </div>
    </>
    
  );
}