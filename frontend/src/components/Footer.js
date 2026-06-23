import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="lux-footer bg-black">
      <Link to="/" className="lux-brand">RUCHI HOMES</Link>
      
      <div className="lux-nav-links">
        <Link to="/" className="lux-nav-link">Home</Link>
        <Link to="/properties" className="lux-nav-link">Properties</Link>
        <a href="#analytics" className="lux-nav-link">Analytics</a>
        <a href="#contact" className="lux-nav-link">Contact</a>
      </div>

      <div className="d-flex gap-3">
        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" className="text-white text-decoration-none">IN</a>
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="text-white text-decoration-none">TW</a>
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="text-white text-decoration-none">IG</a>
      </div>
    </footer>
  );
};

export default Footer;
