const request = require('supertest');
const app = require('../../src/api/auth'); // Adjust the path as necessary to point to your app

describe('User API Endpoints', () => {
  // Test for user registration
  test('POST /register - success', async () => {
    const response = await request(app)
      .post('/register')
      .send({ username: 'testuser', password: 'password123' });
    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('token');
  });

  // Test for user login
  test('POST /login - success', async () => {
    const response = await request(app)
      .post('/login')
      .send({ username: 'testuser', password: 'password123' });
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('token');
  });

  // Test for failed login due to incorrect credentials
  test('POST /login - failure', async () => {
    const response = await request(app)
      .post('/login')
      .send({ username: 'wronguser', password: 'wrongpassword' });
    expect(response.status).toBe(401);
    expect(response.body).toHaveProperty('error', 'Invalid credentials');
  });

  // Test for getting user profile
  test('GET /profile - success', async () => {
    const loginResponse = await request(app)
      .post('/login')
      .send({ username: 'testuser', password: 'password123' });

    const response = await request(app)
      .get('/profile')
      .set('Authorization', `Bearer ${loginResponse.body.token}`);
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('username', 'testuser');
  });

  // Test for unauthorized access to profile
  test('GET /profile - unauthorized', async () => {
    const response = await request(app)
      .get('/profile');
    expect(response.status).toBe(401);
    expect(response.body).toHaveProperty('error', 'No token provided');
  });
});