import axios from 'axios'
import {server, users} from 'context'

export const userLogin = req =>axios.post(`${server}${users}login`, req)