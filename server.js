const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());


// CORS Middleware - CORS Middleware
app.use(cors({ origin: ['*'] }));

// Auth Middleware - Auth Middleware
const authMiddleware = (req, res, next) => {
    if (req.headers.authorization !== 'user' && req.headers.authorization !== 'admin') {
        return res.status(401).json({ message: "Unauthorized" });
    }
    next();
};

// Login Route - POST /login

app.post("/login", (req, res) => {
    res.json({ message: "Login successful" });
});

// Signup Route - POST /signup

app.post("/signup", (req, res) => {
    res.json({ message: "Signup successful" });
});

// Signout Route - POST /signout

app.post("/signout", (req, res) => {
    res.json({ message: "Signout successful" });
});                

// Admin Auth Middleware - Admin Auth Middleware
const adminMiddleware = (req, res, next) => {
    if (req.headers.authorization !== 'admin') {
        return res.status(403).json({ message: "Forbidden" });
    }
    next();
};

// User Route - GET /user

app.get("/user", authMiddleware, (req, res) => {
    res.json({ message: "User data" });
});        

// Admin Route - GET /admin

app.get("/admin", authMiddleware, adminMiddleware, (req, res) => {
    res.json({ message: "Admin data" });
});        

// Logging Middleware - Logging Middleware
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// Home Page - GET /home

app.get("/home", (req, res) => {
    res.json({ message: "Welcome to Home Page" });
});

// About Page - GET /about

app.get("/about", (req, res) => {
    res.json({ message: "About us" });
});

// News Page - GET /news

app.get("/news", (req, res) => {
    res.json({ message: "Latest news" });
});

// Blogs Page - GET /blogs

app.get("/blogs", (req, res) => {
    res.json({ message: "Blogs list" });
});

// Handle invalid routes    
app.use((req, res) => {
    res.status(404).json({ error: "Route not found" });
});

// run server on 3000 port     
app.listen(3000, () => console.log("Server running on 3000"));
