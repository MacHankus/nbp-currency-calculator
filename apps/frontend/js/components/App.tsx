import React from 'react'
import {
    Routes,
    Route,
} from "react-router-dom"
import { QueryClient, QueryClientProvider } from 'react-query'
import Form from './Form'

const queryClient = new QueryClient()




const App = () => {
    return <QueryClientProvider client={queryClient}>
        <Routes>
            <Route path="/" element={
                <Form/>
            } />
        </Routes>
    </QueryClientProvider>
}
export default App