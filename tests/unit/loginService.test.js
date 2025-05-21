const { loginUser } = require('../../src/utils/authService');

describe('Login Management Services', () => {
  it('should return a token for valid credentials', async () => {
    const mockCredentials = { username: 'testuser', password: 'testpassword' };

    const token = await loginUser(mockCredentials);

    expect(token).toBeDefined();
    expect(typeof token).toBe('string');
  });

  it('should throw an error for invalid credentials', async () => {
    const mockInvalidCredentials = { username: 'wronguser', password: 'wrongpassword' };

    await expect(loginUser(mockInvalidCredentials)).rejects.toThrow('Invalid credentials');
  });

  it('should handle errors from the database gracefully', async () => {
    jest.spyOn(global, 'fetch').mockImplementation(() => {
      throw new Error('Database error');
    });

    await expect(loginUser({ username: 'testuser', password: 'testpassword' })).rejects.toThrow('Database error');

    global.fetch.mockRestore();
  });
});