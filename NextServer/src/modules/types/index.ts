import { ReactNode } from "react";

export interface onProps{
    onSubmit: (e : React.FormEvent<HTMLFormElement>) => void
    onChange: (e : React.ChangeEvent<HTMLInputElement> ) => void
}

export interface Layout {
    children?: ReactNode
}

export interface User{
    userid? : string,
    email : string,
    password : string,
    cpassword?: string, 
    username : string,
    phone? : string,
    birth? : string,
    address? : string,
    job? : string,
    userInterests? : string,
    createdAt? : string,
    updatedAt? : string
}
export interface Article{
    art_seq? : number
    title : string
    content : string
    create_at? : string
    updated_at? : string
    user_id : string
}