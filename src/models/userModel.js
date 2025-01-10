const mongoose = require('mongoose');

// Define the schema for the user model
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
        minlength: 3,
        maxlength: 30,
    },
    password: {
        type: String,
        required: true,
        minlength: 6,
    },
    email: {
        type: String,
        required: true,
        unique: true,
        match: /[a-z0-9]+@[a-z]++.[a-z]{2,3}/,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

// Create the user model from the schema
const User = mongoose.model('User', userSchema);

module.exports = User;