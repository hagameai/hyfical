const { registerUser } = require('../src/api/auth');

describe('Registration Service', () => {
  it('should register a new user with valid credentials', async () => {
    const userData = {
      username: 'testuser',
      password: 'Password123!'
    };

    const result = await registerUser(userData);
    expect(result).toHaveProperty('success', true);
    expect(result).toHaveProperty('user');
    expect(result.user).toHaveProperty('username', userData.username);
  });

  it('should not register a user with an existing username', async () => {
    const userData = {
      username: 'existinguser',
      password: 'Password123!'
    };

    // Assuming the username already exists in the database
    const result = await registerUser(userData);
    expect(result).toHaveProperty('success', false);
    expect(result).toHaveProperty('message', 'Username already exists');
  });

  it('should not register a user with invalid password', async () => {
    const userData = {
      username: 'newuser',
      password: '123'
    };

    const result = await registerUser(userData);
    expect(result).toHaveProperty('success', false);
    expect(result).toHaveProperty('message', 'Password must be at least 8 characters long and contain a number and a special character');
  });

  it('should handle errors during registration', async () => {
    const userData = null;

    await expect(registerUser(userData)).rejects.toThrow('Invalid user data');
  });
});