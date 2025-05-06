import React from 'react';
import { render, screen } from '@testing-library/react';
import PasswordResetError from '../../components/PasswordResetError';

describe('PasswordResetError Component', () => {
    test('renders error message correctly', () => {
        const errorMessage = 'There was an error resetting your password.';
        render(<PasswordResetError message={errorMessage} />);
        const errorElement = screen.getByText(/There was an error resetting your password./i);
        expect(errorElement).toBeInTheDocument();
    });

    test('renders without crashing', () => {
        render(<PasswordResetError message={''} />);
        const errorElement = screen.getByText(/Error/i);
        expect(errorElement).toBeInTheDocument();
    });
});