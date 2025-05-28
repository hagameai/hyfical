const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

/**
 * @route POST /api/users/register
 * @description Register a new user
 * @access Public
 */
router.post('/register', userController.register);

/**
 * @route POST /api/users/login
 * @description Login an existing user
 * @access Public
 */
router.post('/login', userController.login);

/**
 * @route POST /api/users/reset-password
 * @description Request a password reset
 * @access Public
 */
router.post('/reset-password', userController.resetPassword);

/**
 * @route POST /api/users/update-password
 * @description Update user password
 * @access Private
 */
router.post('/update-password', userController.updatePassword);

module.exports = router;