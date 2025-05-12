// Import necessary modules and dependencies
import { render, screen } from '@testing-library/react';
import LoginForm from '../components/LoginForm';

// Test suite for LoginForm validation logic
describe('LoginForm Validation', () => {
    // Test case for rendering the LoginForm component
    test('renders LoginForm component', () => {
        render(<LoginForm />);
        const emailInput = screen.getByLabelText(/email/i);
        const passwordInput = screen.getByLabelText(/password/i);
        const submitButton = screen.getByRole('button', { name: /login/i });

        // Check if inputs and button are in the document
        expect(emailInput).toBeInTheDocument();
        expect(passwordInput).toBeInTheDocument();
        expect(submitButton).toBeInTheDocument();
    });

    // Test case for email validation
    test('validates email input', () => {
        render(<LoginForm />);
        const emailInput = screen.getByLabelText(/email/i);
        const submitButton = screen.getByRole('button', { name: /login/i });

        // Submit form without entering email
        submitButton.click();
        // Assuming validation error message appears
        const errorMessage = screen.getByText(/please enter a valid email/i);
        expect(errorMessage).toBeInTheDocument();

        // Enter invalid email and submit
        fireEvent.change(emailInput, { target: { value: 'invalidEmail' } });
        submitButton.click();
        expect(errorMessage).toBeInTheDocument();

        // Enter valid email and submit
        fireEvent.change(emailInput, { target: { value: 'test@example.com' } });
        submitButton.click();
        expect(errorMessage).not.toBeInTheDocument();
    });

    // Test case for password validation
    test('validates password input', () => {
        render(<LoginForm />);
        const passwordInput = screen.getByLabelText(/password/i);
        const submitButton = screen.getByRole('button', { name: /login/i });

        // Submit form without entering password
        submitButton.click();
        const errorMessage = screen.getByText(/password is required/i);
        expect(errorMessage).toBeInTheDocument();

        // Enter password and submit
        fireEvent.change(passwordInput, { target: { value: 'password123' } });
        submitButton.click();
        expect(errorMessage).not.toBeInTheDocument();
    });
});
