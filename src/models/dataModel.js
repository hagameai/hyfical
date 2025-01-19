const mongoose = require('mongoose');

// Define the schema for user-related data
const dataSchema = new mongoose.Schema({
    userId: {
        type: mongoose.Schema.Types.ObjectId,
        required: true,
        ref: 'User'
    },
    dataField: {
        type: String,
        required: true
    },
    createdAt: {
        type: Date,
        default: Date.now
    },
    updatedAt: {
        type: Date,
        default: Date.now
    }
});

// Create a model based on the schema
const DataModel = mongoose.model('Data', dataSchema);

module.exports = DataModel;