// dataController.js

const DataModel = require('../models/dataModel');

/**
 * Create a new data entry.
 * @param {Object} req - The request object containing data details.
 * @param {Object} res - The response object.
 */
exports.createData = async (req, res) => {
    try {
        const newData = new DataModel(req.body);
        await newData.save();
        res.status(201).json({ message: 'Data created successfully', data: newData });
    } catch (error) {
        res.status(500).json({ message: 'Error creating data', error });
    }
};

/**
 * Retrieve all data entries.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 */
exports.getAllData = async (req, res) => {
    try {
        const dataEntries = await DataModel.find();
        res.status(200).json(dataEntries);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving data', error });
    }
};

/**
 * Retrieve a specific data entry by ID.
 * @param {Object} req - The request object containing the data ID.
 * @param {Object} res - The response object.
 */
exports.getDataById = async (req, res) => {
    try {
        const dataEntry = await DataModel.findById(req.params.id);
        if (!dataEntry) return res.status(404).json({ message: 'Data not found' });
        res.status(200).json(dataEntry);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving data', error });
    }
};

/**
 * Update a specific data entry by ID.
 * @param {Object} req - The request object containing the data ID and updated data.
 * @param {Object} res - The response object.
 */
exports.updateDataById = async (req, res) => {
    try {
        const updatedData = await DataModel.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updatedData) return res.status(404).json({ message: 'Data not found' });
        res.status(200).json({ message: 'Data updated successfully', data: updatedData });
    } catch (error) {
        res.status(500).json({ message: 'Error updating data', error });
    }
};

/**
 * Delete a specific data entry by ID.
 * @param {Object} req - The request object containing the data ID.
 * @param {Object} res - The response object.
 */
exports.deleteDataById = async (req, res) => {
    try {
        const deletedData = await DataModel.findByIdAndDelete(req.params.id);
        if (!deletedData) return res.status(404).json({ message: 'Data not found' });
        res.status(200).json({ message: 'Data deleted successfully' });
    } catch (error) {
        res.status(500).json({ message: 'Error deleting data', error });
    }
};