import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Shield, Home, TrendingUp, Users, DollarSign, BrainCircuit, MapPin } from 'lucide-react';
import { Link } from 'react-router-dom';

const fadeIn = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] } }
};

const staggerContainer = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { staggerChildren: 0.1 } }
};

const LandingPage = () => {
  const [properties, setProperties] = useState([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [company, setCompany] = useState("");
  const [message, setMessage] = useState("");



  useEffect(() => {
    fetch('http://localhost:8000/api/properties/')
      .then(res => res.json())
      .then(data => setProperties(data))
      .catch(err => console.error("Error fetching properties:", err));
  }, []);

  const heroProperties = properties.slice(0, 3);
  const showcaseProperties = properties.slice(3, 7);
  const handleSubmit = async (e) => {
    e.preventDefault();

    // 1. Name Validation (Only letters, spaces, hyphens, and apostrophes)
    const nameRegex = /^[a-zA-Z\s'-]+$/;
    if (!nameRegex.test(name.trim())) {
      alert("Name should only contain letters and spaces.");
      return;
    }

    // 2. Email Validation (Requires valid username, @, domain name, and extension like .com)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email.trim())) {
      alert("Please enter a valid email address (e.g., example@domain.com).");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/contact/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: name.trim(),
          email: email.trim(),
          company: company.trim(),
          message: message.trim(),
        }),
      });

      const data = await response.json();
      if (response.ok) {
        alert(data.message);
        setName("");
        setEmail("");
        setCompany("");
        setMessage("");
      } else {
        alert(data.error || "Something went wrong.");
      }
    } catch (err) {
      console.error("Submission error:", err);
      alert("Failed to submit request. Please try again later.");
    }
  };

  return (
    <div className="landing-wrapper">
      
      {/* HERO SECTION */}
      <section className="hero-section" id="home">
        <motion.img 
          initial={{ scale: 1.1 }}
          animate={{ scale: 1 }}
          transition={{ duration: 5, ease: "easeOut" }}
          src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?q=80&w=2000" 
          alt="Luxury Villa" 
          className="hero-bg"
        />
        
        <div className="hero-text-container">
          <motion.h1 
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 1, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
            className="hero-title"
          >
            RUCHI HOMES
          </motion.h1>
        </div>

        <div className="hero-content-overlay">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.3 }}
            className="text-center"
          >
            <p className="hero-subtitle text-uppercase letter-spacing-2 mb-2">AI-powered luxury property intelligence</p>
            <h2 className="hero-tagline serif">Calm control for exceptional estates.</h2>
          </motion.div>
        </div>

        <motion.div 
          className="floating-cards-container"
          variants={staggerContainer}
          initial="hidden"
          animate="visible"
        >
          {heroProperties.map((prop, i) => (
            <motion.div key={prop.id} variants={fadeIn} className="glass-panel floating-card">
              <img src={prop.image_url || `https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format,compress&w=400&q=80`} alt={prop.title} loading="lazy" />
              <p className="floating-card-title text-truncate" title={prop.title}>{prop.title}</p>
              <p className="floating-card-subtitle d-flex justify-content-between">
                <span>{prop.location}</span>
                <span className="text-gold">{new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(prop.price)}</span>
              </p>
            </motion.div>
          ))}
        </motion.div>
      </section>

      {/* SECTION 01: EXPERIENCE */}
      <section className="experience-section bg-cream">
        <motion.div 
          initial="hidden" whileInView="visible" viewport={{ once: true, margin: "-100px" }}
          variants={fadeIn}
        >
          <h2 className="section-heading-large serif">EXPERIENCE EXCELLENCE IN REAL ESTATE</h2>
          
          <div className="experience-grid">
            <div>
              <p className="experience-text">
                Redefining modern living through smart property management and AI-powered analytics. 
                We handle luxury properties with an editorial touch, ensuring your assets are managed, 
                tracked, and optimized with cutting-edge rental automation and unparalleled client care.
              </p>
              <Link to="/properties" className="btn-pill-outline mt-4 d-inline-block text-dark border-dark">Explore Showcase</Link>
            </div>
            
            <motion.div className="image-collage" variants={staggerContainer}>
              <motion.img variants={fadeIn} src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format,compress&w=800" className="collage-img" alt="Interior" loading="lazy" />
              <motion.img variants={fadeIn} src="https://images.unsplash.com/photo-1600607686527-6fb886090705?auto=format,compress&w=800" className="collage-img" alt="Exterior" loading="lazy" />
              <motion.img variants={fadeIn} src="https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format,compress&w=1200" className="collage-img large" alt="Architecture" loading="lazy" />
            </motion.div>
          </div>
        </motion.div>
      </section>

      {/* SECTION 02: FEATURES */}
      <section className="features-section bg-black" id="analytics">
        <motion.div initial="hidden" whileInView="visible" viewport={{ once: true }} variants={fadeIn}>
          <h2 className="section-heading-large serif text-center">SMART REAL ESTATE MANAGEMENT</h2>
          
          <motion.div className="features-grid" variants={staggerContainer}>
            {[
              { icon: <Home size={32} />, title: "Property Management", desc: "End-to-end luxury asset management." },
              { icon: <TrendingUp size={32} />, title: "Smart Analytics", desc: "Real-time market valuation and trends." },
              { icon: <Users size={32} />, title: "Client Management", desc: "White-glove service for premium clients." },
              { icon: <Shield size={32} />, title: "Rental Tracking", desc: "Automated collection and lease execution." },
              { icon: <DollarSign size={32} />, title: "Payment Monitoring", desc: "Secure multi-currency transactions." },
              { icon: <BrainCircuit size={32} />, title: "AI Insights", desc: "Predictive modeling for ROI optimization." }
            ].map((feat, i) => (
              <motion.div key={i} variants={fadeIn} className="glass-panel feature-card">
                <div className="feature-icon">{feat.icon}</div>
                <h4 className="serif mb-0">{feat.title}</h4>
                <p className="text-muted small mb-0">{feat.desc}</p>
              </motion.div>
            ))}
          </motion.div>
        </motion.div>
      </section>

      {/* SECTION 03: PROPERTY SHOWCASE */}
      {showcaseProperties.length > 0 && (
        <section className="showcase-section bg-black text-white" id="properties">
          <motion.div initial="hidden" whileInView="visible" viewport={{ once: true, margin: "-100px" }} variants={fadeIn}>
            <div className="text-center mb-5 pb-4">
              <h2 className="section-heading-large serif mb-3">EDITORIAL HOMES WITH INTELLIGENT OPERATIONS</h2>
              <p className="text-muted mx-auto" style={{ maxWidth: '700px' }}>
                Each asset is presented with its own operational narrative, from owner reporting to tenant intelligence and AI-led valuation.
              </p>
            </div>
            
            <div className="container px-4">
              {showcaseProperties.map((prop, idx) => {
                const isEven = idx % 2 === 0;
                return (
                  <motion.div 
                    key={prop.id}
                    variants={fadeIn}
                    className={`row align-items-center mb-5 pb-5 ${isEven ? '' : 'flex-row-reverse'}`}
                  >
                    <div className="col-md-7 mb-4 mb-md-0">
                      <div className="showcase-img-wrapper">
                        <img src={prop.image_url || `https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format,compress&w=1200`} alt={prop.title} className="showcase-img" loading="lazy" />
                      </div>
                    </div>
                    <div className={`col-md-5 ${isEven ? 'ps-md-5' : 'pe-md-5'}`}>
                      <p className="text-muted small text-uppercase letter-spacing-2 mb-2 d-flex align-items-center">
                        <MapPin size={14} className="me-2" /> {prop.location}
                      </p>
                      <h3 className="serif display-6 mb-3">{prop.title}</h3>
                      <h4 className="text-gold mb-4">{new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(prop.price)}</h4>
                      <p className="text-muted mb-4 line-height-lg">
                        A beautifully curated {prop.property_type} residence featuring {prop.bedrooms} bedrooms, {prop.bathrooms} bathrooms, and spanning {prop.area_sqft} sqft. Managed with predictive maintenance and private owner reporting.
                      </p>
                      <Link to="/properties" className="btn-pill-outline text-white border-white">View Details</Link>
                    </div>
                  </motion.div>
                );
              })}
            </div>
            
            <div className="text-center mt-4">
              <Link to="/properties" className="btn-pill-outline">View All Listings</Link>
            </div>
          </motion.div>
        </section>
      )}

      {/* SECTION 05: CONTACT */}
<section className="contact-section" id="contact">
  <img
    src="https://images.unsplash.com/photo-1600607687644-aac4c3eac7f4?auto=format&fit=crop&w=2000&q=80"
    alt="Night Architecture"
    className="contact-bg"
    loading="lazy"
  />

  <motion.div
    initial="hidden"
    whileInView="visible"
    viewport={{ once: true }}
    variants={fadeIn}
    className="glass-panel contact-panel"
  >
    <h2 className="serif mb-3">
      Ready to Transform Real Estate Management?
    </h2>

    <p className="text-muted">
      Book a free consultation or request a live demo.
    </p>

    <form className="contact-form" onSubmit={handleSubmit}>
      
      <input
        type="text"
        placeholder="Name"
        className="lux-input"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />

      <input
        type="email"
        placeholder="Email"
        className="lux-input"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <input
        type="text"
        placeholder="Company"
        className="lux-input"
        value={company}
        onChange={(e) => setCompany(e.target.value)}
      />

      <textarea
        placeholder="Message"
        className="lux-input"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        required
      ></textarea>

      <button type="submit" className="btn-submit">
        Submit Request
      </button>

    </form>
  </motion.div>
</section>
</div> ); }; export default LandingPage;