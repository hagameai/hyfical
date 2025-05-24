const request = require('supertest');
const app = require('../../app'); // Assuming your Express app is exported from this file
const passwordResetController = require('../utils/passwordResetController');

// Mocking the password reset controller's dependencies if needed
jest.mock('../utils/passwordResetController');

describe('Password Reset Controller', () => {
  describe('POST /password-reset', () => {
    it('should return 200 and a success message for valid email', async () => {
      // Mock implementation for the controller function
      passwordResetController.sendResetEmail.mockImplementation(() => Promise.resolve());

      const response = await request(app)
        .post('/password-reset')
        .send({ email: 'test@example.com' });

      expect(response.status).toBe(200);
      expect(response.body).toEqual({ message: 'Reset email sent successfully.' });
    });

    it('should return 400 for invalid email', async () => {
      const response = await request(app)
        .post('/password-reset')
        .send({ email: 'invalid-email' });

      expect(response.status).toBe(400);
      expect(response.body).toEqual({ error: 'Invalid email format.' });
    });

    it('should return 404 for non-existent email', async () => {
      passwordResetController.sendResetEmail.mockImplementation(() => Promise.reject(new Error('User not found')));

      const response = await request(app)
        .post('/password-reset')
        .send({ email: 'notfound@example.com' });

      expect(response.status).toBe(404);
      expect(response.body).toEqual({ error: 'User not found.' });
    });
  });
});
