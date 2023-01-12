import axios, { AxiosResponse } from 'axios'
import {Config} from '@/components/admin/enums'
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
export const joinApi = async (payload: {userEmail: string, userName: string, password: string}) => {
    try{
        const response : AxiosResponse<unknown, UserType[]> = await axios.post(`${Config.server}`)
        return response.data
    }catch(err){
        return err
    }
}
