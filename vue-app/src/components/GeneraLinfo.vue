<template>
    <div class="container">
      <!-- Hero Section -->
      <div>
        <h2 class="hero-section">Understanding UV Radiation in Australia</h2>
      </div>
  
      <!-- Introduction Section -->
      <div class="info-section">
        <h2>General Information on UV Dangers</h2>
        <p>Learn about the risks associated with UV radiation in Australia</p>
        <div class="info-cards">
          <div class="info-card">
            <a
              href="https://www.arpansa.gov.au/understanding-radiation/what-is-radiation/non-ionising-radiation/ultraviolet-radiation#:~:text=Sun%20exposure%20causes%20the%20outer,UVR%20at%20an%20early%20age."
              target="_blank"
            >
              <h3>UV Basics</h3>
              <p>UV radiation comes from the sun and damages the skin leading to various health issues.</p>
            </a>
          </div>
          <div class="info-card">
            <a
              href="https://www.cancer.org.au/cancercareguides/basal-and-squamous-cell-carcinoma?gad_source=1&gclid=Cj0KCQjw7dm-BhCoARIsALFk4v81i3cKP3SOu_zeOpa81nqnV9Kel4VpTwnYLTdA9nJ6KmbVHblAUDMaApabEALw_wcB"
              target="_blank"
            >
              <h3>Skin Cancer Risk</h3>
              <p>Australia has one of the highest rates of skin cancer due to high UV levels.</p>
            </a>
          </div>
          <div class="info-card">
            <a href="https://www.stevekmd.com/blog/5-eye-conditions-caused-by-sun-damage" target="_blank">
              <h3>Eye Damage</h3>
              <p>UV exposure can also harm your eyes and lead to vision problems.</p>
            </a>
          </div>
        </div>
      </div>
  
      <!-- UV Index Guide -->
      <div class="protection-section">
        <h2>Understanding the UV Index</h2>
        <p>A guide to interpreting UV Index levels and their effects on health</p>
        <div class="uv-index-guide">
          <div class="uv-box">
            <h3>Low UV Index</h3>
            <p>0-2</p>
            <span>Low risk of harm</span>
          </div>
          <div class="uv-box">
            <h3>Moderate UV Index</h3>
            <p>3-5</p>
            <span>Take precautions!</span>
          </div>
          <div class="uv-box">
            <h3>High UV Index</h3>
            <p>6-7</p>
            <span>Risk of harm, ensure to protect yourself</span>
          </div>
          <div class="uv-box">
            <h3>Very High UV Index</h3>
            <p>8-10</p>
            <span>Be extra cautious</span>
          </div>
          <div class="uv-box">
            <h3>Extreme UV Index</h3>
            <p>11+</p>
            <span>Dangerous levels, avoid outdoor activity</span>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  /* General Styling */
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
  
  /* Info Section */
  .info-section {
    margin: 40px 0;
    text-align: center;
  }
  
  .info-cards {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
  }
  
  .info-card {
    background: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 250px;
  }
  
  .info-card a {
    text-decoration: none;
    color: black;
  }
  
  .info-card h3 {
    font-size: 18px;
    font-weight: bold;
  }
  
  .info-card p {
    font-size: 14px;
    color: #555;
  }
  
  /* UV Index Guide */
  .protection-section {
    margin: 40px 0;
    text-align: center;
  }
  
  .uv-index-guide {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
  }
  
  .uv-box {
    background: #f4f4f4;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 180px;
  }
  
  .uv-box h3 {
    font-size: 16px;
    font-weight: bold;
  }
  
  .uv-box p {
    font-size: 24px;
    font-weight: bold;
    color: #333;
  }
  
  .uv-box span {
    font-size: 14px;
    color: #777;
  }
  </style>
  