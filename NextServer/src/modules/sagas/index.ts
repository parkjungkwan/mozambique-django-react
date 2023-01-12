import { all, fork } from "redux-saga/effects"
import{
    watchJoin
} from "./user.saga"

export default function* rootSaga(){
    yield all([ fork(watchJoin) ])
}