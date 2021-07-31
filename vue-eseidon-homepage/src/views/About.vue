<template>
  <div class="about">
    <ourStory />
    <ourTeam />
    <ourVision/>
  </div>
</template>
<script>
import ourTeam from "../components/OurTeam";
import ourVision from "../components/OurVision";
import ourStory from "../components/OurStory";
export default {
  components: {
    ourTeam,
    ourVision,
    ourStory
  }
}
</script>
<style lang="scss" scoped>

</style>