// auth.js

/**
 * User Authentication API
 * 
 * This module handles user login and registration, 
 * utilizing JWT for session management and password hashing.
 */

const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const User = require('../models/userModel');
const router = express.Router();

/**
 * Register a new user
 * @route POST /register
 * @param {Object} req - Request object containing user data
 * @param {Object} res - Response object
 * @returns {Object} - Confirmation message
 */
router.post('/register', async (req, res) => {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = new User({ username, password: hashedPassword });
    await user.save();
    res.status(201).json({ message: 'User registered successfully' });
});

/**
 * Login a user
 * @route POST /login
 * @param {Object} req - Request object containing login data
 * @param {Object} res - Response object
 * @returns {Object} - JWT token
 */
router.post('/login', async (req, res) => {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (user && await bcrypt.compare(password, user.password)) {
        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
        res.json({ token });
    } else {
        res.status(401).json({ message: 'Invalid credentials' });
    }
});

module.exports = router;