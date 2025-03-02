// auth.js
// This file handles user authentication logic, including login and registration.

const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const User = require('../models/userModel');

const SECRET_KEY = process.env.SECRET_KEY || 'your_secret_key';

// Register a new user
async function registerUser(req, res) {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ username, password: hashedPassword });
    await newUser.save();
    res.status(201).send('User registered successfully');
}

// Login user
async function loginUser(req, res) {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user) return res.status(404).send('User not found');

    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) return res.status(401).send('Invalid password');

    const token = jwt.sign({ id: user._id }, SECRET_KEY);
    res.status(200).json({ token });
}

module.exports = { registerUser, loginUser };