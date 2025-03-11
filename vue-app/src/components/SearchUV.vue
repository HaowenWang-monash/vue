<template>
    <div class="search-section">
      <h2>Search for UV Index</h2>
      <input type="text" v-model="location" placeholder="Enter location">
      <button @click="getUVIndex">Search</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        location: "",
      };
    },
    methods: {
      getUVIndex() {
        if (this.location) {
          this.$emit("search", this.location);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .search-section {
    text-align: center;
    margin: 20px 0;
  }
  input {
    padding: 10px;
    width: 300px;
    margin-right: 10px;
  }
  button {
    padding: 10px 20px;
    background-color: black;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  