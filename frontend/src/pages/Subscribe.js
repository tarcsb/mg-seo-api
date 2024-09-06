
import React, { useState } from 'react';
import { Button, Typography, Container, Grid, Card, CardContent, CircularProgress } from '@mui/material';
import axios from 'axios';

const Subscribe = () => {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');

  const handleSubscribe = async (plan) => {
    setLoading(true);
    setMessage('');
    try {
      const response = await axios.post('/payments/create-payment-intent', { plan });
      const { clientSecret } = response.data;
      // Continue with Stripe payment flow
      setMessage('Payment intent created. Please complete the payment.');
    } catch (error) {
      setMessage('Failed to create payment intent.');
    }
    setLoading(false);
  };

  return (
    <Container style={{ marginTop: '50px' }}>
      <Typography variant="h4" gutterBottom>
        Choose Your Plan
      </Typography>
      <Grid container spacing={4}>
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Basic Plan - $10</Typography>
              <Button variant="contained" color="primary" fullWidth onClick={() => handleSubscribe('basic')}>
                {loading ? <CircularProgress size={24} /> : 'Subscribe'}
              </Button>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Premium Plan - $20</Typography>
              <Button variant="contained" color="primary" fullWidth onClick={() => handleSubscribe('premium')}>
                {loading ? <CircularProgress size={24} /> : 'Subscribe'}
              </Button>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
      {message && <Typography color="error" style={{ marginTop: '20px' }}>{message}</Typography>}
    </Container>
  );
};

export default Subscribe;
