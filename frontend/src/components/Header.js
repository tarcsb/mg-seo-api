import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <header className="header">
      <h1>SEO Tool</h1>
      <nav>
        <ul>
          <li><Link to="/seo-analysis">SEO Analysis</Link></li>
          <li><Link to="/competitor-analysis">Competitor Analysis</Link></li>
          <li><Link to="/help">Help</Link></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
