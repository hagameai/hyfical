const mongoose = require('mongoose');

// Define the user schema with the necessary fields and validation rules
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
        trim: true,
    },
    password: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true,
        unique: true,
        trim: true,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

// Create a model based on the user schema
const User = mongoose.model('User', userSchema);

module.exports = User; // Export the User model for use in other modules