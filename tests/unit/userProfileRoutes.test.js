const request = require('supertest');
const app = require('../../app'); // Adjust the path to your app
const mongoose = require('mongoose');
const UserProfile = require('../../models/userProfileModel'); // Adjust based on your actual model path

// Sample user profile data for testing
const sampleProfile = {
    userId: '60b8d6a0b6c0f64a68c3a5c3', // Replace with a valid userId
    name: 'John Doe',
    email: 'john@example.com',
    age: 30
};

beforeAll(async () => {
    await mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true, useUnifiedTopology: true });
});

afterAll(async () => {
    await UserProfile.deleteMany(); // Cleanup the database
    await mongoose.connection.close();
});

describe('User Profile Routes', () => {
    // Test for creating a user profile
    it('should create a new user profile', async () => {
        const response = await request(app)
            .post('/api/profiles') // Adjust the path based on your routes
            .send(sampleProfile);
        expect(response.statusCode).toBe(201);
        expect(response.body).toHaveProperty('_id');
        expect(response.body.name).toBe(sampleProfile.name);
        expect(response.body.email).toBe(sampleProfile.email);
    });

    // Test for retrieving a user profile
    it('should retrieve a user profile', async () => {
        const profile = await UserProfile.create(sampleProfile);
        const response = await request(app)
            .get(`/api/profiles/${profile._id}`); // Adjust the path based on your routes
        expect(response.statusCode).toBe(200);
        expect(response.body.name).toBe(profile.name);
        expect(response.body.email).toBe(profile.email);
    });

    // Test for updating a user profile
    it('should update a user profile', async () => {
        const profile = await UserProfile.create(sampleProfile);
        const updatedProfile = { ...sampleProfile, name: 'Jane Doe' };
        const response = await request(app)
            .put(`/api/profiles/${profile._id}`)
            .send(updatedProfile);
        expect(response.statusCode).toBe(200);
        expect(response.body.name).toBe(updatedProfile.name);
    });

    // Test for deleting a user profile
    it('should delete a user profile', async () => {
        const profile = await UserProfile.create(sampleProfile);
        const response = await request(app)
            .delete(`/api/profiles/${profile._id}`);
        expect(response.statusCode).toBe(204);
    });
});
