/**
 * passwordValidation.js
 * 
 * This module provides functions to validate the strength
 * and requirements of a password. It checks for minimum length,
 * uppercase letters, lowercase letters, numbers, and special characters.
 * 
 * @module passwordValidation
 */

/**
 * Validate the strength of a password.
 * 
 * @param {string} password - The password to validate.
 * @returns {Object} An object containing:
 *   - isValid {boolean} - Indicates if the password is valid.
 *   - errors {Array<string>} - List of errors if invalid.
 */
function validatePassword(password) {
    const errors = [];

    // Check password length
    if (password.length < 8) {
        errors.push('Password must be at least 8 characters long.');
    }

    // Check for uppercase letters
    if (!/[A-Z]/.test(password)) {
        errors.push('Password must contain at least one uppercase letter.');
    }

    // Check for lowercase letters
    if (!/[a-z]/.test(password)) {
        errors.push('Password must contain at least one lowercase letter.');
    }

    // Check for numbers
    if (!/[0-9]/.test(password)) {
        errors.push('Password must contain at least one number.');
    }

    // Check for special characters
    if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
        errors.push('Password must contain at least one special character.');
    }

    return {
        isValid: errors.length === 0,
        errors
    };
}

module.exports = { validatePassword };