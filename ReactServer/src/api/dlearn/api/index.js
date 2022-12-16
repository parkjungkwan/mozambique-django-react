import axios from "axios";
import {server, dlearn, vision} from 'context'
export const iris = req => axios.post(`${server}${dlearn}iris`, req)
export const getFashion = id => axios.get(`${server}${dlearn}fashion?id=${id}`)
export const postFashion = id => axios.post(`${server}${dlearn}fashion?id=${id}`)
