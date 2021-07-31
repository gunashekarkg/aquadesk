<template>
  <div class="databasaetable">
    <Navbar></Navbar>
    <div class="ui container">
      <my-vuetable></my-vuetable>
    </div>
  </div>
</template>

<script>
import MyVuetable from '../components/DataVisualisationTable.vue'
import Navbar from '../components/Navbar.vue'

export default {
  name: 'DatabaseTable',
  components: {
    MyVuetable,
    Navbar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>