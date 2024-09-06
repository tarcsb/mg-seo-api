import React from 'react';
import { Container, Typography, Button, Grid, Card, CardContent, TextField, Box } from '@mui/material';
import { useState } from 'react';

const LandingPage = () => {
  const [isLogin, setIsLogin] = useState(true);

  const toggleAuthMode = () => {
    setIsLogin(!isLogin);
  };

  return (
    <Container maxWidth="lg" sx={{ textAlign: 'center', marginTop: '50px' }}>
      {/* Header */}
      <Typography variant="h2" gutterBottom>
        Elevate Your SEO with AI-Powered Optimization
      </Typography>
      <Typography variant="h5" color="textSecondary" paragraph>
        Boost your website rankings, get actionable insights, and manage your SEO strategy easily with our AI-powered tools.
      </Typography>

      {/* Call to Action */}
      <Button variant="contained" color="primary" size="large" sx={{ marginBottom: '40px' }}>
        Start Your Free Trial
      </Button>

      {/* Features Section */}
      <Grid container spacing={4} justifyContent="center">
        <Grid item xs={12} md={4}>
          <Card sx={{ backgroundColor: '#f5f5f5' }}>
            <CardContent>
              <Typography variant="h5" component="div">
                AI-Powered Analysis
              </Typography>
              <Typography variant="body2" color="textSecondary">
                Get real-time SEO recommendations powered by AI.
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card sx={{ backgroundColor: '#f5f5f5' }}>
            <CardContent>
              <Typography variant="h5" component="div">
                SEO Performance Tracking
              </Typography>
              <Typography variant="body2" color="textSecondary">
                Monitor your site's SEO performance with detailed analytics.
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card sx={{ backgroundColor: '#f5f5f5' }}>
            <CardContent>
              <Typography variant="h5" component="div">
                Upgrade to Pro
              </Typography>
              <Typography variant="body2" color="textSecondary">
                Unlock premium features and accelerate your results.
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Auth Section */}
      <Box sx={{ marginTop: '60px' }}>
        <Typography variant="h4" gutterBottom>
          {isLogin ? 'Login to Your Account' : 'Register for Free'}
        </Typography>
        <AuthForm isLogin={isLogin} toggleAuthMode={toggleAuthMode} />
      </Box>
    </Container>
  );
};

const AuthForm = ({ isLogin, toggleAuthMode }) => {
  return (
    <form>
      <TextField
        label="Email"
        variant="outlined"
        fullWidth
        margin="normal"
      />
      <TextField
        label="Password"
        type="password"
        variant="outlined"
        fullWidth
        margin="normal"
      />
      {!isLogin && (
        <TextField
          label="Confirm Password"
          type="password"
          variant="outlined"
          fullWidth
          margin="normal"
        />
      )}
      <Button variant="contained" color="primary" fullWidth sx={{ marginTop: '20px' }}>
        {isLogin ? 'Login' : 'Register'}
      </Button>
      <Button onClick={toggleAuthMode} fullWidth sx={{ marginTop: '10px' }}>
        {isLogin ? 'Don't have an account? Register' : 'Already have an account? Login'}
      </Button>
    </form>
  );
};

export default LandingPage;
