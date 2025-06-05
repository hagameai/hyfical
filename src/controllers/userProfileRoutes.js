// userProfileRoutes.js
// This file defines the routes for user profile management in the application.

const express = require('express');
const { getUserProfile, updateUserProfile } = require('../controllers/userProfileController');

const router = express.Router();

/**
 * @route GET /api/user/profile
 * @desc Get user profile information
 * @access Private
 */
router.get('/profile', getUserProfile);

/**
 * @route PUT /api/user/profile
 * @desc Update user profile information
 * @access Private
 */
router.put('/profile', updateUserProfile);

module.exports = router;
