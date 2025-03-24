const request = require('supertest');
const app = require('../src/app'); // Adjust the path as necessary

describe('User Authentication API', () => {
    it('should register a new user', async () => {
        const res = await request(app)
            .post('/api/auth/register')
            .send({ username: 'testuser', password: 'password123' });
        expect(res.statusCode).toEqual(201);
        expect(res.body).toHaveProperty('token');
    });

    it('should login a user', async () => {
        const res = await request(app)
            .post('/api/auth/login')
            .send({ username: 'testuser', password: 'password123' });
        expect(res.statusCode).toEqual(200);
        expect(res.body).toHaveProperty('token');
    });

    it('should fail to login with wrong credentials', async () => {
        const res = await request(app)
            .post('/api/auth/login')
            .send({ username: 'wronguser', password: 'wrongpassword' });
        expect(res.statusCode).toEqual(401);
    });
});