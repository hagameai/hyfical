import React from 'react';

/**
 * PasswordResetSuccess component
 * 
 * This component displays a success message to the user after they have successfully reset their password.
 * It can be used in various parts of the application where a password reset confirmation is needed.
 */
const PasswordResetSuccess = () => {
    return (
        <div className="password-reset-success">
            <h2>Password Reset Successful!</h2>
            <p>Your password has been reset successfully. You can now log in with your new password.</p>
        </div>
    );
};

export default PasswordResetSuccess;