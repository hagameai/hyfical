// dataController.js

const DataModel = require('../models/dataModel');

/**
 * Get all data entries
 * @returns {Promise<Array>} List of data entries
 */
const getAllData = async () => {
    return await DataModel.find();
};

/**
 * Get a specific data entry by ID
 * @param {string} id - The ID of the data entry
 * @returns {Promise<Object>} The data entry
 */
const getDataById = async (id) => {
    return await DataModel.findById(id);
};

/**
 * Create a new data entry
 * @param {Object} data - The data to create
 * @returns {Promise<Object>} The created data entry
 */
const createData = async (data) => {
    const newData = new DataModel(data);
    return await newData.save();
};

/**
 * Update an existing data entry
 * @param {string} id - The ID of the data entry to update
 * @param {Object} data - The updated data
 * @returns {Promise<Object>} The updated data entry
 */
const updateData = async (id, data) => {
    return await DataModel.findByIdAndUpdate(id, data, { new: true });
};

/**
 * Delete a data entry
 * @param {string} id - The ID of the data entry to delete
 * @returns {Promise<Object>} The deleted data entry
 */
const deleteData = async (id) => {
    return await DataModel.findByIdAndDelete(id);
};

module.exports = {
    getAllData,
    getDataById,
    createData,
    updateData,
    deleteData
};