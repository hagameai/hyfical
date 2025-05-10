const request = require('supertest');
const app = require('../../src/api/auth'); // Adjust the path as necessary

describe('User Login Integration Tests', () => {
    // Test data
    const validUser = {
        email: 'user@example.com',
        password: 'password123'
    };

    const invalidUser = {
        email: 'wrong@example.com',
        password: 'wrongpassword'
    };

    it('should login a user with valid credentials', async () => {
        const response = await request(app)
            .post('/login')
            .send(validUser);

        expect(response.status).toBe(200);
        expect(response.body).toHaveProperty('token'); // Assuming token is returned on successful login
    });

    it('should not login a user with invalid credentials', async () => {
        const response = await request(app)
            .post('/login')
            .send(invalidUser);

        expect(response.status).toBe(401);
        expect(response.body).toHaveProperty('message', 'Invalid credentials'); // Assuming the message is returned on failure
    });

    it('should return 400 for missing fields', async () => {
        const response = await request(app)
            .post('/login')
            .send({}); // Sending empty body

        expect(response.status).toBe(400);
        expect(response.body).toHaveProperty('message', 'Email and password are required'); // Assuming this message is returned
    });
});