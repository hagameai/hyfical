// src/api/data.js

const express = require('express');
const router = express.Router();
const DataModel = require('../models/dataModel');

// Create new data
router.post('/', async (req, res) => {
    try {
        const data = new DataModel(req.body);
        await data.save();
        res.status(201).send(data);
    } catch (error) {
        res.status(400).send(error);
    }
});

// Read data
router.get('/', async (req, res) => {
    try {
        const data = await DataModel.find();
        res.status(200).send(data);
    } catch (error) {
        res.status(500).send(error);
    }
});

// Update data
router.patch('/:id', async (req, res) => {
    try {
        const data = await DataModel.findByIdAndUpdate(req.params.id, req.body, { new: true, runValidators: true });
        if (!data) {
            return res.status(404).send();
        }
        res.status(200).send(data);
    } catch (error) {
        res.status(400).send(error);
    }
});

// Delete data
router.delete('/:id', async (req, res) => {
    try {
        const data = await DataModel.findByIdAndDelete(req.params.id);
        if (!data) {
            return res.status(404).send();
        }
        res.status(200).send(data);
    } catch (error) {
        res.status(500).send(error);
    }
});

module.exports = router;