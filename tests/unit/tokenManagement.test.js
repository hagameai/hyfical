const authService = require('../../utils/authService');

describe('Token Management', () => {
    test('should create a token', () => {
        const userId = '123';
        const token = authService.createToken(userId);
        expect(token).toBeDefined();
        expect(typeof token).toBe('string');
    });

    test('should validate a token', () => {
        const userId = '123';
        const token = authService.createToken(userId);
        const isValid = authService.validateToken(token);
        expect(isValid).toBe(true);
    });

    test('should invalidate an incorrect token', () => {
        const isValid = authService.validateToken('invalidToken');
        expect(isValid).toBe(false);
    });
});