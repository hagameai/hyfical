/**
 * passwordReset.js
 * 
 * This module handles the password reset logic and validation. 
 * It provides functions to validate the password, generate a reset token, 
 * and verify the token during the password reset process.
 */

const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const User = require('../models/userModel');

/**
 * Validates the new password according to specified criteria.
 * @param {string} password - The new password to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
function validatePassword(password) {
    // Check for password length and complexity
    const minLength = 8;
    const hasUpperCase = /[A-Z]/.test(password);
    const hasLowerCase = /[a-z]/.test(password);
    const hasNumbers = /[0-9]/.test(password);
    const hasSpecialChar = /[!@#$%^&*]/.test(password);

    return password.length >= minLength && hasUpperCase && hasLowerCase && hasNumbers && hasSpecialChar;
}

/**
 * Generates a password reset token for the user.
 * @param {string} email - The user's email address.
 * @returns {string|null} - The generated token or null if user not found.
 */
async function generateResetToken(email) {
    const user = await User.findOne({ email });
    if (!user) return null;

    // Create a reset token using JWT
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1h' });
    return token;
}

/**
 * Verifies the password reset token.
 * @param {string} token - The token to verify.
 * @returns {object|null} - The decoded token payload or null if invalid.
 */
function verifyResetToken(token) {
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        return decoded;
    } catch (error) {
        return null; // Token is invalid
    }
}

/**
 * Resets the user's password.
 * @param {string} userId - The user's ID.
 * @param {string} newPassword - The new password to set.
 * @returns {Promise<boolean>} - True if successful, false otherwise.
 */
async function resetPassword(userId, newPassword) {
    if (!validatePassword(newPassword)) return false;
    const user = await User.findById(userId);
    if (!user) return false;

    user.password = newPassword; // Assume password hashing is handled in the user model
    await user.save();
    return true;
}

module.exports = {
    validatePassword,
    generateResetToken,
    verifyResetToken,
    resetPassword
};