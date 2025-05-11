const { validateUserModel } = require('../../models/userModel');

describe('User Model Validation', () => {
  test('should validate a valid user model', () => {
    const userModel = {
      username: 'testUser',
      password: 'securePassword123',
      email: 'test@example.com'
    };
    const validationResult = validateUserModel(userModel);
    expect(validationResult).toBe(true);
  });

  test('should invalidate a user model with missing username', () => {
    const userModel = {
      password: 'securePassword123',
      email: 'test@example.com'
    };
    const validationResult = validateUserModel(userModel);
    expect(validationResult).toBe(false);
  });

  test('should invalidate a user model with invalid email', () => {
    const userModel = {
      username: 'testUser',
      password: 'securePassword123',
      email: 'invalidEmail'
    };
    const validationResult = validateUserModel(userModel);
    expect(validationResult).toBe(false);
  });

  test('should invalidate a user model with short password', () => {
    const userModel = {
      username: 'testUser',
      password: 'short',
      email: 'test@example.com'
    };
    const validationResult = validateUserModel(userModel);
    expect(validationResult).toBe(false);
  });
});