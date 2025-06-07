const { validatePasswordReset } = require('../../utils/passwordResetValidation');

describe('Password Reset Validation', () => {
    test('should return an error if email is not provided', () => {
        const result = validatePasswordReset({});
        expect(result).toHaveProperty('error');
        expect(result.error).toBe('Email is required');
    });

    test('should return an error if email is invalid', () => {
        const result = validatePasswordReset({ email: 'invalid-email' });
        expect(result).toHaveProperty('error');
        expect(result.error).toBe('Email is not valid');
    });

    test('should return success if email is valid', () => {
        const result = validatePasswordReset({ email: 'user@example.com' });
        expect(result).toHaveProperty('success');
        expect(result.success).toBe(true);
    });

    test('should return an error if password is not provided', () => {
        const result = validatePasswordReset({ email: 'user@example.com', password: '' });
        expect(result).toHaveProperty('error');
        expect(result.error).toBe('Password is required');
    });

    test('should return success if both email and password are valid', () => {
        const result = validatePasswordReset({ email: 'user@example.com', password: 'StrongPassword123!' });
        expect(result).toHaveProperty('success');
        expect(result.success).toBe(true);
    });
});