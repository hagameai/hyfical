const authService = require('../utils/authService');

describe('Auth Service', () => {
    test('should hash passwords', () => {
        const password = 'password123';
        const hashedPassword = authService.hashPassword(password);
        expect(hashedPassword).not.toBe(password);
    });

    test('should validate password correctly', () => {
        const password = 'password123';
        const hashedPassword = authService.hashPassword(password);
        expect(authService.validatePassword(password, hashedPassword)).toBe(true);
        expect(authService.validatePassword('wrongpassword', hashedPassword)).toBe(false);
    });
});