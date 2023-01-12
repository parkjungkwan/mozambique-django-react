import axios, { AxiosResponse } from 'axios'
import {context} from '@/components/admin/enums'
import { currentTime } from '@/components/admin/utils'
import { User } from '@/modules/types'
import { accessClient, client } from "@/modules/controllers"

export const user = {
    join: async (payload: { 
        userid? : string,
        email : string,
        password : string,
        username : string,
        phone? : string,
        birth? : string,
        address? : string,
        job? : string,
        userInterests? : string,
        createdAt? : string,
        updatedAt? : string}) => {
            try{
                const response : AxiosResponse<unknown, User[]> = await axios.post(`${context.server}/users`)
                return response.data
            }catch(err){
                console.log(` ${currentTime} : userSaga 내부에서 join 실패 `)
            }
        },
        login: async (payload: User) => {
            try{
                const response : AxiosResponse<any, User[]> =
                await accessClient.post('/users/login', payload)
                return response.data
            }catch(err){
                return err;
            }
        },
        logout: async() => {
            try{
                await client.post('/users/logout')
            } catch(err){
                console.log(err)
                return err;
            }
        },
        userInfo: async () => {
            try{
                const response : AxiosResponse = await client.get(`/users/join`)
                return response.data
            } catch(err) {
                console.log(err)
                return err
            }
        }
    
}
