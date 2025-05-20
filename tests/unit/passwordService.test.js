const bcrypt = require('bcrypt');
const passwordService = require('../../src/utils/passwordValidation');

/**
 * Unit tests for password management services.
 */
describe('Password Management Service', () => {
    const validPassword = 'StrongPassword123!';
    const invalidPassword = 'weakpass';
    const hash = bcrypt.hashSync(validPassword, 10);

    test('should hash a valid password', () => {
        const hashedPassword = passwordService.hashPassword(validPassword);
        expect(hashedPassword).not.toBe(validPassword);
        expect(bcrypt.compareSync(validPassword, hashedPassword)).toBe(true);
    });

    test('should return false for invalid password verification', () => {
        const isMatch = passwordService.verifyPassword(invalidPassword, hash);
        expect(isMatch).toBe(false);
    });

    test('should return true for valid password verification', () => {
        const isMatch = passwordService.verifyPassword(validPassword, hash);
        expect(isMatch).toBe(true);
    });

    test('should throw an error for empty password', () => {
        expect(() => passwordService.hashPassword('')).toThrow('Password cannot be empty');
    });
});
