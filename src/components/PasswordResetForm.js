import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import axios from 'axios';

/**
 * PasswordResetForm component allows users to reset their password securely.
 * This form includes input fields for the user's email and a new password.
 */
const PasswordResetForm = () => {
    const [email, setEmail] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [message, setMessage] = useState('');
    const [error, setError] = useState('');
    const history = useHistory();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setMessage('');
        setError('');

        try {
            const response = await axios.post('/api/auth/reset-password', { email, newPassword });
            setMessage(response.data.message);
            // Redirect to login or another page after successful reset
            history.push('/login');
        } catch (err) {
            setError(err.response ? err.response.data.message : 'An error occurred. Please try again later.');
        }
    };

    return (
        <div>
            <h2>Reset Password</h2>
            {message && <p>{message}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="newPassword">New Password:</label>
                    <input
                        type="password"
                        id="newPassword"
                        value={newPassword}
                        onChange={(e) => setNewPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Reset Password</button>
            </form>
        </div>
    );
};

export default PasswordResetForm;