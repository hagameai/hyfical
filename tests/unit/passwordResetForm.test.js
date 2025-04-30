import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import PasswordResetForm from '../../components/PasswordResetForm';

// Mocking the function to simulate API call
jest.mock('../../api/authService', () => ({
  sendResetEmail: jest.fn(() => Promise.resolve()),
}));

describe('PasswordResetForm Component', () => {
  test('renders PasswordResetForm', () => {
    render(<PasswordResetForm />);
    const emailInput = screen.getByPlaceholderText(/email/i);
    const submitButton = screen.getByRole('button', { name: /reset password/i });

    expect(emailInput).toBeInTheDocument();
    expect(submitButton).toBeInTheDocument();
  });

  test('submits the form with valid email', async () => {
    render(<PasswordResetForm />);
    const emailInput = screen.getByPlaceholderText(/email/i);
    const submitButton = screen.getByRole('button', { name: /reset password/i });

    fireEvent.change(emailInput, { target: { value: 'test@example.com' } });
    fireEvent.click(submitButton);

    // Expect the email input to be cleared after submission
    expect(emailInput.value).toBe('');
    // Here, you would check for API call or success message
  });

  test('shows error message with invalid email', async () => {
    render(<PasswordResetForm />);
    const emailInput = screen.getByPlaceholderText(/email/i);
    const submitButton = screen.getByRole('button', { name: /reset password/i });

    fireEvent.change(emailInput, { target: { value: 'invalid-email' } });
    fireEvent.click(submitButton);

    const errorMessage = await screen.findByText(/please enter a valid email/i);
    expect(errorMessage).toBeInTheDocument();
  });
});