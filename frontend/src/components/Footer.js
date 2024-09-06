
import React from 'react';
import { Container, Typography, Link } from '@mui/material';

const Footer = () => {
  return (
    <Container component="footer" style={{ marginTop: '50px', padding: '20px', textAlign: 'center', backgroundColor: '#f5f5f5' }}>
      <Typography variant="body2" color="textSecondary">
        © {new Date().getFullYear()} SEO Analyzer. All Rights Reserved.
      </Typography>
      <Link href="/about" color="primary">About</Link> | <Link href="/contact" color="primary">Contact</Link>
    </Container>
  );
};

export default Footer;
