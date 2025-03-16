<template>
  <div>

    <NavBar />

 
    <div class="hero-section">
      <h1>View UV Index Levels for Different Locations</h1>
    </div>

 
    <SearchUV @search="fetchUVIndex" />


    <UVIndex :uvData="uvData" />


    <SunProtection />


    <RecommendedProducts />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import SearchUV from "./components/SearchUV.vue";
import UVIndex from "./components/UVIndex.vue";
import SunProtection from "./components/SunProtection.vue";
import RecommendedProducts from "./components/RecommendedProducts.vue";

export default {
  components: {
    NavBar,
    SearchUV,
    UVIndex,
    SunProtection,
    RecommendedProducts,
  },
  data() {
    return {
      uvData: null,
    };
  },
  methods: {
    async fetchUVIndex(location) {
      try {
        const response = await fetch(`http://localhost:5000/api/uv?location=${location}`);
        this.uvData = await response.json();
      } catch (error) {
        console.error("Error fetching UV index:", error);
      }
    }
  }
};
</script>

<style scoped>
.hero-section {
  background-color: #4a4a4a;
  color: white;
  text-align: center;
  padding: 40px 0;
  font-size: 24px;
  font-weight: bold;
}
</style>
