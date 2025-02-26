// dataController.js

const Data = require('../models/dataModel');

/**
 * Create a new data entry.
 * @param {Object} req - The request object containing the data to be created.
 * @param {Object} res - The response object used to send the response.
 */
const createDataEntry = async (req, res) => {
    try {
        const data = new Data(req.body);
        await data.save();
        res.status(201).json(data);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
};

/**
 * Get all data entries.
 * @param {Object} req - The request object.
 * @param {Object} res - The response object used to send the response.
 */
const getAllDataEntries = async (req, res) => {
    try {
        const dataEntries = await Data.find();
        res.status(200).json(dataEntries);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

/**
 * Get a data entry by ID.
 * @param {Object} req - The request object containing the ID.
 * @param {Object} res - The response object used to send the response.
 */
const getDataEntryById = async (req, res) => {
    try {
        const dataEntry = await Data.findById(req.params.id);
        if (!dataEntry) return res.status(404).json({ message: 'Data not found' });
        res.status(200).json(dataEntry);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

/**
 * Update a data entry by ID.
 * @param {Object} req - The request object containing the ID and update data.
 * @param {Object} res - The response object used to send the response.
 */
const updateDataEntryById = async (req, res) => {
    try {
        const dataEntry = await Data.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!dataEntry) return res.status(404).json({ message: 'Data not found' });
        res.status(200).json(dataEntry);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
};

/**
 * Delete a data entry by ID.
 * @param {Object} req - The request object containing the ID.
 * @param {Object} res - The response object used to send the response.
 */
const deleteDataEntryById = async (req, res) => {
    try {
        const dataEntry = await Data.findByIdAndDelete(req.params.id);
        if (!dataEntry) return res.status(404).json({ message: 'Data not found' });
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    createDataEntry,
    getAllDataEntries,
    getDataEntryById,
    updateDataEntryById,
    deleteDataEntryById
};