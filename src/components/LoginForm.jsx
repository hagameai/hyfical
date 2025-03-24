import React, { useState } from 'react';

/**
 * LoginForm component allows users to log in to their account.
 * It collects email and password inputs and handles form submission.
 */
const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // TODO: Implement login logic here
        // Example: Call authService.login(email, password)
        // Handle success or error accordingly
        console.log('Logging in with:', { email, password });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Email:</label>
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
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
            {error && <div style={{color: 'red'}}>{error}</div>}
            <button type="submit">Login</button>
        </form>
    );
};

export default LoginForm;