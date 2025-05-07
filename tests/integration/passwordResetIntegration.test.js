const request = require('supertest');
const app = require('../../src/api/auth');
const mongoose = require('mongoose');

// Test suite for password reset functionality
describe('Password Reset Integration Tests', () => {
  // Connect to the test database before running the tests
  beforeAll(async () => {
    await mongoose.connect('mongodb://localhost:27017/hyfical-test', { useNewUrlParser: true, useUnifiedTopology: true });
  });

  // Disconnect from the database after the tests are complete
  afterAll(async () => {
    await mongoose.connection.close();
  });

  test('should send password reset email', async () => {
    const response = await request(app)
      .post('/api/auth/password-reset')
      .send({ email: 'testuser@example.com' });

    expect(response.status).toBe(200);
    expect(response.body.message).toBe('Password reset email sent.');
  });

  test('should reset password successfully', async () => {
    const resetToken = 'valid-reset-token'; // This should normally be generated
    const newPassword = 'newPassword123';

    const response = await request(app)
      .post(`/api/auth/reset/${resetToken}`)
      .send({ password: newPassword });

    expect(response.status).toBe(200);
    expect(response.body.message).toBe('Password has been reset successfully.');
  });

  test('should return an error for invalid reset token', async () => {
    const invalidToken = 'invalid-reset-token';
    const response = await request(app)
      .post(`/api/auth/reset/${invalidToken}`)
      .send({ password: 'anotherPassword123' });

    expect(response.status).toBe(400);
    expect(response.body.message).toBe('Invalid or expired reset token.');
  });
});