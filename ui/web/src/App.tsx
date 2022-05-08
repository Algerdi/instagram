import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import Login from "./routes/login"
import Fishtank from "./routes/fishtank";
import Register from "./routes/register";

function App() {
  return (
  <Routes>
    <Route path="/" element={<App />} />
    <Route path="/fishtank" element={<Fishtank />} />
    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />}/>
  </Routes>
  );
}

export default App;
