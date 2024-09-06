
import React from 'react';
import { Container, Typography, Button, Grid } from '@mui/material';
import { useHistory } from 'react-router-dom';

const HeroSection = () => {
  const history = useHistory();

  return (
    <Container style={{ padding: '100px 0', textAlign: 'center' }}>
      <Typography variant="h2" gutterBottom>
        Boost Your Website's SEO Performance
      </Typography>
      <Typography variant="h6" paragraph>
        Get real-time insights to enhance your SEO rankings, track competitors, and dominate search engines.
      </Typography>
      <Grid container spacing={3} justifyContent="center">
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={() => history.push('/subscribe')}
            style={{ marginTop: '20px' }}
          >
            Start Free Trial
          </Button>
        </Grid>
        <Grid item>
          <Button
            variant="outlined"
            color="secondary"
            size="large"
            onClick={() => history.push('/signon')}
            style={{ marginTop: '20px' }}
          >
            Login / Sign Up
          </Button>
        </Grid>
      </Grid>
    </Container>
  );
};

export default HeroSection;
