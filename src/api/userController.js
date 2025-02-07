// userController.js

const UserService = require('../api/authService');

/**
 * User controller for handling user-related requests.
 */
class UserController {
    /**
     * Handles user registration.
     * @param {Object} req - The request object.
     * @param {Object} res - The response object.
     */
    async register(req, res) {
        try {
            const userData = req.body;
            const newUser = await UserService.registerUser(userData);
            res.status(201).json(newUser);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * Handles user login.
     * @param {Object} req - The request object.
     * @param {Object} res - The response object.
     */
    async login(req, res) {
        try {
            const { email, password } = req.body;
            const token = await UserService.loginUser(email, password);
            res.status(200).json({ token });
        } catch (error) {
            res.status(401).json({ message: error.message });
        }
    }
}

module.exports = new UserController();