const express = require('express');
const router = express.Router();
const DataModel = require('../models/dataModel');

// Create a new data entry
router.post('/', async (req, res) => {
    try {
        const newData = new DataModel(req.body);
        await newData.save();
        res.status(201).json(newData);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Get all data entries
router.get('/', async (req, res) => {
    try {
        const data = await DataModel.find();
        res.status(200).json(data);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

// Update a data entry
router.put('/:id', async (req, res) => {
    try {
        const updatedData = await DataModel.findByIdAndUpdate(req.params.id, req.body, { new: true });
        res.status(200).json(updatedData);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

// Delete a data entry
router.delete('/:id', async (req, res) => {
    try {
        await DataModel.findByIdAndDelete(req.params.id);
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

module.exports = router;
