const express = require('express');

const app = express();

// serve static files from the 'public' directory
app.use(express.static('Frontend'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/Frontend/index.html');
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});