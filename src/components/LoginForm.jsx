import React, { useState } from 'react';

/**
 * LoginForm component for user authentication.
 * This component handles user login functionality,
 * including form submission and state management.
 */
const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        // Logic for handling the login goes here
        // For example, call the auth API and handle responses
        try {
            // Replace with actual authentication logic
            console.log('Logging in with', email, password);
            // Clear inputs on successful login
            setEmail('');
            setPassword('');
        } catch (err) {
            setError('Login failed. Please try again.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Login</h2>
            {error && <p className="error">{error}</p>}
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
                <label htmlFor="password">Password:</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </div>
            <button type="submit">Login</button>
        </form>
    );
};

export default LoginForm;