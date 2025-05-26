// Import necessary modules
const express = require('express');
const { resetPassword, requestPasswordReset } = require('../utils/passwordResetController');

// Create a router instance
const router = express.Router();

/**
 * @route POST /api/password-reset/request
 * @description Request a password reset link
 * @access Public
 */
router.post('/request', requestPasswordReset);

/**
 * @route POST /api/password-reset/reset
 * @description Reset the user's password
 * @access Public
 */
router.post('/reset', resetPassword);

// Export the router
module.exports = router;