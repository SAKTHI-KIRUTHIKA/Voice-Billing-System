import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Signup.css";

const Signup = () => {
  const [email, setEmail] = useState("");
  const [storeName, setStoreName] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSignup = (e) => {
    e.preventDefault();
    const user = { email, storeName, password };
    localStorage.setItem("user", JSON.stringify(user));
    alert("Signup successful! Please login.");
    navigate("/login");
  };

  return (
    <div className="signup-container">
      <div className="signup-card">
        <h2 className="signup-title">Signup</h2>
        <form onSubmit={handleSignup}>
          <input
            type="email"
            placeholder="Email"
            className="signup-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="Store Name"
            className="signup-input"
            value={storeName}
            onChange={(e) => setStoreName(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            className="signup-input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit" className="signup-button">Sign Up</button>
        </form>
        <p className="signup-text">
          Already have an account? <a href="/login" className="signup-link">Login</a>
        </p>
      </div>
    </div>
  );
};

export default Signup;