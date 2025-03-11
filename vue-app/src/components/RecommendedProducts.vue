<template>
    <div class="products">
      <h2>Recommended Sun Protection Products</h2>
      <div class="product-list">
        <div class="product">
          <span>🌞</span>
          <p>Sunscreen SPF 50</p>
          <button>Buy Now</button>
        </div>
        <div class="product">
          <span>👒</span>
          <p>Hat - Wide-brimmed</p>
          <button>Buy Now</button>
        </div>
        <div class="product">
          <span>🕶️</span>
          <p>Sunglasses UV Protection</p>
          <button>Buy Now</button>
        </div>
      </div>
    </div>
  </template>
  
  <style scoped>
  .products {
    text-align: center;
    margin-top: 40px;
  }
  .product-list {
    display: flex;
    justify-content: center;
    gap: 20px;
  }
  .product {
    padding: 20px;
    background-color: #f1f1f1;
    border-radius: 8px;
    width: 150px;
    text-align: center;
  }
  button {
    margin-top: 10px;
    padding: 8px 12px;
    background-color: black;
    color: white;
    border: none;
  }
  </style>
  