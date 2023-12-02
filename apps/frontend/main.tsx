import React from 'react'
import * as ReactDOM from 'react-dom'
import "./css/index.scss"
import {
    BrowserRouter
} from "react-router-dom"
import App from './js/components/App'

const root = ReactDOM.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>,
    document.getElementById("root")
);