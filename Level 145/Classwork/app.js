const User = require("../models/user.model");
const catchAsync = require("../util/catchAsync");

const register = catchAsync(async (req, res, next) => {
    const {username, email, password} = req.body;

    await User.create({username, email, password});

    res.status(201).json({
        status: 'success',
        message: "Account  created successfuly"
    })
});

const login = catchAsync(async (req, res, next) => {
    const {email, password} = req.body;

    const found = await User.find({email, password});

    if(!found) {
        return new AppError('Email or password incorrect', 404)
    }
    res.status(201).json({
        status: 'success',
        message: "Account  created successfuly"
    })
});

module.exports = {
    register,
    login
}