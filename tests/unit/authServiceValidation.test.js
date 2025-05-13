const { validateLogin, validateRegistration } = require('../utils/authService');

describe('authService validation', () => {
    test('validateLogin should return true for valid credentials', () => {
        const credentials = { username: 'testuser', password: 'testpass' };
        const result = validateLogin(credentials);
        expect(result).toBe(true);
    });

    test('validateLogin should return false for invalid username', () => {
        const credentials = { username: '', password: 'testpass' };
        const result = validateLogin(credentials);
        expect(result).toBe(false);
    });

    test('validateLogin should return false for invalid password', () => {
        const credentials = { username: 'testuser', password: '' };
        const result = validateLogin(credentials);
        expect(result).toBe(false);
    });

    test('validateRegistration should return true for valid user data', () => {
        const userData = { username: 'newuser', password: 'newpass', email: 'user@example.com' };
        const result = validateRegistration(userData);
        expect(result).toBe(true);
    });

    test('validateRegistration should return false for invalid email', () => {
        const userData = { username: 'newuser', password: 'newpass', email: 'invalid-email' };
        const result = validateRegistration(userData);
        expect(result).toBe(false);
    });

    test('validateRegistration should return false for missing username', () => {
        const userData = { username: '', password: 'newpass', email: 'user@example.com' };
        const result = validateRegistration(userData);
        expect(result).toBe(false);
    });
});