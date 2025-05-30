// userRoutes.js

const express = require('express');
const { registerUser, loginUser } = require('../api/authController');

const router = express.Router();

/**
 * @route POST /api/users/register
 * @desc Register a new user
 * @access Public
 */
router.post('/register', registerUser);

/**
 * @route POST /api/users/login
 * @desc Login a user
 * @access Public
 */
router.post('/login', loginUser);

module.exports = router;