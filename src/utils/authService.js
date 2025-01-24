// authService.js
// This module provides functions for user authentication, including login and registration.

import axios from 'axios';

const API_URL = '/api/auth/';

// Register user
const register = async (userData) => {
    const response = await axios.post(`${API_URL}register`, userData);
    return response.data;
};

// Login user
const login = async (credentials) => {
    const response = await axios.post(`${API_URL}login`, credentials);
    if (response.data.token) {
        localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
};

// Logout user
const logout = () => {
    localStorage.removeItem('user');
};

export default { register, login, logout };