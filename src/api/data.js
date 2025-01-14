const express = require('express');
const router = express.Router();
const DataModel = require('../models/dataModel');

// Create new data
router.post('/', async (req, res) => {
    try {
        const newData = new DataModel(req.body);
        const savedData = await newData.save();
        res.status(201).json(savedData);
    } catch (err) {
        res.status(500).json(err);
    }
});

// Read all data
router.get('/', async (req, res) => {
    try {
        const data = await DataModel.find();
        res.status(200).json(data);
    } catch (err) {
        res.status(500).json(err);
    }
});

// Update data
router.put('/:id', async (req, res) => {
    try {
        const updatedData = await DataModel.findByIdAndUpdate(req.params.id, req.body, { new: true });
        res.status(200).json(updatedData);
    } catch (err) {
        res.status(500).json(err);
    }
});

// Delete data
router.delete('/:id', async (req, res) => {
    try {
        await DataModel.findByIdAndDelete(req.params.id);
        res.status(204).send();
    } catch (err) {
        res.status(500).json(err);
    }
});

module.exports = router;