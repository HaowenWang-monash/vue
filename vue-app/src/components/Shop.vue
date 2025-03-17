<template>
    <div class="container">
      <!-- Hero Section -->
      <div>
        <h2 class="hero-section">Discover Sun-Safe Products</h2>
        <p>Browse through our curated collection of sun protective clothing and accessories.</p>
      </div>
  
      <!-- Featured Sun-Safe Products -->
      <div class="featured-section">
        <h2>Featured Sun-Safe Products</h2>
        <div class="product-list">
          <div class="product" v-for="(product, index) in featuredProducts" :key="index">
            <img :src="product.img" :alt="product.name" />
            <h3>{{ product.name }}</h3>
            <p>{{ product.description }}</p>
            <a :href="product.link" target="_blank">
              <button>Shop Now</button>
            </a>
          </div>
        </div>
      </div>
  
      <!-- Shop by Category -->
      <div class="category-section">
        <h2>Shop by Category</h2>
        <div class="category-list">
          <div class="category" v-for="(category, index) in categories" :key="index">
            <a :href="category.link" target="_blank">
              <img :src="category.img" :alt="category.name" />
              <h3>{{ category.name }}</h3>
            </a>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const featuredProducts = [
    {
      name: "Little Urchin Natural Sunscreen SPF 50+",
      description: "A natural zinc-based sunscreen that is reef-safe and water-resistant.",
      img: new URL("../public/sunscreen.jpg", import.meta.url).href,
      link: "https://www.amazon.com.au/LITTLE-URCHIN-Natural-Clear-Sunscreen/dp/B09YLL278Z"
    },
    {
      name: "DAWNTREES Foldable Travel Umbrella",
      description: "A compact travel umbrella with 99% UV protection and a UPF of 50+.",
      img: new URL("../public/umbrella.jpg", import.meta.url).href,
      link: "https://www.amazon.com.au/DAWNTREES-Windproof-Automatic-Lightweight-Protection/dp/B0B3QX5N28"
    },
    {
      name: "ASY Sun Hat with Removable Face Covering",
      description: "Protection for face and neck with a removable neck and face flap.",
      img: new URL("../public/hat.png", import.meta.url).href,
      link: "https://www.amazon.com.au/ASY-Outdoor-Protection-Waterproof-Removable/dp/B07MVYTNL2"
    }
  ];
  
  const categories = [
    {
      name: "Hats",
      img: new URL("../public/hat.png", import.meta.url).href,
      link: "https://www.amazon.com.au/s?k=sun+protection+hat"
    },
    {
      name: "Sunglasses",
      img: new URL("../public/sunglasses.png", import.meta.url).href,
      link: "https://www.amazon.com.au/s?k=sunglasses"
    },
    {
      name: "T-shirts & Tops",
      img: new URL("../public/shirt.png", import.meta.url).href,
      link: "https://www.amazon.com.au/s?k=sun+protection+t+shirt"
    },
    {
      name: "Bottoms",
      img: new URL("../public/bottoms.png", import.meta.url).href,
      link: "https://www.amazon.com.au/s?k=sun+protection+pants"
    },
    {
      name: "Accessories",
      img: new URL("../public/accessories.png", import.meta.url).href,
      link: "https://www.amazon.com.au/s?k=sun+protection+accessories"
    }
  ];
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
  
  /* Featured Section */
  .featured-section {
    margin: 40px 0;
    text-align: center;
  }
  
  .product-list {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
  }
  
  .product {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 220px;
  }
  
  .product img {
    width: 120px;
    height: auto;
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
  
  /* Category Section */
  .category-section {
    margin: 40px 0;
    text-align: center;
  }
  
  .category-list {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
  }
  
  .category {
    background: white;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 180px;
  }
  
  .category img {
    width: 80px;
    height: auto;
    margin-bottom: 10px;
  }
  </style>
  