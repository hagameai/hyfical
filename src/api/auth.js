const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const UserModel = require('../models/userModel');

/**
 * User Authentication Controller
 */
const AuthController = {
    /**
     * Register a new user
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     * @returns {Promise<void>}
     */
    register: async (req, res) => {
        const { username, password } = req.body;
        const hashedPassword = await bcrypt.hash(password, 10);
        const user = new UserModel({ username, password: hashedPassword });
        await user.save();
        res.status(201).send({ message: 'User registered successfully' });
    },

    /**
     * Login a user
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     * @returns {Promise<void>}
     */
    login: async (req, res) => {
        const { username, password } = req.body;
        const user = await UserModel.findOne({ username });
        if (!user || !(await bcrypt.compare(password, user.password))) {
            return res.status(403).send({ message: 'Invalid credentials' });
        }
        const token = jwt.sign({ id: user._id }, 'secret', { expiresIn: '1h' });
        res.send({ token });
    }
};

module.exports = AuthController;