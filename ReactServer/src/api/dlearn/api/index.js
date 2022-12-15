import axios from "axios";
import {server, dlearn, vision} from 'context'
export const iris = req => axios.post(`${server}${dlearn}iris`, req)
export const fakeFaces = req => axios.get(`${server}${vision}fake-faces`, req)