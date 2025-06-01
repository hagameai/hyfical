const request = require('supertest');
const app = require('../../src/app');
const User = require('../../src/models/userModel');

// Mock user data for testing
const userData = {
    username: 'testuser',
    password: 'testpassword',
    email: 'testuser@example.com'
};

describe('User Routes', () => {
    // Clean up the database after each test
    afterEach(async () => {
        await User.deleteMany();
    });

    describe('POST /api/user/reset-password', () => {
        it('should reset the password for existing user', async () => {
            // Create a user
            await User.create(userData);
            const response = await request(app)
                .post('/api/user/reset-password')
                .send({ email: userData.email, newPassword: 'newpassword' });

            expect(response.status).toBe(200);
            expect(response.body.message).toBe('Password reset successful');
        });

        it('should return error for non-existing user', async () => {
            const response = await request(app)
                .post('/api/user/reset-password')
                .send({ email: 'nonexistent@example.com', newPassword: 'newpassword' });

            expect(response.status).toBe(404);
            expect(response.body.message).toBe('User not found');
        });
    });

    // Additional tests can be added here for other user routes
});