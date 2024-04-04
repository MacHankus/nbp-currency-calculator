import React from 'react'
import './css/index.scss'
import {
  BrowserRouter
} from 'react-router-dom'
import App from './js/components/App'
import { createRoot } from 'react-dom/client'

const container = document.getElementById('root')
const root = createRoot(container  as Element)
root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
)
