const { validateUser, validateUserUpdate } = require('../../src/api/userController');

describe('User Controller Validation', () => {
    describe('validateUser', () => {
        it('should return an error if username is missing', () => {
            const userData = { password: 'password123' };
            const result = validateUser(userData);
            expect(result).toHaveProperty('error');
            expect(result.error).toBe('Username is required.');
        });

        it('should return an error if password is missing', () => {
            const userData = { username: 'testuser' };
            const result = validateUser(userData);
            expect(result).toHaveProperty('error');
            expect(result.error).toBe('Password is required.');
        });

        it('should return valid user data when all fields are correct', () => {
            const userData = { username: 'testuser', password: 'password123' };
            const result = validateUser(userData);
            expect(result).toHaveProperty('valid');
            expect(result.valid).toBe(true);
        });
    });

    describe('validateUserUpdate', () => {
        it('should return an error if userId is missing', () => {
            const updateData = { username: 'newusername' };
            const result = validateUserUpdate(updateData);
            expect(result).toHaveProperty('error');
            expect(result.error).toBe('User ID is required for update.');
        });

        it('should return valid update data when userId is provided', () => {
            const updateData = { userId: '1234', username: 'newusername' };
            const result = validateUserUpdate(updateData);
            expect(result).toHaveProperty('valid');
            expect(result.valid).toBe(true);
        });

        it('should return an error if username is empty', () => {
            const updateData = { userId: '1234', username: '' };
            const result = validateUserUpdate(updateData);
            expect(result).toHaveProperty('error');
            expect(result.error).toBe('Username cannot be empty.');
        });
    });
});