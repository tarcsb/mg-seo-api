
import React from 'react';
import { Container, Typography, Button } from '@mui/material';

const Dashboard = () => {
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Typography variant="body1">
        Welcome to your dashboard! Here, you can manage your SEO reports, track subscriptions, and update your profile.
      </Typography>
      <Button variant="contained" color="primary" style={{ marginTop: '20px' }}>
        Manage SEO Reports
      </Button>
    </Container>
  );
};

export default Dashboard;
