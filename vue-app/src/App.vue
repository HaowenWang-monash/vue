<template>
  <div>
    <!-- Navigation Bar -->
    <NavBar />

    <!-- Main Content Area -->
    <router-view />
  </div>
</template>

<script>


import NavBar from "./components/NavBar.vue";
export default {
  components: {
    NavBar,
  },
};
</script>

<style scoped>

</style>


