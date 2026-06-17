const express = require("express");
const { handleRegister } = require("../controllers/auth.controller");
const authRouter = express.Router();

authRouter.post('/signup', handleRegister)

module.exports = authRouter;