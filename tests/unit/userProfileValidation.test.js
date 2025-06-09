const { validateUserProfile } = require('../../src/utils/userProfileValidation');

describe('User Profile Validation', () => {
    test('should return true for valid user profile', () => {
        const validProfile = {
            username: 'testUser',
            email: 'test@example.com',
            age: 25
        };
        expect(validateUserProfile(validProfile)).toBe(true);
    });

    test('should return false for invalid username', () => {
        const invalidProfile = {
            username: '', // empty username
            email: 'test@example.com',
            age: 25
        };
        expect(validateUserProfile(invalidProfile)).toBe(false);
    });

    test('should return false for invalid email', () => {
        const invalidProfile = {
            username: 'testUser',
            email: 'invalidEmail', // invalid email format
            age: 25
        };
        expect(validateUserProfile(invalidProfile)).toBe(false);
    });

    test('should return false for invalid age', () => {
        const invalidProfile = {
            username: 'testUser',
            email: 'test@example.com',
            age: -5 // negative age
        };
        expect(validateUserProfile(invalidProfile)).toBe(false);
    });

    test('should return false for missing fields', () => {
        const invalidProfile = {
            username: 'testUser',
            // email is missing
            age: 25
        };
        expect(validateUserProfile(invalidProfile)).toBe(false);
    });
});