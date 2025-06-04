// userProfileController.js

// Import necessary modules
const User = require('../models/userModel');
const express = require('express');
const router = express.Router();

/**
 * Get user profile by ID.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @returns {Object} User profile data or error message.
 */
router.get('/:id', async (req, res) => {
    try {
        const user = await User.findById(req.params.id);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.status(200).json(user);
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
});

/**
 * Update user profile by ID.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @returns {Object} Updated user data or error message.
 */
router.put('/:id', async (req, res) => {
    try {
        const user = await User.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.status(200).json(user);
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
});

/**
 * Delete user profile by ID.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @returns {Object} Success message or error message.
 */
router.delete('/:id', async (req, res) => {
    try {
        const user = await User.findByIdAndDelete(req.params.id);
        if (!user) {
            return res.status(404).json({ message: 'User not found' });
        }
        res.status(200).json({ message: 'User deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Server error', error });
    }
});

module.exports = router;