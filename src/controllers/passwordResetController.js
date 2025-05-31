// passwordResetController.js

const User = require('../models/userModel');
const authService = require('../utils/authService');
const { sendResetEmail } = require('../utils/sendResetEmail');
const passwordValidation = require('../utils/passwordValidation');

/**
 * Controller for handling password reset operations.
 */

/**
 * Request a password reset link.
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 */
const requestPasswordReset = async (req, res) => {
    const { email } = req.body;
    try {
        // Check if user exists
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(404).json({ message: 'User not found.' });
        }

        // Generate reset token
        const resetToken = authService.generateResetToken(user);
        await sendResetEmail(user.email, resetToken);

        return res.status(200).json({ message: 'Password reset email sent.' });
    } catch (error) {
        console.error('Error requesting password reset:', error);
        return res.status(500).json({ message: 'Internal server error.' });
    }
};

/**
 * Reset the user's password.
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 */
const resetPassword = async (req, res) => {
    const { token, newPassword } = req.body;
    try {
        // Validate new password
        const isValid = passwordValidation.validate(newPassword);
        if (!isValid) {
            return res.status(400).json({ message: 'Invalid password.' });
        }

        // Verify token and find the user
        const user = await authService.verifyResetToken(token);
        if (!user) {
            return res.status(400).json({ message: 'Invalid token.' });
        }

        // Update user's password
        user.password = await authService.hashPassword(newPassword);
        await user.save();

        return res.status(200).json({ message: 'Password reset successful.' });
    } catch (error) {
        console.error('Error resetting password:', error);
        return res.status(500).json({ message: 'Internal server error.' });
    }
};

module.exports = {
    requestPasswordReset,
    resetPassword,
};
