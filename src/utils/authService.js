// authService.js
// This service handles user authentication logic, including login, registration, and token management.

import axios from 'axios';

const API_URL = '/api/auth/';

// Register user
const register = async (username, email, password) => {
    const response = await axios.post(API_URL + 'register', {
        username,
        email,
        password
    });
    return response.data;
};

// Login user
const login = async (username, password) => {
    const response = await axios.post(API_URL + 'login', {
        username,
        password
    });
    if (response.data.token) {
        localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
};

// Logout user
const logout = () => {
    localStorage.removeItem('user');
};

// Get current user
const getCurrentUser = () => {
    return JSON.parse(localStorage.getItem('user')); 
};

const authService = {
    register,
    login,
    logout,
    getCurrentUser
};

export default authService;