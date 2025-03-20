const jwt = require('jsonwebtoken');
const User = require('../models/userModel');

// User Registration
exports.register = async (req, res) => {
    const { username, password } = req.body;
    try {
        const user = new User({ username, password }); // Ideally, hash the password
        await user.save();
        res.status(201).json({ message: 'User created successfully' });
    } catch (error) {
        res.status(400).json({ error: 'User registration failed' });
    }
};

// User Login
exports.login = async (req, res) => {
    const { username, password } = req.body;
    try {
        const user = await User.findOne({ username });
        if (!user || user.password !== password) { // Password should be hashed and compared
            return res.status(401).json({ error: 'Invalid credentials' });
        }
        const token = jwt.sign({ id: user._id }, 'secretkey', { expiresIn: '1h' }); // Use environment variable for secret
        res.status(200).json({ token });
    } catch (error) {
        res.status(500).json({ error: 'Login failed' });
    }
};