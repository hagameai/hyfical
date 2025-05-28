const express = require('express');
const router = express.Router();
const passwordResetController = require('../utils/passwordResetController');

/**
 * @route POST /api/password-reset
 * @desc Initiate password reset process by sending a reset email.
 * @access Public
 */
router.post('/', passwordResetController.initiateReset);

/**
 * @route POST /api/password-reset/verify
 * @desc Verify the password reset token and reset the password.
 * @access Public
 */
router.post('/verify', passwordResetController.verifyReset);

module.exports = router;