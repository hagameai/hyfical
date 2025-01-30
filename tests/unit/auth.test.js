const request = require('supertest');
const app = require('../src/app'); // Adjust path as necessary

describe('Authentication API', () => {
  it('should register a new user', async () => {
    const response = await request(app)
      .post('/api/auth/register')
      .send({ username: 'testuser', password: 'testpass' });
    expect(response.statusCode).toBe(201);
    expect(response.body).toHaveProperty('token');
  });

  it('should login with valid credentials', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({ username: 'testuser', password: 'testpass' });
    expect(response.statusCode).toBe(200);
    expect(response.body).toHaveProperty('token');
  });

  it('should not login with invalid credentials', async () => {
    const response = await request(app)
      .post('/api/auth/login')
      .send({ username: 'wronguser', password: 'wrongpass' });
    expect(response.statusCode).toBe(401);
  });
});