const express = require('express');
const router = express.Router();
const passwordResetController = require('../controllers/passwordResetController');

/**
 * @route POST /api/password-reset
 * @description Initiate password reset process
 * @param {string} email - User's email address
 * @returns {object} Confirmation message
 */
router.post('/password-reset', passwordResetController.initiatePasswordReset);

/**
 * @route POST /api/password-reset/confirm
 * @description Confirm password reset with token
 * @param {string} token - Reset token
 * @param {string} newPassword - New password
 * @returns {object} Confirmation message
 */
router.post('/password-reset/confirm', passwordResetController.confirmPasswordReset);

module.exports = router;