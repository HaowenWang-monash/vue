<template>
  <nav class="navbar">
    <div class="logo">🌞 SunWise</div>
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/check-uv">Check UV</router-link></li>
      <li><router-link to="/info">UV Information</router-link></li>
      <li><router-link to="/tips">Tips & Tricks</router-link></li>
      <li><router-link to="/planner">Sun Safety Planner</router-link></li>
      <li><router-link to="/shop">Shop</router-link></li>
      <li><router-link to="/about">About</router-link></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8f9fa;
  padding: 10px 20px;
}

.navbar .logo {
  font-size: 24px;
  font-weight: bold;
}

.navbar ul {
  list-style: none;
  display: flex;
  gap: 15px;
}

.navbar ul li {
  display: inline;
}

.navbar ul li a {
  text-decoration: none;
  color: #333;
}

.navbar ul li a:hover {
  color: #007bff;
}
</style>

  