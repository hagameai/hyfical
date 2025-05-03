const sendResetEmail = require('../../utils/sendResetEmail');

describe('sendResetEmail', () => {
    it('should send an email with the correct parameters', async () => {
        const mockEmailService = jest.fn();
        const mockEmail = 'test@example.com';
        const mockToken = 'dummyToken';

        // Mock the email service
        jest.mock('../../utils/sendResetEmail', () => {
            return jest.fn().mockImplementation((email, token) => {
                mockEmailService(email, token);
                return Promise.resolve();
            });
        });

        await sendResetEmail(mockEmail, mockToken);

        expect(mockEmailService).toHaveBeenCalledWith(mockEmail, mockToken);
    });

    it('should throw an error if email is invalid', async () => {
        const mockEmail = 'invalid-email';
        const mockToken = 'dummyToken';

        await expect(sendResetEmail(mockEmail, mockToken)).rejects.toThrow('Invalid email address');
    });

    it('should handle errors during email sending', async () => {
        const mockEmail = 'test@example.com';
        const mockToken = 'dummyToken';

        // Mock the email service to throw an error
        jest.mock('../../utils/sendResetEmail', () => {
            return jest.fn().mockImplementation(() => {
                throw new Error('Email service error');
            });
        });

        await expect(sendResetEmail(mockEmail, mockToken)).rejects.toThrow('Email service error');
    });
});