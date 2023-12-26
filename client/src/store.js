import { applyMiddleware, createStore } from "redux" 
import { composewithDevTools } from "redux-devtools-extension"
import reduxThunk from "redux-thunk"
import rootReducer from "./reducers";

const initialState ={}

const middleware=[reduxThunk]

const store =createStore(
    rootReducer,
    initialState,
    composewithDevTools(applyMiddleware(...middleware))
)