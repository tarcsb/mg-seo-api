import React, { useState } from 'react';
import { Container, Grid, Card, CardContent, Typography, Button, CircularProgress, Snackbar } from '@mui/material';
import { getSEOAnalysis, getCompetitorAnalysis } from '../services/api';

function Dashboard() {
  const [loading, setLoading] = useState(false);
  const [seoData, setSeoData] = useState(null);
  const [competitorData, setCompetitorData] = useState(null);
  const [error, setError] = useState('');

  const handleSEOAnalysis = async () => {
    setLoading(true);
    try {
      const data = await getSEOAnalysis('https://example.com');
      setSeoData(data);
    } catch (err) {
      setError('Failed to fetch SEO analysis.');
    } finally {
      setLoading(false);
    }
  };

  const handleCompetitorAnalysis = async () => {
    setLoading(true);
    try {
      const data = await getCompetitorAnalysis('https://example.com');
      setCompetitorData(data);
    } catch (err) {
      setError('Failed to fetch competitor analysis.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Typography variant="h4">Dashboard</Typography>
      <Snackbar open={!!error} message={error} onClose={() => setError('')} />
      <Grid container spacing={4}>
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h5">SEO Analysis</Typography>
              <Button variant="contained" onClick={handleSEOAnalysis} disabled={loading}>
                {loading ? <CircularProgress size={24} /> : 'Analyze SEO'}
              </Button>
              {seoData && <Typography>SEO Score: {seoData.seo_score}</Typography>}
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h5">Competitor Analysis</Typography>
              <Button variant="contained" onClick={handleCompetitorAnalysis} disabled={loading}>
                {loading ? <CircularProgress size={24} /> : 'Analyze Competitor'}
              </Button>
              {competitorData && <Typography>Competitor Score: {competitorData.competitor_score}</Typography>}
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
}

export default Dashboard;
