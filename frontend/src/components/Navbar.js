import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="lux-navbar">
      <Link to="/" className="lux-brand">RUCHI HOMES</Link>
      
      <div className="lux-nav-links">
        <a href="/#home" className="lux-nav-link">Home</a>
        <Link to="/properties" className="lux-nav-link">Properties</Link>
        <a href="/#analytics" className="lux-nav-link">Analytics</a>
        <a href="/#contact" className="lux-nav-link">Contact</a>
      </div>

      <a href="/#contact" className="btn-pill-outline">Get Started</a>
    </nav>
  );
};

export default Navbar;
