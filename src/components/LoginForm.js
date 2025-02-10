import React, { useState } from 'react';

/**
 * LoginForm component allows users to log in to the application.
 * It handles user input and submits the login request to the API.
 */
const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ username, password }),
            });
            if (!response.ok) {
                throw new Error('Login failed!');
            }
            // Handle successful login (e.g., redirect, store token)
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>
                    Username:
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required />
                </label>
            </div>
            <div>
                <label>
                    Password:
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </label>
            </div>
            {error && <p>{error}</p>}
            <button type="submit">Log In</button>
        </form>
    );
};

export default LoginForm;
