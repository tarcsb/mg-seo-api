
import React, { useState } from 'react';
import { Container, TextField, Button, Typography } from '@mui/material';

const SignOn = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isSigningIn, setIsSigningIn] = useState(true);

  const handleSubmit = () => {
    // Handle sign-in or sign-up logic
    if (isSigningIn) {
      console.log('Signing in with:', email, password);
    } else {
      console.log('Signing up with:', email, password);
    }
  };

  return (
    <Container style={{ marginTop: '50px' }}>
      <Typography variant="h4" gutterBottom>
        {isSigningIn ? 'Sign In' : 'Sign Up'}
      </Typography>
      <TextField
        label="Email"
        fullWidth
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        margin="normal"
      />
      <TextField
        label="Password"
        type="password"
        fullWidth
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        margin="normal"
      />
      <Button variant="contained" color="primary" fullWidth onClick={handleSubmit}>
        {isSigningIn ? 'Sign In' : 'Sign Up'}
      </Button>
      <Button
        color="secondary"
        fullWidth
        onClick={() => setIsSigningIn(!isSigningIn)}
        style={{ marginTop: '20px' }}
      >
        {isSigningIn ? 'Create an account' : 'Already have an account? Sign In'}
      </Button>
    </Container>
  );
};

export default SignOn;
