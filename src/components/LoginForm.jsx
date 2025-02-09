import React, { useState } from 'react';
import PropTypes from 'prop-types';

const LoginForm = ({ onLogin }) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!email || !password) {
            setError('Email and Password are required.');
            return;
        }
        onLogin({ email, password });
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
            {error && <div className="error">{error}</div>}
            <button type="submit">Login</button>
        </form>
    );
};

LoginForm.propTypes = {
    onLogin: PropTypes.func.isRequired,
};

export default LoginForm;