const express = require('express');
const router = express.Router();
const auth = require('./auth');
const User = require('../models/userModel');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

/**
 * @route POST /api/password-reset
 * @desc Handle password reset logic
 * @access Public
 */
router.post('/password-reset', async (req, res) => {
    const { email, newPassword, token } = req.body;

    // Validate input
    if (!email || !newPassword || !token) {
        return res.status(400).json({ message: 'All fields are required' });
    }

    try {
        // Verify token
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        const user = await User.findById(decoded.id);

        if (!user || user.email !== email) {
            return res.status(400).json({ message: 'Invalid token or email' });
        }

        // Hash the new password
        const hashedPassword = await bcrypt.hash(newPassword, 10);
        user.password = hashedPassword;
        await user.save();

        return res.status(200).json({ message: 'Password reset successful' });
    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Server error' });
    }
});

module.exports = router;