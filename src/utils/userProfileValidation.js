// userProfileValidation.js

/**
 * Validation logic for user profile data.
 * This module exports functions to validate user profile inputs.
 */

// Importing necessary libraries
const { body, validationResult } = require('express-validator');

/**
 * Validate user profile data.
 * @returns {Array} Array of validation rules.
 */
const validateUserProfile = () => {
    return [
        body('username')
            .isString().withMessage('Username must be a string.')
            .isLength({ min: 3, max: 30 }).withMessage('Username must be between 3 and 30 characters long.'),
        body('email')
            .isEmail().withMessage('Email must be a valid email address.'),
        body('bio')
            .optional() // bio is optional
            .isString().withMessage('Bio must be a string.')
            .isLength({ max: 500 }).withMessage('Bio must not exceed 500 characters.'),
        body('avatar')
            .optional() // avatar is optional
            .isString().withMessage('Avatar URL must be a string.')
            .isURL().withMessage('Avatar must be a valid URL.')
    ];
};

/**
 * Function to handle validation result.
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 * @param {Function} next - Next middleware function.
 */
const handleValidationResult = (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }
    next();
};

module.exports = {
    validateUserProfile,
    handleValidationResult
};