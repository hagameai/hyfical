import React, { useState } from 'react';

/**
 * LoginForm component for user authentication.
 * Allows users to enter their credentials and submit for login.
 */
const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // TODO: Implement login logic
        if (!email || !password) {
            setError('Please fill in both fields.');
            return;
        }
        // Call API to authenticate user
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
