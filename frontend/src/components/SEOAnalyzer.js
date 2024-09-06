
import React, { useState } from 'react';
import { TextField, Button, CircularProgress, Typography, Grid, Card, CardContent, Snackbar } from '@mui/material';
import { Search } from '@mui/icons-material';
import axios from 'axios';

const SEOAnalyzer = () => {
  const [url, setUrl] = useState('');
  const [keyword, setKeyword] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [snackbarOpen, setSnackbarOpen] = useState(false);

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/seo/analyze`,
        { url, keyword },
      );
      setResult(response.data);
      setSnackbarOpen(true);
    } catch (err) {
      setError('Failed to analyze SEO.');
    }
    setLoading(false);
  };

  return (
    <Card sx={{ mt: 5, p: 3 }}>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          <Search sx={{ mr: 1 }} /> SEO Analysis
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
              label="Keyword"
              fullWidth
              value={keyword}
              onChange={(e) => setKeyword(e.target.value)}
            />
          </Grid>
          <Grid item xs={12}>
            <Button
              onClick={handleAnalyze}
              disabled={loading}
              fullWidth
              variant="contained"
            >
              {loading ? <CircularProgress size={24} /> : 'Analyze SEO'}
            </Button>
          </Grid>
        </Grid>

        {error && <Typography color="error" variant="body2">{error}</Typography>}
        {result && <Typography variant="body1" sx={{ mt: 3 }}>{JSON.stringify(result)}</Typography>}

        <Snackbar
          open={snackbarOpen}
          autoHideDuration={4000}
          onClose={() => setSnackbarOpen(false)}
          message="SEO Analysis Complete!"
        />
      </CardContent>
    </Card>
  );
};

export default SEOAnalyzer;
