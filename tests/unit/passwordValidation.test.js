// passwordValidation.test.js

import { validatePassword } from '../utils/passwordValidation';

describe('Password Validation Utility', () => {
  test('valid password should return true', () => {
    const validPassword = 'StrongPassw0rd!';
    expect(validatePassword(validPassword)).toBe(true);
  });

  test('password without uppercase should return false', () => {
    const invalidPassword = 'weakpassword1!';
    expect(validatePassword(invalidPassword)).toBe(false);
  });

  test('password without lowercase should return false', () => {
    const invalidPassword = 'WEAKPASSWORD1!';
    expect(validatePassword(invalidPassword)).toBe(false);
  });

  test('password without number should return false', () => {
    const invalidPassword = 'WeakPassword!';
    expect(validatePassword(invalidPassword)).toBe(false);
  });

  test('password without special character should return false', () => {
    const invalidPassword = 'WeakPassword1';
    expect(validatePassword(invalidPassword)).toBe(false);
  });
  
  test('password shorter than 8 characters should return false', () => {
    const invalidPassword = 'Short1!';
    expect(validatePassword(invalidPassword)).toBe(false);
  });
});
