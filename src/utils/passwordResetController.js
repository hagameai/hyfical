const User = require('../models/userModel');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');

/**
 * Controller for handling password reset requests.
 */

/**
 * Request a password reset link.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 */
const requestPasswordReset = async (req, res) => {
    const { email } = req.body;
    try {
        const user = await User.findOne({ email });
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        // Generate a reset token
        const resetToken = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
        // Here you would send the reset token via email
        // sendResetEmail(email, resetToken);
        return res.status(200).json({ message: 'Password reset link sent' });
    } catch (error) {
        return res.status(500).json({ message: 'Server error', error });
    }
};

/**
 * Reset the user's password.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 */
const resetPassword = async (req, res) => {
    const { token, newPassword } = req.body;
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        const user = await User.findById(decoded.id);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        // Hash the new password
        const hashedPassword = await bcrypt.hash(newPassword, 10);
        user.password = hashedPassword;
        await user.save();
        return res.status(200).json({ message: 'Password reset successful' });
    } catch (error) {
        return res.status(500).json({ message: 'Server error', error });
    }
};

module.exports = {
    requestPasswordReset,
    resetPassword,
};
