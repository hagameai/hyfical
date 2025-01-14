import React, { useState } from 'react';

/**
 * LoginForm Component
 * 
 * This component provides a user interface for logging in. It includes fields for the username and password,
 * and a submit button to send the credentials to the authentication API.
 */
const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        // TODO: Implement API call for authentication
        // Handle login logic here

        // Example placeholder response
        const mockResponse = { success: false, message: 'Invalid credentials' };

        if (!mockResponse.success) {
            setError(mockResponse.message);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Username:</label>
                <input 
                    type="text" 
                    value={username} 
                    onChange={(e) => setUsername(e.target.value)} 
                    required 
                />
            </div>
            <div>
                <label>Password:</label>
                <input 
                    type="password" 
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)} 
                    required 
                />
            </div>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <button type="submit">Login</button>
        </form>
    );
};

export default LoginForm;
