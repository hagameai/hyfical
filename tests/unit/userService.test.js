const userService = require('../../src/utils/authService');

describe('User Management Services', () => {
    test('should register a new user successfully', async () => {
        const userData = { username: 'testUser', password: 'testPassword' };
        const result = await userService.register(userData);
        expect(result).toHaveProperty('username', userData.username);
    });

    test('should not register a user with existing username', async () => {
        const userData = { username: 'existingUser', password: 'testPassword' };
        await userService.register(userData);
        await expect(userService.register(userData)).rejects.toThrow('User already exists');
    });

    test('should authenticate user with valid credentials', async () => {
        const userData = { username: 'validUser', password: 'validPassword' };
        await userService.register(userData);
        const result = await userService.login(userData);
        expect(result).toHaveProperty('token');
    });

    test('should not authenticate user with invalid password', async () => {
        const userData = { username: 'validUser', password: 'wrongPassword' };
        await expect(userService.login(userData)).rejects.toThrow('Invalid credentials');
    });

    test('should return user profile info', async () => {
        const userData = { username: 'validUser', password: 'validPassword' };
        await userService.register(userData);
        const loginResult = await userService.login(userData);
        const profile = await userService.getProfile(loginResult.token);
        expect(profile).toHaveProperty('username', userData.username);
    });
});