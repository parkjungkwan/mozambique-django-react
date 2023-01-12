import { context } from "@/components/admin/enums"
import axios, { AxiosResponse } from "axios"

export interface UserType{
    userid : string
    email : string
    password : string
    username : string
    phone : string
    birth : string
    address : string
    job : string
    userInterests : string
    token : string
    createAt: string
    updatedAt: string
}
export const userJoinApi =async (
    payload: {
    email : string,
    password : string,
    username : string,
    phone : string,
    birth : string,
    address : string,
    job : string,
    userInterests : string}) => {
    const headers = context.headers    
    try{
        const url = `${context.server}/users`
        alert("서버 :  ${url}")
        const response : AxiosResponse<unknown, UserType[]> = await axios.post(url, payload, {headers})
    } catch(err){

    }
}