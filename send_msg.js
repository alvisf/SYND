const accountSid = "AC77ca0614a6d1238cffaac5e095139f83";
const authToken = "749bf3da242c6716be74bf2e1465805f";
const client = require("twilio")(accountSid, authToken);

client.messages
  .create({
    from: "whatsapp:+14155238886",
    to: "whatsapp:+919677051645",
    body: "hdhfgdg"
  })
  .then(message => console.log(message.sid));

var express = require("express");
var bodyParser = require("body-parser");
var multer = require("multer");
var upload = multer();
var app = express();

app.get("/", function(req, res) {
  res.render("form");
});

app.set("view engine", "pug");
app.set("views", "./views");

// for parsing application/json
app.use(bodyParser.json());

// for parsing application/xwww-
app.use(bodyParser.urlencoded({ extended: true }));
//form-urlencoded

// for parsing multipart/form-data
app.use(upload.array());
app.use(express.static("public"));

app.post("/", function(req, res) {
  console.log(req.body);
  res.send("recieved your request!");
});
app.listen(3000);
