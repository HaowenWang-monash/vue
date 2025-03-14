<template>
    <div class="container">
      <div>
        <h2 class="hero-section">Promoting Sun Protection Across Communities</h2>
      </div>
  
      <div class="contact-section">
        <h2>Write to Us</h2>
        <p>Have a question or feedback? Drop us a message!</p>
        <form @submit.prevent="sendMessage">
          <input type="text" v-model="name" placeholder="Enter your name" required />
          <input type="email" v-model="email" placeholder="Enter your email" required />
          <textarea v-model="message" placeholder="Type your message here" required></textarea>
          <button type="submit" :disabled="loading">
            {{ loading ? "Sending..." : "Send Message" }}
          </button>
        </form>
        <p v-if="successMessage" class="success">{{ successMessage }}</p>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </div>
  
      <div class="about-section">
        <h2>About Us</h2>
        <p>Our mission is to promote sun protection and raise awareness about the importance of sun safety in various communities.</p>
        <div class="about-cards">
          <div class="card">
            <h3>Our Mission</h3>
            <p>To educate and inspire people to protect themselves from the harmful effects of the sun.</p>
            <span>🌞 SunWise Team</span>
          </div>
          <div class="card">
            <h3>The Problem</h3>
            <p>Many people underestimate the risks associated with sun exposure, leading to increased cases of skin damage.</p>
            <span>🌞 SunWise Team</span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: "",
        email: "",
        message: "",
        successMessage: "",
        errorMessage: "",
        loading: false,
      };
    },
    methods: {
      async sendMessage() {
        if (!this.name || !this.email || !this.message) {
          this.errorMessage = "All fields are required!";
          return;
        }
  
        this.loading = true;
        this.successMessage = "";
        this.errorMessage = "";
  
        try {
          const response = await fetch("http://localhost:5000/api/messages", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              name: this.name,
              email: this.email,
              message: this.message,
            }),
          });
  
          const result = await response.json();
  
          if (response.ok) {
            this.successMessage = "Message sent successfully!";
            this.name = "";
            this.email = "";
            this.message = "";
          } else {
            this.errorMessage = result.error || "Failed to send message.";
          }
        } catch (error) {
          this.errorMessage = "Server error. Please try again later.";
        } finally {
          this.loading = false;
        }
      },
    },
  };
  </script>
  