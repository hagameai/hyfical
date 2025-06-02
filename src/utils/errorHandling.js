// errorHandling.js

/**
 * Centralized error handling middleware for the application.
 * This middleware captures errors thrown in the application and formats them
 * for consistent API responses.
 */

const createError = require('http-errors');

/**
 * Error handling middleware.
 * @param {Object} err - The error object.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * @param {Function} next - The next middleware function.
 */
const errorHandler = (err, req, res, next) => {
    // Log the error (could be to a logging service)
    console.error(err);

    // Set the response status and message
    const status = err.status || 500;
    const message = err.message || 'Internal Server Error';

    // Send the error response
    res.status(status).json({
        status,
        message,
    });
};

module.exports = errorHandler;