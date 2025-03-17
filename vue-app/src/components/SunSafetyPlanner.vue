<template>
    <div class="container">
      <!-- Hero Section -->
      <div>
        <h2 class="hero-section">Your Personalised Sun Safety Plan</h2>
      </div>
  
      <!-- Skin Type Input Section -->
      <div class="search-section">
        <h2>Input Your Skin Type</h2>
        <p>Please input your skin type for personalised recommendations</p>
        
        <div class="skin-chart">
          <div v-for="(color, type) in skinColors" :key="type" class="skin-box">
            <div class="circle" :style="{ backgroundColor: color }"></div>
            <h3>Type {{ type }}</h3>
          </div>
        </div>
  
        <select class="form-select" v-model="userData.skinType">
          <option value="" disabled>Choose your skin type</option>
          <option v-for="(color, type) in skinColors" :key="type" :value="type">Skin Type {{ type }}</option>
        </select>
  
        <button @click="submitDetails">Submit</button>
        <button @click="clearForm" class="clear-btn">Clear</button>
      </div>
  
      <!-- Displaying Personalised Sun Protection Plan -->
      <div v-if="submittedForm" class="uv-info">
        <h2>Your Personalised Sun Protection Plan</h2>
        
        <div class="uv-data">
          <div>
            <strong>Sunscreen SPF Level:</strong> SPF 50+
          </div>
          <div>
            <strong>Recommended Sun Exposure:</strong> {{ skinTypeTime[userData.skinType] || "N/A" }}
          </div>
        </div>
      </div>
  
      <!-- Sun Protection Recommendations -->
      <div class="protection-section">
        <h2>Sun Protection Recommendations</h2>
        <p>Stay safe under the sun with these tips</p>
        <div class="tips">
          <div class="tip-box">
            <img :src="sunscreenImg" alt="Sunscreen" />
            <h3>Apply Sunscreen</h3>
            <p>Use SPF 30+ sunscreen</p>
          </div>
          <div class="tip-box">
            <img :src="hatImg" alt="Hat" />
            <h3>Wear Protective Clothing</h3>
            <p>Cover up with long sleeves and a hat</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const userData = ref({ skinType: "" });
  const submittedForm = ref(false);
  
  const skinColors = {
    I: "rgb(231,205,184)",
    II: "rgb(228,182,150)",
    III: "rgb(221,178,119)",
    IV: "rgb(194,134,88)",
    V: "rgb(141,99,56)",
    VI: "rgb(116,74,50)"
  };
  
  const skinTypeTime = {
    I: "10-15m",
    II: "15-20m",
    III: "20-30m",
    IV: "30-40m",
    V: "40-60m",
    VI: "60-80m"
  };
  
  const submitDetails = () => {
    if (!userData.value.skinType) {
      alert("Please select a skin type");
      return;
    }
    submittedForm.value = true;
  };
  
  const clearForm = () => {
    userData.value.skinType = "";
    submittedForm.value = false;
  };
  
  const sunscreenImg = new URL("../public/sunscreen.jpg", import.meta.url).href;
  const hatImg = new URL("../public/hat.png", import.meta.url).href;
  </script>
  
  <style scoped>
  /* General Container */
  .container {
    width: 90%;
    max-width: 1000px;
    margin: auto;
    padding: 20px;
  }
  
  /* Hero Section */
  .hero-section {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    background-color: #4a90e2;
    color: white;
    padding: 15px;
    border-radius: 5px;
  }
  
  /* Search Section */
  .search-section {
    text-align: center;
    margin: 40px 0;
  }
  
  .skin-chart {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }
  
  .skin-box {
    text-align: center;
  }
  
  .circle {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  /* Buttons */
  button {
    background-color: black;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
    margin: 10px;
  }
  
  .clear-btn {
    background-color: gray;
  }
  
  button:hover {
    background-color: #333;
  }
  
  /* UV Information */
  .uv-info {
    margin: 40px 0;
    text-align: center;
  }
  
  .uv-data {
    background: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  /* Protection Section */
  .protection-section {
    margin: 40px 0;
    text-align: center;
  }
  
  .tips {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
  }
  
  .tip-box {
    background: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 250px;
  }
  
  .tip-box img {
    width: 60px;
    height: 60px;
    margin-bottom: 10px;
  }
  
  .tip-box h3 {
    font-size: 18px;
    font-weight: bold;
  }
  
  .tip-box p {
    font-size: 14px;
    color: #555;
  }
  </style>
  