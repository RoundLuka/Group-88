// Modules
const express = require("express");
const cors = require("cors");
const morgan = require("morgan");
const mongoose = require('mongoose');
const dotenv = require("dotenv");
const userRouter = require("./routers/user.router");

// Server init
const app = express();

// Loading global envrionmental variables from .env file
dotenv.config()

// ---------- Middlewares -------------
// -------- Security Middleware ----------
app.use(cors());

// -------- Helper Middleware ------------
app.use(express.json());

// -------- Monitoring Middleware ----------
app.use(morgan('dev'));

// routers
app.use('/api/auth', userRouter)

// env - envrionment varaibles

mongoose.connect(process.env.MONGO_URI)
    .then(() => {
        console.log("Connceted to Mongo database!")

        // Running server
        app.listen(3000, () => console.log("Server running on port 3000!"))
    })
    .catch((err) => console.log(err));
