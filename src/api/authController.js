// authController.js

const authService = require('../utils/authService');

/**
 * Handles user authentication requests.
 */
class AuthController {
    /**
     * Registers a new user.
     * @param {Object} req - The request object containing user data.
     * @param {Object} res - The response object.
     * @returns {Promise<void>}
     */
    async register(req, res) {
        try {
            const user = await authService.registerUser(req.body);
            res.status(201).json(user);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * Authenticates a user and returns a JWT.
     * @param {Object} req - The request object containing user credentials.
     * @param {Object} res - The response object.
     * @returns {Promise<void>}
     */
    async login(req, res) {
        try {
            const token = await authService.authenticateUser(req.body);
            res.status(200).json({ token });
        } catch (error) {
            res.status(401).json({ message: error.message });
        }
    }
}

module.exports = new AuthController();