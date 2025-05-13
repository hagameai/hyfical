const { validateRegistration } = require('../../src/utils/authService');

describe('Registration Validation', () => {
    it('should return error for missing username', () => {
        const result = validateRegistration({ password: 'Password123!', email: 'user@example.com' });
        expect(result).toEqual({ error: 'Username is required' });
    });

    it('should return error for missing password', () => {
        const result = validateRegistration({ username: 'user', email: 'user@example.com' });
        expect(result).toEqual({ error: 'Password is required' });
    });

    it('should return error for invalid email format', () => {
        const result = validateRegistration({ username: 'user', password: 'Password123!', email: 'invalid-email' });
        expect(result).toEqual({ error: 'Invalid email format' });
    });

    it('should return success for valid registration details', () => {
        const result = validateRegistration({ username: 'user', password: 'Password123!', email: 'user@example.com' });
        expect(result).toEqual({ success: true });
    });
});