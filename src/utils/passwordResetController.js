// passwordResetController.js

const passwordValidation = require('../utils/passwordValidation');
const sendResetEmail = require('../utils/sendResetEmail');
const User = require('../models/userModel');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

/**
 * Controller for handling password reset requests.
 */

/**
 * Initiates password reset process by sending a reset email.
 *
 * @param {Object} req - The request object containing user email.
 * @param {Object} res - The response object.
 * @returns {Object} - Response indicating success or failure.
 */
const initiatePasswordReset = async (req, res) => {
    const { email } = req.body;

    // Validate email
    if (!email) {
        return res.status(400).json({ message: 'Email is required.' });
    }

    try {
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(404).json({ message: 'User not found.' });
        }

        // Create a reset token
        const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });

        // Send reset email
        await sendResetEmail(email, token);

        return res.status(200).json({ message: 'Reset email sent.' });
    } catch (error) {
        console.error('Error initiating password reset:', error);
        return res.status(500).json({ message: 'Server error.' });
    }
};

/**
 * Resets the user's password.
 *
 * @param {Object} req - The request object containing the token and new password.
 * @param {Object} res - The response object.
 * @returns {Object} - Response indicating success or failure.
 */
const resetPassword = async (req, res) => {
    const { token, newPassword } = req.body;

    // Validate new password
    if (!passwordValidation(newPassword)) {
        return res.status(400).json({ message: 'Invalid password format.' });
    }

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        const user = await User.findById(decoded.id);

        if (!user) {
            return res.status(404).json({ message: 'User not found.' });
        }

        // Hash the new password and save it
        user.password = await bcrypt.hash(newPassword, 10);
        await user.save();

        return res.status(200).json({ message: 'Password reset successfully.' });
    } catch (error) {
        console.error('Error resetting password:', error);
        return res.status(500).json({ message: 'Server error.' });
    }
};

module.exports = {
    initiatePasswordReset,
    resetPassword
};