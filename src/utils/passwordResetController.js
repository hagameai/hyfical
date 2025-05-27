const User = require('../models/userModel');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const sendResetEmail = require('./sendResetEmail');

/**
 * Controller logic for handling password reset requests.
 */
const passwordResetController = {
    /**
     * Initiates the password reset process by sending a reset link to the user's email.
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     */
    initiatePasswordReset: async (req, res) => {
        const { email } = req.body;
        try {
            const user = await User.findOne({ email });
            if (!user) {
                return res.status(404).json({ message: 'User not found.' });
            }
            // Generate a password reset token
            const resetToken = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
            // Send reset email
            await sendResetEmail(email, resetToken);
            res.status(200).json({ message: 'Password reset email sent.' });
        } catch (error) {
            console.error(error);
            res.status(500).json({ message: 'An error occurred while processing your request.' });
        }
    },

    /**
     * Resets the user's password based on the provided token and new password.
     * @param {Object} req - Express request object
     * @param {Object} res - Express response object
     */
    resetPassword: async (req, res) => {
        const { token, newPassword } = req.body;
        try {
            const decoded = jwt.verify(token, process.env.JWT_SECRET);
            const user = await User.findById(decoded.id);
            if (!user) {
                return res.status(404).json({ message: 'User not found.' });
            }
            // Hash new password
            const hashedPassword = await bcrypt.hash(newPassword, 10);
            user.password = hashedPassword;
            await user.save();
            res.status(200).json({ message: 'Password reset successful.' });
        } catch (error) {
            console.error(error);
            if (error.name === 'JsonWebTokenError') {
                return res.status(400).json({ message: 'Invalid or expired token.' });
            }
            res.status(500).json({ message: 'An error occurred while resetting the password.' });
        }
    }
};

module.exports = passwordResetController;