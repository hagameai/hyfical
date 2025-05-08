const request = require('supertest');
const app = require('../../api/authController');

describe('Auth Controller', () => {
    it('should register a new user successfully', async () => {
        const response = await request(app)
            .post('/api/auth/register')
            .send({ username: 'testuser', password: 'testpassword' });
        expect(response.status).toBe(201);
        expect(response.body).toHaveProperty('message', 'User registered successfully');
    });

    it('should fail to register an existing user', async () => {
        await request(app)
            .post('/api/auth/register')
            .send({ username: 'testuser', password: 'testpassword' }); // First registration
        const response = await request(app)
            .post('/api/auth/register')
            .send({ username: 'testuser', password: 'testpassword' });
        expect(response.status).toBe(400);
        expect(response.body).toHaveProperty('message', 'User already exists');
    });

    it('should login an existing user successfully', async () => {
        await request(app)
            .post('/api/auth/register')
            .send({ username: 'testuser', password: 'testpassword' });
        const response = await request(app)
            .post('/api/auth/login')
            .send({ username: 'testuser', password: 'testpassword' });
        expect(response.status).toBe(200);
        expect(response.body).toHaveProperty('token');
    });

    it('should fail to login with incorrect credentials', async () => {
        const response = await request(app)
            .post('/api/auth/login')
            .send({ username: 'wronguser', password: 'wrongpassword' });
        expect(response.status).toBe(401);
        expect(response.body).toHaveProperty('message', 'Invalid credentials');
    });
});