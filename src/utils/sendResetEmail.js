const nodemailer = require('nodemailer');

/**
 * Sends a password reset email to the user.
 * 
 * @param {string} email - The email address of the user.
 * @param {string} resetToken - The token for resetting the password.
 * @returns {Promise<void>} - A promise that resolves when the email is sent.
 */
async function sendResetEmail(email, resetToken) {
    // Create a transporter object using SMTP
    const transporter = nodemailer.createTransport({
        host: 'smtp.example.com', // Replace with your SMTP server
        port: 587,
        secure: false, // true for 465, false for other ports
        auth: {
            user: process.env.SMTP_USER, // Your SMTP username
            pass: process.env.SMTP_PASS, // Your SMTP password
        },
    });

    // Email content
    const resetUrl = `https://yourapp.com/reset-password?token=${resetToken}`;
    const mailOptions = {
        from: 'no-reply@yourapp.com', // Sender address
        to: email, // List of receivers
        subject: 'Password Reset Request', // Subject line
        text: `You requested a password reset. Click the link to reset your password: ${resetUrl}`, // Plain text body
        html: `<p>You requested a password reset. Click the link to reset your password: <a href="${resetUrl}">Reset Password</a></p>`, // HTML body
    };

    // Send email
    return transporter.sendMail(mailOptions)
        .then(() => {
            console.log('Reset email sent successfully.');
        })
        .catch((error) => {
            console.error('Error sending reset email:', error);
            throw new Error('Could not send reset email.');
        });
}

module.exports = sendResetEmail;