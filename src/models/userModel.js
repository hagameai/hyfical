const mongoose = require('mongoose');

// Define the schema for the User model
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Create the User model from the schema
const User = mongoose.model('User', userSchema);

module.exports = User;
