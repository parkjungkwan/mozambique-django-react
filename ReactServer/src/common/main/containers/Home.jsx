import { Route, Routes } from "react-router-dom"
import {Navigation2, Footer} from "common"
import {Schedule} from "api"
import {LoginForm} from "security"
import image from '../images/fashion.png'
import {Counter, Iris, Fashion} from "api"
const Home = () => {
    const imageSize = {width: 700, height: 500}
    return (<>
    <table style={{ width: "1200px", height: "550px", margin: "0 auto", border: "1px solid black"}}>
        <thead>
            <tr columns="3" >
                <td style={{ width: "100%", border: "1px solid black"}}>
                    <Navigation2/>
                </td>
            </tr>
        </thead>
        <tbody>
        <tr style={{ width: "20%",height: "80%",  border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
            <Routes>
                <Route path="/counter" element={<Counter/>}></Route>
                <Route path="/todos" element={<Schedule/>}></Route>
                <Route path="/login" element={<LoginForm/>}></Route>
                <Route path="/iris" element={<Iris/>}></Route>
                <Route path="/fashion" element={<Fashion/>}></Route>
            </Routes>
            </td>
        </tr>
        <tr>
            <td>
                <img src={image} style={imageSize}/>
            </td>
        </tr>
        <tr style={{ width: "100%", height: "20%", border: "1px solid black"}}>
            <td style={{ width: "100%", border: "1px solid black"}}>
                <Footer/>
            </td>
        </tr>
        </tbody>
    </table>
    </>)
}
export default Home