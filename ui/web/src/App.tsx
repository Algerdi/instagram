import React from 'react';
import { Link } from "react-router-dom";
import { Routes, Route } from 'react-router-dom';
import './App.css';
import Login from "./routes/login"
import Fishtank from "./routes/fishtank";

function App() {
  return (
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="/fishtank" element={<Fishtank />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  );
}

export default App;
