// userController.js

// Import necessary modules and dependencies
const User = require('../models/userModel');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

/**
 * @description Register a new user
 * @param {Object} req - Express request object
 * @param {Object} res - Express response object
 * @returns {Object} - Response object with success or error message
 */
const registerUser = async (req, res) => {
    const { username, password } = req.body;

    try {
        // Check if user already exists
        const existingUser = await User.findOne({ username });
        if (existingUser) {
            return res.status(400).json({ message: 'User already exists' });
        }

        // Hash the password
        const hashedPassword = await bcrypt.hash(password, 10);
        const newUser = new User({ username, password: hashedPassword });

        // Save user to the database
        await newUser.save();
        res.status(201).json({ message: 'User registered successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};

/**
 * @description Authenticate user and return JWT token
 * @param {Object} req - Express request object
 * @param {Object} res - Express response object
 * @returns {Object} - Response object with JWT token
 */
const loginUser = async (req, res) => {
    const { username, password } = req.body;

    try {
        // Find user by username
        const user = await User.findOne({ username });
        if (!user) {
            return res.status(400).json({ message: 'Invalid credentials' });
        }

        // Validate password
        const isPasswordValid = await bcrypt.compare(password, user.password);
        if (!isPasswordValid) {
            return res.status(400).json({ message: 'Invalid credentials' });
        }

        // Generate JWT token
        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
        res.status(200).json({ token });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
};

// Export controller functions
module.exports = {
    registerUser,
    loginUser,
};