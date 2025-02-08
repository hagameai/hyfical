const mongoose = require('mongoose');

// Create a user schema for MongoDB with validation rules
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
        minlength: 3,
        maxlength: 30
    },
    password: {
        type: String,
        required: true,
        minlength: 6
    },
    email: {
        type: String,
        required: true,
        unique: true,
        match: /.+@.+\..+/ // Simple email regex
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Create a User model from the schema
const User = mongoose.model('User', userSchema);

module.exports = User;