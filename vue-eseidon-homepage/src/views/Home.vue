<template>
<div class="home">
  <homescreenvideotext/>
  <majorBenifits/>
</div>
</template>
<script>
import majorBenifits from "../components/MajorBenifits"
import homescreenvideotext from "../components/HomescreenVideoText"
export default {
  name: 'home',
  components: {
    majorBenifits,
    homescreenvideotext
  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    }
  }
}
</script>
<style lang="scss" scoped>

</style>