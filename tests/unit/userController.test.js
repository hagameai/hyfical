const request = require('supertest');
const app = require('../../api/auth');
const User = require('../../models/userModel');

// Mock user data
const mockUser = {
    username: 'testuser',
    password: 'testpassword'
};

describe('User Controller', () => {
    beforeAll(async () => {
        // Clean the database before tests
        await User.deleteMany();
    });

    afterEach(async () => {
        // Clean up after each test
        await User.deleteMany();
    });

    describe('POST /register', () => {
        it('should register a new user', async () => {
            const res = await request(app)
                .post('/api/register')
                .send(mockUser);
            expect(res.statusCode).toEqual(201);
            expect(res.body).toHaveProperty('message', 'User registered successfully.');
        });

        it('should return 400 for duplicate user', async () => {
            await request(app)
                .post('/api/register')
                .send(mockUser);
            const res = await request(app)
                .post('/api/register')
                .send(mockUser);
            expect(res.statusCode).toEqual(400);
            expect(res.body).toHaveProperty('error', 'User already exists.');
        });
    });

    describe('POST /login', () => {
        it('should login an existing user', async () => {
            await request(app)
                .post('/api/register')
                .send(mockUser);
            const res = await request(app)
                .post('/api/login')
                .send(mockUser);
            expect(res.statusCode).toEqual(200);
            expect(res.body).toHaveProperty('token');
        });

        it('should return 401 for invalid credentials', async () => {
            const res = await request(app)
                .post('/api/login')
                .send({ username: 'wronguser', password: 'wrongpassword' });
            expect(res.statusCode).toEqual(401);
            expect(res.body).toHaveProperty('error', 'Invalid credentials.');
        });
    });
});