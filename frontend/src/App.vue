<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from '../src/components/NavBar.vue'
</script>

<template>
  <main>
    <RouterView />
  </main>
</template>

<style scoped>
body {
  font-family: 'Roboto', sans-serif;
}

h1 {
  color: #111827;
}

p {
  color: #9199b4;
}
</style>
