
import React from 'react'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify"
import Header from "./components/Header"
import Homepage from "./pages/HomePage"

const App = () => {
  return (
    <>
    <Router>
      <Header/>
        <main>
          <Routes>
            <Route path="/" element={<Homepage />}/> 
          </Routes>
          <ToastContainer theme="dark"/>  
        </main>  
       
    </Router>
    </>
  )
}

export default App
