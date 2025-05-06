import React from 'react';

/**
 * PasswordResetError Component
 * 
 * This component displays an error message if the password reset process fails.
 */
const PasswordResetError = ({ message }) => {
    return (
        <div className="password-reset-error">
            <h2>Error</h2>
            <p>{message}</p>
        </div>
    );
};

export default PasswordResetError;
