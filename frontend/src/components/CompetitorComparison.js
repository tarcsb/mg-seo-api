
import React, { useState } from 'react';
import { TextField, Button, CircularProgress, Typography, Grid, Card, CardContent } from '@mui/material';
import { Compare } from '@mui/icons-material';
import axios from 'axios';

const CompetitorComparison = () => {
  const [url, setUrl] = useState('');
  const [competitorUrl, setCompetitorUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleCompare = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/seo/analyze/competitor-comparison`,
        { url, competitorUrl },
      );
      setResult(response.data);
    } catch (err) {
      setError('Failed to perform competitor comparison.');
    }
    setLoading(false);
  };

  return (
    <Card sx={{ mt: 5, p: 3 }}>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          <Compare sx={{ mr: 1 }} /> Competitor Comparison
        </Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} md={6}>
            <TextField
              label="Your Website URL"
              fullWidth
              value={url}
              onChange={(e) => setUrl(e.target.value)}
            />
          </Grid>
          <Grid item xs={12} md={6}>
            <TextField
              label="Competitor Website URL"
              fullWidth
              value={competitorUrl}
              onChange={(e) => setCompetitorUrl(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <Button
              onClick={handleCompare}
              disabled={loading}
              fullWidth
              variant="contained"
            >
              {loading ? <CircularProgress size={24} /> : 'Compare Competitor'}
            </Button>
          </Grid>
        </Grid>

        {error && <Typography color="error" variant="body2">{error}</Typography>}
        {result && <Typography variant="body1" sx={{ mt: 3 }}>{JSON.stringify(result)}</Typography>}
      </CardContent>
    </Card>
  );
};

export default CompetitorComparison;
