import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import SEOAnalysis from './components/SEOAnalysis';
import CompetitorAnalysis from './components/CompetitorAnalysis';
import HelpSection from './components/HelpSection';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <Switch>
          <Route path="/seo-analysis" component={SEOAnalysis} />
          <Route path="/competitor-analysis" component={CompetitorAnalysis} />
          <Route path="/help" component={HelpSection} />
          <Route path="/" component={SEOAnalysis} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
