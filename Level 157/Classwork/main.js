const nodemailer = require("nodemailer");

const transporter = nodemailer.createTransport({
    host: "sandbox.smtp.mailtrap.io",
    port: 2525,
    auth: {
        user: "თქვენი mailtrap სახელი",
        pass: "პაროლი",
    },
});

const sendMail = async (code) => {
    await transporter.sendMail({
    // from: "Newsletters <noreply@example.com>",
        to: "alice@example.com",
        subject: "Account verification",
        text: code
    });
} 

module.exports = sendMail;
ზურაბ შენგელია — 9:32 PM