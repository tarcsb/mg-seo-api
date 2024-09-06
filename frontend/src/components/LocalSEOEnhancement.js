
import React, { useState } from 'react';
import { TextField, Button, CircularProgress, Typography, Grid, Card, CardContent } from '@mui/material';
import { LocationOn } from '@mui/icons-material';
import axios from 'axios';

const LocalSEOEnhancement = () => {
  const [url, setUrl] = useState('');
  const [location, setLocation] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleEnhance = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/seo/analyze/local-seo`,
        { url, location },
      );
      setResult(response.data);
    } catch (err) {
      setError('Failed to enhance local SEO.');
    }
    setLoading(false);
  };

  return (
    <Card sx={{ mt: 5, p: 3 }}>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          <LocationOn sx={{ mr: 1 }} /> Local SEO Enhancement
        </Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} md={6}>
            <TextField
              label="Website URL"
              fullWidth
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
          </Grid>
          <Grid item xs={12} md={6}>
            <TextField
              label="Location"
              fullWidth
              value={location}
              onChange={(e) => setLocation(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <Button
              onClick={handleEnhance}
              disabled={loading}
              fullWidth
              variant="contained"
            >
              {loading ? <CircularProgress size={24} /> : 'Enhance Local SEO'}
            </Button>
          </Grid>
        </Grid>

        {error && <Typography color="error" variant="body2">{error}</Typography>}
        {result && <Typography variant="body1" sx={{ mt: 3 }}>{JSON.stringify(result)}</Typography>}
      </CardContent>
    </Card>
  );
};

export default LocalSEOEnhancement;
