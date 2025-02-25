'use strict';

const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const User = require('../models/userModel');

/**
 * User authentication functions
 */

/**
 * Registers a new user and hashes the password
 * @param {Object} req - Request object containing user data
 * @param {Object} res - Response object
 */
const registerUser = async (req, res) => {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ username, password: hashedPassword });
    await newUser.save();
    res.status(201).json({ message: 'User registered successfully.' });
};

/**
 * Authenticates a user and issues a JWT token
 * @param {Object} req - Request object containing login credentials
 * @param {Object} res - Response object
 */
const loginUser = async (req, res) => {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user || !(await bcrypt.compare(password, user.password))) {
        return res.status(401).json({ message: 'Invalid credentials.' });
    }
    const token = jwt.sign({ userId: user._id }, 'secretKey', { expiresIn: '1h' });
    res.status(200).json({ token });
};

module.exports = { registerUser, loginUser };