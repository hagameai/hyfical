'use strict';

const jwt = require('jsonwebtoken');
const User = require('../models/userModel');

// User authentication logic

/**
 * Registers a new user in the system.
 * @param {Object} req - The request object containing user data.
 * @param {Object} res - The response object to send results.
 */
exports.register = async (req, res) => {
    const { username, password } = req.body;

    try {
        const newUser = await User.create({ username, password });
        res.status(201).json({ message: 'User registered successfully', user: newUser });
    } catch (error) {
        res.status(400).json({ message: 'User registration failed', error });
    }
};

/**
 * Authenticates a user and generates a JWT token.
 * @param {Object} req - The request object containing login data.
 * @param {Object} res - The response object to send results.
 */
exports.login = async (req, res) => {
    const { username, password } = req.body;

    try {
        const user = await User.findOne({ username });
        if (!user || !(await user.comparePassword(password))) {
            return res.status(401).json({ message: 'Invalid credentials' });
        }

        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
        res.status(200).json({ message: 'Login successful', token });
    } catch (error) {
        res.status(500).json({ message: 'Login failed', error });
    }
};

/**
 * Middleware to protect routes by verifying JWT.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @param {Function} next - The next middleware function.
 */
exports.authenticate = (req, res, next) => {
    const token = req.headers['authorization'];

    if (!token) return res.status(403).json({ message: 'No token provided' });

    jwt.verify(token, process.env.JWT_SECRET, (err, decoded) => {
        if (err) return res.status(401).json({ message: 'Unauthorized' });
        req.userId = decoded.id;
        next();
    });
};