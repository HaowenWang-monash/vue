<template>
  <div class="container">
    <div>
    <h2 class="hero-section">View UV Index Levels for Different Locations</h2>
      </div>
    
    <div class="search-section">
      <h2>Search for UV Index</h2>
      <input type="text" v-model="location" placeholder="e.g. City, Country" />
      <button @click="getUVIndex">Search</button>
    </div>

   
    <div v-if="uvDataFetched" class="uv-info">
      <h2>Current UV Index Information</h2>
      <p>Check the UV levels and take necessary precautions</p>
      <div class="uv-data">
        <div>
          <strong>Location:</strong> {{ uvData.location || "N/A" }}
        </div>
        <div>
          <strong>UV Index:</strong> {{ uvData.uv_index || "N/A" }}
          <span>({{ uvData.level || "Unknown" }})</span>
        </div>
        <div>
          <strong>Date:</strong> {{ uvData.date || "N/A" }}
        </div>
        <div>
          <strong>Time:</strong> {{ uvData.time || "N/A" }}
        </div>
      </div>
    </div>


    <div v-else class="uv-info">
      <h2>Please enter a location to check the UV index.</h2>
    </div>

    
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
        <div class="tip-box">
          <img :src="shadeImg" alt="Seek Shade" />
          <h3>Seek Shade</h3>
          <p>Stay in shaded areas during peak hours</p>
        </div>
      </div>
    </div>

  
    <div class="products-section">
      <h2>Recommended Sun Protection Products</h2>
      <div class="products">
        <div class="product">
          <img :src="sunscreenImg" alt="Sunscreen" />
          <p>Sunscreen <br /><small>SPF 50</small></p>
          <a href="https://www.amazon.com.au/s?k=sunscreen" target="_blank">
            <button>Buy Now</button>
          </a>
        </div>
        <div class="product">
          <img :src="hatImg" alt="Hat" />
          <p>Hat <br /><small>Wide-brimmed</small></p>
          <a href="https://www.amazon.com.au/s?k=wide-brimmed+hat" target="_blank">
            <button>Buy Now</button>
          </a>
        </div>
        <div class="product">
          <img :src="shadeImg" alt="Sunglasses" />
          <p>Sunglasses <br /><small>UV Protection</small></p>
          <a href="https://www.amazon.com.au/s?k=sunglasses" target="_blank">
            <button>Buy Now</button>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sunscreenImg: new URL("../assets/sunscreen.png", import.meta.url).href,
      hatImg: new URL("../assets/hat.png", import.meta.url).href,
      shadeImg: new URL("../assets/sunglasses.png", import.meta.url).href,
      location: "",
      uvData: {}, 
      uvDataFetched: false, 
    };
  },

  methods: {
  async getUVIndex() {
    if (!this.location.trim()) {
      alert("Please enter a location");
      return;
    }

    try {
      console.log("Fetching UV data for:", this.location);
      const response = await fetch(
        `https://vue-fx7m.onrender.com/api/uv?location=${this.location}`
      );

      if (!response.ok) throw new Error("Failed to fetch UV index");

      const data = await response.json();
      console.log("Fetched data:", data);

      this.uvData = data;
      this.uvDataFetched = true;
    } catch (error) {
      console.error("Error fetching UV index:", error);
      alert("Error fetching data. Please try again.");
    }
  },
},

};
</script>


<style scoped>


.search-section input {
  padding: 10px;
  width: 250px;
  margin-right: 10px;
}

button {
  background-color: black;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #333;
}

.uv-info,
.protection-section,
.multi-locations,
.products-section {
  margin: 40px 0;
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

.locations {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.location-box {
  background: #f4f4f4;
  padding: 20px;
  border-radius: 5px;
}

.products {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.product {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 180px;
}

.product img {
  width: 80px;
  height: 80px;
  margin-bottom: 10px;
}

.product button {
  background-color: #f4a261;
  color: white;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.product button:hover {
  background-color: #e76f51;
}
</style>
