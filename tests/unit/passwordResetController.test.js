const request = require('supertest');
const app = require('../../../../app'); // Make sure to import your app instance
const passwordResetController = require('../../utils/passwordResetController');

describe('Password Reset Controller', () => {
    it('should request a password reset', async () => {
        const response = await request(app)
            .post('/api/password-reset')
            .send({ email: 'user@example.com' });

        expect(response.status).toBe(200);
        expect(response.body.message).toBe('Password reset email sent.');
    });

    it('should fail if email is not registered', async () => {
        const response = await request(app)
            .post('/api/password-reset')
            .send({ email: 'nonexistent@example.com' });

        expect(response.status).toBe(404);
        expect(response.body.message).toBe('Email not found.');
    });

    it('should reset the password', async () => {
        const response = await request(app)
            .post('/api/password-reset/confirm')
            .send({ token: 'validToken', newPassword: 'newStrongPassword123!' });

        expect(response.status).toBe(200);
        expect(response.body.message).toBe('Password has been reset successfully.');
    });

    it('should fail to reset the password with an invalid token', async () => {
        const response = await request(app)
            .post('/api/password-reset/confirm')
            .send({ token: 'invalidToken', newPassword: 'newStrongPassword123!' });

        expect(response.status).toBe(400);
        expect(response.body.message).toBe('Invalid or expired token.');
    });
});