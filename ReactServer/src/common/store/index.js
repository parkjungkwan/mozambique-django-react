import { combineReducers} from "@reduxjs/toolkit"
import todoReducer from "common/reducers/todo.reducer"

export default combineReducers({
    todos: todoReducer
})
