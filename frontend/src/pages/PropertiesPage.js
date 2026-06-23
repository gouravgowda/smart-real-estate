import React, { useState, useEffect } from 'react';
import { Search, MapPin, Bed, Bath, Square, ArrowUpRight, LayoutGrid, Table } from 'lucide-react';
import { motion } from 'framer-motion';

const PropertiesPage = () => {
  const [properties, setProperties] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [type, setType] = useState('');
  const [minPrice, setMinPrice] = useState('');
  const [maxPrice, setMaxPrice] = useState('');
  const [viewMode, setViewMode] = useState('grid');

  const fetchProperties = () => {
    let queryParams = [];
    if (search) queryParams.push(`search=${search}`);
    if (type) queryParams.push(`type=${type}`);
    if (minPrice) queryParams.push(`min_price=${minPrice}`);
    if (maxPrice) queryParams.push(`max_price=${maxPrice}`);
    
    const queryString = queryParams.length > 0 ? `?${queryParams.join('&')}` : '';

    setLoading(true);
    fetch(`http://localhost:8000/api/properties/${queryString}`)
      .then(res => res.json())
      .then(data => {
        setProperties(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching data:", err);
        setLoading(false);
      });
  };

  useEffect(() => {
    fetchProperties();
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  const handleSearch = (e) => {
    if (e) e.preventDefault();
    fetchProperties();
  };

  return (
    <motion.div 
      initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.8 }}
      className="container properties-page"
    >
      <h1 className="mb-4 serif">Property Showcase</h1>
      <p className="text-muted mb-5">Explore our exclusive collection of premium real estate.</p>

      <div className="glass-panel search-box-lux">
        <form onSubmit={handleSearch}>
          <div className="row g-3">
            <div className="col-12 col-md-4">
              <div className="input-group h-100">
                <span className="input-group-text bg-transparent border-end-0 border-secondary"><MapPin size={18} className="text-muted" /></span>
                <input type="text" className="form-control bg-transparent text-white border-start-0 border-secondary" placeholder="Search by location..." value={search} onChange={(e) => setSearch(e.target.value)} />
              </div>
            </div>
            <div className="col-md-3">
              <select className="form-select bg-dark text-white border-secondary h-100" value={type} onChange={(e) => setType(e.target.value)}>
                <option value="">Any Type</option>
                <option value="apartment">Apartment</option>
                <option value="villa">Villa</option>
                <option value="house">House</option>
                <option value="commercial">Commercial</option>
              </select>
            </div>
            <div className="col-md-3">
              <input type="number" className="form-control bg-transparent text-white border-secondary h-100" placeholder="Min Price (₹)" value={minPrice} onChange={(e) => setMinPrice(e.target.value)} />
            </div>
            <div className="col-md-2">
              <button type="submit" className="btn-pill-outline w-100 h-100 d-flex align-items-center justify-content-center">
                <Search size={18} className="me-2" /> Search
              </button>
            </div>
          </div>
        </form>
      </div>

      <div className="view-toggle-btns">
        <button 
          className={`btn-toggle-lux ${viewMode === 'grid' ? 'active' : ''}`} 
          onClick={() => setViewMode('grid')}
          title="Grid View"
        >
          <LayoutGrid size={16} /> Grid
        </button>
        <button 
          className={`btn-toggle-lux ${viewMode === 'table' ? 'active' : ''}`} 
          onClick={() => setViewMode('table')}
          title="Table View"
        >
          <Table size={16} /> Table
        </button>
      </div>

      {loading ? (
        <div className="text-center py-5">
          <div className="spinner-border text-gold mb-3" role="status"></div>
          <h4 className="text-muted">Loading exceptional properties...</h4>
        </div>
      ) : properties.length === 0 ? (
        <div className="text-center py-5">
          <h4 className="text-muted">No properties found matching your criteria.</h4>
          <button className="btn-pill-outline mt-3" onClick={() => {setSearch(''); setType(''); setMinPrice(''); setMaxPrice(''); setTimeout(handleSearch, 0);}}>Clear Filters</button>
        </div>
      ) : viewMode === 'grid' ? (
        <div className="row g-4 mt-2 mb-5">
          {properties.map((property, index) => (
            <motion.div 
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3, delay: Math.min(index * 0.05, 0.5) }}
              className="col-md-6 col-lg-4" key={property.id}
            >
              <div className="glass-panel property-card-lux h-100">
                <img src={property.image_url || "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format,compress&w=800&q=80"} alt={property.title} loading="lazy" />
                <div className="card-body">
                  <h5 className="property-title text-truncate mb-2 serif" title={property.title}>{property.title}</h5>
                  <p className="property-location d-flex align-items-center text-muted small mb-3">
                    <MapPin size={14} className="me-1" /> {property.location}
                  </p>
                  
                  <div className="d-flex justify-content-between text-muted small mb-4">
                    <div title="Bedrooms"><Bed size={16} className="text-gold" /> {property.bedrooms}</div>
                    <div title="Bathrooms"><Bath size={16} className="text-gold" /> {property.bathrooms}</div>
                    <div title="Square Feet"><Square size={16} className="text-gold" /> {property.area_sqft} sqft</div>
                  </div>
                  
                  <div className="d-flex justify-content-between align-items-center mt-auto">
                    <div className="fs-5 text-gold">{new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(property.price)}</div>
                    <button className="btn btn-link text-white p-0">
                      <ArrowUpRight size={24} />
                    </button>
                  </div>
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      ) : (
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
          className="lux-table-container mb-5"
        >
          <table className="lux-table">
            <thead>
              <tr>
                <th>Preview</th>
                <th>Title</th>
                <th>Type</th>
                <th>Price</th>
                <th>Location</th>
                <th>Beds</th>
                <th>Baths</th>
                <th>Area</th>
              </tr>
            </thead>
            <tbody>
              {properties.map((property) => (
                <tr key={property.id}>
                  <td>
                    <img 
                      className="lux-table-img" 
                      src={property.image_url || "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format,compress&w=800&q=80"} 
                      alt={property.title} 
                    />
                  </td>
                  <td className="serif fw-bold text-white">{property.title}</td>
                  <td className="text-capitalize text-gold">{property.property_type}</td>
                  <td className="text-gold fw-semibold">
                    {new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR', maximumFractionDigits: 0 }).format(property.price)}
                  </td>
                  <td>{property.location}</td>
                  <td>{property.bedrooms}</td>
                  <td>{property.bathrooms}</td>
                  <td>{property.area_sqft} sqft</td>
                </tr>
              ))}
            </tbody>
          </table>
        </motion.div>
      )}
    </motion.div>
  );
};

export default PropertiesPage;
