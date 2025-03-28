const DataModel = require('../models/dataModel');

/**
 * Controller for handling data-related operations.
 */
class DataController {
    /**
     * Create a new data entry.
     * @param {Object} req - Request object containing data details.
     * @param {Object} res - Response object.
     */
    async createData(req, res) {
        try {
            const data = new DataModel(req.body);
            await data.save();
            res.status(201).json(data);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * Get all data entries.
     * @param {Object} req - Request object.
     * @param {Object} res - Response object.
     */
    async getAllData(req, res) {
        try {
            const data = await DataModel.find();
            res.status(200).json(data);
        } catch (error) {
            res.status(500).json({ message: error.message });
        }
    }

    /**
     * Get a specific data entry by ID.
     * @param {Object} req - Request object containing data ID.
     * @param {Object} res - Response object.
     */
    async getDataById(req, res) {
        try {
            const data = await DataModel.findById(req.params.id);
            if (!data) {
                return res.status(404).json({ message: 'Data not found' });
            }
            res.status(200).json(data);
        } catch (error) {
            res.status(500).json({ message: error.message });
        }
    }

    /**
     * Update a data entry by ID.
     * @param {Object} req - Request object containing data ID and update details.
     * @param {Object} res - Response object.
     */
    async updateData(req, res) {
        try {
            const data = await DataModel.findByIdAndUpdate(req.params.id, req.body, { new: true });
            if (!data) {
                return res.status(404).json({ message: 'Data not found' });
            }
            res.status(200).json(data);
        } catch (error) {
            res.status(400).json({ message: error.message });
        }
    }

    /**
     * Delete a data entry by ID.
     * @param {Object} req - Request object containing data ID.
     * @param {Object} res - Response object.
     */
    async deleteData(req, res) {
        try {
            const data = await DataModel.findByIdAndDelete(req.params.id);
            if (!data) {
                return res.status(404).json({ message: 'Data not found' });
            }
            res.status(204).send();
        } catch (error) {
            res.status(500).json({ message: error.message });
        }
    }
}

module.exports = new DataController();