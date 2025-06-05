const request = require('supertest');
const app = require('../../app'); // Adjust the path to your main app file
const UserProfileController = require('../controllers/userProfileController');

// Mock UserProfileController methods for testing
jest.mock('../controllers/userProfileController');

describe('UserProfileController', () => {
    describe('GET /user/profile', () => {
        it('should return user profile data', async () => {
            // Arrange
            const mockUserProfile = { name: 'John Doe', email: 'john@example.com' };
            UserProfileController.getUserProfile.mockImplementation((req, res) => {
                res.status(200).json(mockUserProfile);
            });

            // Act
            const response = await request(app).get('/user/profile');

            // Assert
            expect(response.statusCode).toBe(200);
            expect(response.body).toEqual(mockUserProfile);
        });
    });

    describe('PUT /user/profile', () => {
        it('should update user profile data', async () => {
            // Arrange
            const updatedProfile = { name: 'Jane Doe', email: 'jane@example.com' };
            UserProfileController.updateUserProfile.mockImplementation((req, res) => {
                res.status(200).json(updatedProfile);
            });

            // Act
            const response = await request(app)
                .put('/user/profile')
                .send(updatedProfile);

            // Assert
            expect(response.statusCode).toBe(200);
            expect(response.body).toEqual(updatedProfile);
        });
    });
});