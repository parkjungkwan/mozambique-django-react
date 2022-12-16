import axios from "axios";
import {server, dlearn, vision} from 'context'
export const iris = req => axios.post(`${server}${dlearn}iris`, req)
export const fashion = id => axios.get(`${server}${dlearn}fashion?id=${id}`)
