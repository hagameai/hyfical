// passwordResetValidation.js

/**
 * Validate password reset requests.
 * @param {Object} requestBody - The body of the request containing email and password.
 * @returns {Object} - Returns an object with error messages if validation fails, otherwise returns null.
 */
function validatePasswordReset(requestBody) {
    const errors = {};

    // Check if email is provided
    if (!requestBody.email || typeof requestBody.email !== 'string') {
        errors.email = 'Email is required and must be a valid string.';
    }

    // Check if password is provided
    if (!requestBody.password || typeof requestBody.password !== 'string') {
        errors.password = 'Password is required and must be a valid string.';
    } else if (requestBody.password.length < 8) {
        errors.password = 'Password must be at least 8 characters long.';
    }

    // If errors exist, return them
    return Object.keys(errors).length ? errors : null;
}

module.exports = { validatePasswordReset };