<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
    </div>
    
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<style>

</style>
