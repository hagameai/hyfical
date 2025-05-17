const jwt = require('jsonwebtoken');
const { createToken, validateToken } = require('../utils/tokenManagement');

// Mock secret key for testing
const secretKey = 'your_secret_key';

/**
 * Unit tests for token management services.
 */
describe('Token Management Services', () => {
  let token;

  beforeAll(() => {
    // Create a token before running tests
    token = createToken({ userId: '123' }, secretKey);
  });

  test('should create a valid JWT token', () => {
    expect(token).toBeDefined();
    expect(typeof token).toBe('string');
  });

  test('should validate a valid JWT token', () => {
    const decoded = validateToken(token, secretKey);
    expect(decoded).toBeDefined();
    expect(decoded.userId).toBe('123');
  });

  test('should not validate an invalid JWT token', () => {
    const invalidToken = token + 'invalid'; // Create an invalid token
    const decoded = validateToken(invalidToken, secretKey);
    expect(decoded).toBeNull();
  });

  test('should handle token expiration', () => {
    // Create a token with a short expiration
    const expiredToken = jwt.sign({ userId: '123' }, secretKey, { expiresIn: '1ms' });
    // Wait for the token to expire
    setTimeout(() => {
      const decoded = validateToken(expiredToken, secretKey);
      expect(decoded).toBeNull();
    }, 5);
  });
});
