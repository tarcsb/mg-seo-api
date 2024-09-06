
import React from 'react';
import { Container, Typography } from '@mui/material';

const Profile = () => {
  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        User Profile
      </Typography>
      <Typography variant="body1">
        This is your profile page. You can view and update your account information here.
      </Typography>
      {/* Add profile management features here */}
    </Container>
  );
};

export default Profile;
