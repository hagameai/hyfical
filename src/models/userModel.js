const mongoose = require('mongoose');

// Define the user schema for MongoDB
const userSchema = new mongoose.Schema({
    username: {
        type: String,
        required: true,
        unique: true,
        trim: true
    },
    password: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true,
        trim: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    }
});

// Create the user model based on the schema
const User = mongoose.model('User', userSchema);

// Export the model for use in other parts of the application
module.exports = User;