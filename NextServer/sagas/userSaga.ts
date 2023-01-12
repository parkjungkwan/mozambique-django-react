import { PayloadAction } from "@reduxjs/toolkit"
import { call, delay, put, takeLatest } from "redux-saga/effects"
import { string } from 'yup'
import userActions from '@/modules/users'
// api 

interface UserJoinType{
    type: string,
    payload: {
        userEmail: string, password: string, userName: string
    }
}
