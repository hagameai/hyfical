// authMiddleware.js

const jwt = require('jsonwebtoken');
const config = require('../config'); // Assuming there is a config file for secret

/**
 * Middleware to authenticate JWT tokens.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @param {Function} next - The next middleware function.
 */
const authMiddleware = (req, res, next) => {
    // Get the token from the "Authorization" header
    const token = req.headers['authorization'] && req.headers['authorization'].split(' ')[1];

    // If there is no token, return an error response
    if (!token) {
        return res.status(401).json({ message: 'Access denied. No token provided.' });
    }

    // Verify the token
    jwt.verify(token, config.jwtSecret, (err, decoded) => {
        if (err) {
            return res.status(403).json({ message: 'Invalid token.' });
        }

        // Save the decoded information to the request object for future use
        req.user = decoded;
        next(); // Proceed to the next middleware or route handler
    });
};

module.exports = authMiddleware;
