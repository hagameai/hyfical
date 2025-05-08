const mongoose = require('mongoose');
const User = require('../models/userModel');

// Sample user data for testing
const sampleUser = {
    username: 'testuser',
    password: 'Test123!',
    email: 'testuser@example.com'
};

describe('User Model Test', () => {
    beforeAll(async () => {
        // Connect to the database before running tests
        await mongoose.connect('mongodb://localhost:27017/hyfical_test', {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
    });

    afterAll(async () => {
        // Disconnect from the database after tests
        await mongoose.connection.close();
    });

    it('should create a user successfully', async () => {
        const user = new User(sampleUser);
        const savedUser = await user.save();
        expect(savedUser._id).toBeDefined();
        expect(savedUser.username).toBe(sampleUser.username);
        expect(savedUser.email).toBe(sampleUser.email);
    });

    it('should not create a user with an existing email', async () => {
        const user = new User(sampleUser);
        await user.save(); // Save first user

        const duplicateUser = new User(sampleUser);
        let error;
        try {
            await duplicateUser.save(); // Try to save duplicate user
        } catch (err) {
            error = err;
        }
        expect(error).toBeDefined();
        expect(error.errors.email).toBeDefined();
    });

    it('should not create a user without a username', async () => {
        const userWithoutUsername = new User({ ...sampleUser, username: '' });
        let error;
        try {
            await userWithoutUsername.save();
        } catch (err) {
            error = err;
        }
        expect(error).toBeDefined();
        expect(error.errors.username).toBeDefined();
    });

    it('should not create a user with a weak password', async () => {
        const weakPasswordUser = new User({ ...sampleUser, password: '12345' });
        let error;
        try {
            await weakPasswordUser.save();
        } catch (err) {
            error = err;
        }
        expect(error).toBeDefined();
        expect(error.errors.password).toBeDefined();
    });
});