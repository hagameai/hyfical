const User = require('../models/userModel');
const jwt = require('jsonwebtoken');

// Register a new user
exports.register = async (req, res) => {
    const { username, password } = req.body;
    // Check for existing user
    const existingUser = await User.findOne({ username });
    if (existingUser) {
        return res.status(400).json({ message: 'User already exists' });
    }
    // Create new user
    const newUser = new User({ username, password });
    await newUser.save();
    return res.status(201).json({ message: 'User registered successfully' });
};

// Login user
exports.login = async (req, res) => {
    const { username, password } = req.body;
    // Validate user credentials
    const user = await User.findOne({ username });
    if (!user || !(await user.isCorrectPassword(password))) {
        return res.status(401).json({ message: 'Invalid credentials' });
    }
    // Generate JWT token
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    return res.status(200).json({ token });
};

// Export other functionalities as needed
