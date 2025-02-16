const jwt = require('jsonwebtoken');
const User = require('../models/userModel');

// Function to handle user registration
const registerUser = async (req, res) => {
    const { username, password } = req.body;
    // Check if user already exists
    const existingUser = await User.findOne({ username });
    if (existingUser) {
        return res.status(400).json({ message: 'User already exists' });
    }
    // Create new user
    const user = new User({ username, password });
    await user.save();
    res.status(201).json({ message: 'User registered successfully' });
};

// Function to handle user login
const loginUser = async (req, res) => {
    const { username, password } = req.body;
    // Validate user credentials
    const user = await User.findOne({ username });
    if (!user || user.password !== password) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }
    // Generate JWT token
    const token = jwt.sign({ id: user._id }, 'secret_key', { expiresIn: '1h' });
    res.status(200).json({ token });
};

module.exports = {
    registerUser,
    loginUser,
};