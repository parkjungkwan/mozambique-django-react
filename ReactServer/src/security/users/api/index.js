import axios from 'axios'
import {server, users} from 'context'

export const userLogin = req => {
    const url = `${server}${users}login`
    alert('url is '+url)
    axios.post(url, req)
}
