const request = require('supertest');
const express = require('express');
const passwordResetRoutes = require('../utils/passwordResetRoutes');

const app = express();

// Middleware to parse JSON
app.use(express.json());

// Use the password reset routes
app.use('/api/reset', passwordResetRoutes);

describe('Password Reset Routes', () => {
  it('should send a password reset email', async () => {
    const response = await request(app)
      .post('/api/reset/request')
      .send({ email: 'test@example.com' });

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('message', 'Reset email sent successfully.');
  });

  it('should reset password', async () => {
    const response = await request(app)
      .post('/api/reset/confirm')
      .send({ token: 'valid-reset-token', newPassword: 'newPassword123' });

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('message', 'Password has been reset successfully.');
  });

  it('should return 400 for invalid token', async () => {
    const response = await request(app)
      .post('/api/reset/confirm')
      .send({ token: 'invalid-token', newPassword: 'newPassword123' });

    expect(response.status).toBe(400);
    expect(response.body).toHaveProperty('error', 'Invalid reset token.');
  });
});
