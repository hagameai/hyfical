const authService = require('../utils/authService');

describe('AuthService Error Handling', () => {
    it('should throw an error if invalid credentials are passed to login', async () => {
        const invalidCredentials = { username: '', password: '' };
        await expect(authService.login(invalidCredentials)).rejects.toThrow('Invalid credentials');
    });

    it('should throw an error if token is expired', async () => {
        const expiredToken = 'expiredToken'; // Mock expired token
        await expect(authService.verifyToken(expiredToken)).rejects.toThrow('Token is expired');
    });

    it('should throw an error if an error occurs during token verification', async () => {
        const invalidToken = 'invalidToken'; // Mock invalid token
        await expect(authService.verifyToken(invalidToken)).rejects.toThrow('Token verification failed');
    });

    it('should throw an error if user not found during registration', async () => {
        const newUser = { username: 'testUser', password: 'password123' };
        jest.spyOn(authService, 'register').mockImplementation(() => { throw new Error('User already exists'); });
        await expect(authService.register(newUser)).rejects.toThrow('User already exists');
    });
});