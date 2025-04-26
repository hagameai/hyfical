// tokenManagement.js
// This module handles JWT token creation, validation, and expiration.

const jwt = require('jsonwebtoken');
const config = require('../config'); // Assuming config contains secret keys and other settings

/**
 * Generate a JWT token for a user.
 * @param {Object} user - The user object.
 * @returns {string} - The generated JWT token.
 */
function generateToken(user) {
    return jwt.sign({ id: user.id }, config.jwtSecret, { expiresIn: '1h' });
}

/**
 * Verify a given JWT token.
 * @param {string} token - The JWT token to verify.
 * @returns {Object|null} - The decoded user information or null if verification fails.
 */
function verifyToken(token) {
    try {
        return jwt.verify(token, config.jwtSecret);
    } catch (error) {
        console.error('Token verification failed:', error);
        return null;
    }
}

/**
 * Middleware to validate the JWT token in requests.
 * @param {Object} req - The incoming request object.
 * @param {Object} res - The response object.
 * @param {Function} next - The next middleware function.
 */
function authenticateToken(req, res, next) {
    const token = req.headers['authorization']?.split(' ')[1];
    if (!token) return res.sendStatus(401); // Unauthorized

    const user = verifyToken(token);
    if (!user) return res.sendStatus(403); // Forbidden

    req.user = user;
    next(); // Proceed to the next middleware or route handler
}

module.exports = { generateToken, verifyToken, authenticateToken };