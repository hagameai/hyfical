// authService.js
// This file contains functions for user authentication, including login and registration.

import axios from 'axios';

const API_URL = '/api/auth';

// Login user
export const login = async (username, password) => {
    const response = await axios.post(`${API_URL}/login`, { username, password });
    if (response.data.token) {
        localStorage.setItem('user', JSON.stringify(response.data));
    }
    return response.data;
};

// Register user
export const register = async (username, password) => {
    return await axios.post(`${API_URL}/register`, { username, password });
};

// Logout user
export const logout = () => {
    localStorage.removeItem('user');
};

// Check if user is logged in
export const isLoggedIn = () => {
    return !!localStorage.getItem('user');
};