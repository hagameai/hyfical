const { validateLogin } = require('../../src/utils/authService');

describe('Login Validation', () => {
    it('should return true for valid credentials', () => {
        const result = validateLogin('user@example.com', 'password123');
        expect(result).toBe(true);
    });

    it('should return false for invalid email format', () => {
        const result = validateLogin('invalidEmail', 'password123');
        expect(result).toBe(false);
    });

    it('should return false for empty email', () => {
        const result = validateLogin('', 'password123');
        expect(result).toBe(false);
    });

    it('should return false for empty password', () => {
        const result = validateLogin('user@example.com', '');
        expect(result).toBe(false);
    });

    it('should return false for short password', () => {
        const result = validateLogin('user@example.com', 'short');
        expect(result).toBe(false);
    });
});