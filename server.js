const express = require('express');
const bodyParser = require('body-parser');

const port = 3000;
const app = express();

app.use(bodyParser.json());

app.post('/convert', (req, res) => {
    const amountInRs = req.body.amount_in_rs;
    const conversionRate = 0.0145;

    const amountInUsd = amountInRs * conversionRate;

    res.json({
        amount_in_usd: amountInUsd
    });
});

app.listen(port, () => {
    console.log(`Currency conversion service running on http://localhost:${port}`);
});