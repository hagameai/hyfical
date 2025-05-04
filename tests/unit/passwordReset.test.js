// Import the necessary modules for testing
const passwordReset = require('../../utils/passwordReset');
const { sendResetEmail } = require('../../utils/sendResetEmail');

// Mock the sendResetEmail function
jest.mock('../../utils/sendResetEmail');

describe('Password Reset Logic', () => {
    test('should generate a reset token', () => {
        const email = 'user@example.com';
        const token = passwordReset.generateResetToken(email);
        expect(token).toBeDefined();
        expect(token).toBeTruthy();
    });

    test('should send reset email', async () => {
        const email = 'user@example.com';
        await passwordReset.sendResetEmail(email);
        expect(sendResetEmail).toHaveBeenCalledWith(email);
    });

    test('should handle errors when sending email', async () => {
        sendResetEmail.mockImplementationOnce(() => {
            throw new Error('Email service failed');
        });
        await expect(passwordReset.sendResetEmail('user@example.com')).rejects.toThrow('Email service failed');
    });

    test('should validate reset token', () => {
        const email = 'user@example.com';
        const token = passwordReset.generateResetToken(email);
        const isValid = passwordReset.validateResetToken(token);
        expect(isValid).toBe(true);
    });

    test('should invalidate expired token', () => {
        const expiredToken = 'expiredToken'; // Simulate an expired token
        const isValid = passwordReset.validateResetToken(expiredToken);
        expect(isValid).toBe(false);
    });
});
