import { combineReducers} from "@reduxjs/toolkit"
import todoReducer from "basic/todos/reducers/todo.reducer"

export default combineReducers({
    todos: todoReducer
})
