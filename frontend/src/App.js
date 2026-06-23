import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import Navbar from './components/Navbar';
import Footer from './components/Footer';
import LandingPage from './pages/LandingPage';
import PropertiesPage from './pages/PropertiesPage';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/properties" element={<PropertiesPage />} />
        </Routes>

        <Footer />
      </div>
    </Router>
  );
}

export default App;