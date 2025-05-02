import React from 'react';
import { render, screen } from '@testing-library/react';
import PasswordResetSuccess from '../../components/PasswordResetSuccess';

/**
 * Unit tests for the PasswordResetSuccess component.
 */
describe('PasswordResetSuccess', () => {
    test('renders success message', () => {
        render(<PasswordResetSuccess />);
        const successMessage = screen.getByText(/Your password has been reset successfully!/i);
        expect(successMessage).toBeInTheDocument();
    });

    test('renders link to login', () => {
        render(<PasswordResetSuccess />);
        const loginLink = screen.getByRole('link', { name: /Login/i });
        expect(loginLink).toHaveAttribute('href', '/login');
    });
});