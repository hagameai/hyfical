// authController.js

const authService = require('./authService');

/**
 * Handles user registration.
 * @param {Object} req - The request object containing user data.
 * @param {Object} res - The response object to send data back.
 */
exports.register = async (req, res) => {
    try {
        const user = await authService.registerUser(req.body);
        res.status(201).json({ message: 'User registered successfully', user });
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
};

/**
 * Handles user login.
 * @param {Object} req - The request object containing login data.
 * @param {Object} res - The response object to send data back.
 */
exports.login = async (req, res) => {
    try {
        const token = await authService.loginUser(req.body);
        res.status(200).json({ message: 'Login successful', token });
    } catch (error) {
        res.status(401).json({ message: error.message });
    }
};

/**
 * Handles user logout.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object to send data back.
 */
exports.logout = (req, res) => {
    // Implement logout logic (e.g., invalidate token)
    res.status(200).json({ message: 'User logged out successfully' });
};
