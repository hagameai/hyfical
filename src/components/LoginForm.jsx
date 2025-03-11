import React, { useState } from 'react';

/**
 * LoginForm component.
 * This component handles user login via a form.
 * It captures the email and password, and triggers
 * the login action. Validation is included to ensure
 * the fields are filled out.
 */
const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!email || !password) {
            setError('Please fill in both fields.');
            return;
        }
        // Logic to handle login (e.g., API call)
        console.log('Submitting:', { email, password });
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Email:</label>
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <div>
                <label>Password:</label>
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            {error && <div style={{ color: 'red' }}>{error}</div>}
            <button type="submit">Login</button>
        </form>
    );
};

export default LoginForm;