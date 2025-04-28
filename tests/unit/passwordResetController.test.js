const request = require('supertest');
const app = require('../../app'); // Make sure to adjust the path to your main app file
const PasswordResetController = require('../../api/passwordResetController');

describe('Password Reset Controller', () => {
    describe('POST /api/reset-password', () => {
        it('should send a reset email for a valid user', async () => {
            const response = await request(app)
                .post('/api/reset-password')
                .send({ email: 'testuser@example.com' });
            expect(response.status).toBe(200);
            expect(response.body.message).toBe('Reset email sent successfully.');
        });

        it('should return an error if the email is not registered', async () => {
            const response = await request(app)
                .post('/api/reset-password')
                .send({ email: 'nonexistentuser@example.com' });
            expect(response.status).toBe(404);
            expect(response.body.message).toBe('User not found.');
        });

        it('should return an error if email is invalid', async () => {
            const response = await request(app)
                .post('/api/reset-password')
                .send({ email: 'invalid-email' });
            expect(response.status).toBe(400);
            expect(response.body.message).toBe('Invalid email format.');
        });
    });
});