
import React from 'react';
import { AppBar, Toolbar, Button } from '@mui/material';
import { useHistory } from 'react-router-dom';

const Navbar = ({ isAuthenticated, onLogout }) => {
  const history = useHistory();

  return (
    <AppBar position="static">
      <Toolbar>
        <Button color="inherit" onClick={() => history.push('/')}>Home</Button>
        <Button color="inherit" onClick={() => history.push('/about')}>About</Button>
        <Button color="inherit" onClick={() => history.push('/contact')}>Contact</Button>
        {isAuthenticated ? (
          <>
            <Button color="inherit" onClick={() => history.push('/dashboard')}>Dashboard</Button>
            <Button color="inherit" onClick={onLogout}>Logout</Button>
          </>
        ) : (
          <>
            <Button color="inherit" onClick={() => history.push('/signon')}>Login</Button>
            <Button color="inherit" onClick={() => history.push('/signon')}>Sign Up</Button>
          </>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
