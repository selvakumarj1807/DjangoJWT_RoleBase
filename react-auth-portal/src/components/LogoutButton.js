// src/components/LogoutButton.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

function LogoutButton() {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Remove tokens from localStorage
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    localStorage.removeItem('user');

    // Redirect to login/home
    navigate('/');
  };

  const buttonStyle = {
    padding: '10px 20px',
    backgroundColor: '#e53935',
    color: '#fff',
    border: 'none',
    borderRadius: '8px',
    fontSize: '16px',
    fontWeight: '600',
    cursor: 'pointer',
    marginTop: '15px',
    width: '100%',
    maxWidth: '200px',
    transition: 'background-color 0.3s ease',
  };

  const responsiveWrapper = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    margin: '0 auto',
  };

  return (
    <div style={responsiveWrapper}>
      <button
        onClick={handleLogout}
        style={buttonStyle}
        onMouseOver={(e) => (e.target.style.backgroundColor = '#d32f2f')}
        onMouseOut={(e) => (e.target.style.backgroundColor = '#e53935')}
      >
        Logout
      </button>
    </div>
  );
}

export default LogoutButton;
