<template>
  <div id="app1">
    <AquaDeskNav/>
    <router-view/>
  </div>
</template>
<script>
import AquaDeskNav from '../components/partials/AquaDeskNav.vue';
export default {
  name: 'app',
  components: {
    AquaDeskNav
  } 
}
</script>
<style lang="scss">
#app1 {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;

}

</style>