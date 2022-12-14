import { Route, Routes } from "react-router-dom"
import {Navigation, Footer} from "admin"
import {Login, SignUp, UserList} from "security"
import {Counter, Iris, Fashion, NaverMovie, Schedule, NaverMovieReview} from "basic"

const Home = () => {
    return (<>
    <table style={{ width: "1200px", height: "600px", margin: "0 auto", border: "1px solid black"}}>
        <thead style={{ height: "20%",  border: "1px solid black"}}>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%",height: "70%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/counter" element={<Counter/>}></Route>
                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/login" element={<Login/>}></Route>
                <Route path="/signup" element={<SignUp/>}></Route>
                <Route path="/iris" element={<Iris/>}></Route>
                <Route path="/fashion" element={<Fashion/>}></Route>
                <Route path="/naver-movie" element={<NaverMovie/>}></Route>
                <Route path="/naver-movie-review" element={<NaverMovieReview/>}></Route>
                <Route path="/user-list" element={<UserList/>}></Route>
            </Routes>
            </td>
        </tr>
        
        <tr style={{ width: "100%", height: "10%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}
export default Home