<template>
    <div class="uv-info">
      <h2>Current UV Index Information</h2>
      <p><strong>Location:</strong> {{ uvData?.location || "City, Country" }}</p>
      <p><strong>UV Index:</strong> {{ uvData?.uv_index || "--" }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ["uvData"],
  };
  </script>
  
  <style scoped>
  .uv-info {
    text-align: center;
    margin-top: 20px;
  }
  </style>
  
  