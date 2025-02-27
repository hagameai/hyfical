// userController.js

// Import necessary modules
const UserService = require('../api/authService');

/**
 * Controller for handling user-related requests.
 */
class UserController {
    /**
     * Login user with email and password.
     * @param {Request} req - Express request object.
     * @param {Response} res - Express response object.
     */
    static async login(req, res) {
        try {
            const { email, password } = req.body;
            const user = await UserService.authenticateUser(email, password);
            if (user) {
                // Generate JWT token
                const token = UserService.generateToken(user);
                return res.json({ token });
            }
            return res.status(401).json({ message: 'Invalid credentials' });
        } catch (error) {
            return res.status(500).json({ message: error.message });
        }
    }

    /**
     * Register a new user.
     * @param {Request} req - Express request object.
     * @param {Response} res - Express response object.
     */
    static async register(req, res) {
        try {
            const userData = req.body;
            const newUser = await UserService.createUser(userData);
            return res.status(201).json(newUser);
        } catch (error) {
            return res.status(500).json({ message: error.message });
        }
    }
}

module.exports = UserController;