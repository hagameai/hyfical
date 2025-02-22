const mongoose = require('mongoose');

// Define the user schema for MongoDB
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
    },
    password: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true,
        unique: true,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

// Create a User model based on the schema
const User = mongoose.model('User', userSchema);

module.exports = User;
