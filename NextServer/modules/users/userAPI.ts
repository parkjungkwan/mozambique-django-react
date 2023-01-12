import axios, { AxiosResponse } from 'axios'
import {context} from '@/components/admin/enums'
import { currentTime } from '@/components/admin/utils'
export interface UserType{
    userId : string
    userEmail : string
    password : string
    userName : string
    phone : string
    birth : string
    address : string
    job : string
    userInterests : string
    token : string
    createAt: string
    updatedAt: string
}
export const joinApi = async (payload: {email: string, username: string, password: string}) => {
    try{
        const response : AxiosResponse<unknown, UserType[]> = await axios.post(`${context.server}`)
        return response.data
    }catch(err){
        console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
    }
}
