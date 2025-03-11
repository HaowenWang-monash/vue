<template>
    <nav class="navbar">
      <div class="logo">🌞 SunWise</div>
      <ul class="nav-links">
        <li><a href="#">Home</a></li>
        <li><a href="#">UV Index</a></li>
        <li><a href="#">Locations</a></li>
        <li><a href="#">About</a></li>
      </ul>
      <input type="text" placeholder="Search in site 🔍" class="search-bar" />
    </nav>
  </template>
  
  <style scoped>
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #fff;
    padding: 15px 30px;
    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .logo {
    font-size: 20px;
    font-weight: bold;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    gap: 20px;
  }
  
  .nav-links li a {
    text-decoration: none;
    color: black;
    font-weight: bold;
  }
  
  .search-bar {
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  </style>
  