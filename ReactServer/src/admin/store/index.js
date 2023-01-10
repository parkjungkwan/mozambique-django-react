import { configureStore,
    combineReducers // redux의 Reducer 의 집합과 같다.
} from '@reduxjs/toolkit';

import todos from "basic/todos/reducers/todo.reducer"
import users from "security/users/reducers/userSlice"

const rootReducer = combineReducers({ todos, users })
export const store = configureStore({
    reducer: rootReducer
  })