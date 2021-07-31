<template>
    <div class="hero">
    <div id="videoDiv"> 
        <video id="video1" preload="" autoplay="" muted="" playsinline="" loop="">
            <source src="../assets/Forelle-Gesund.mp4" type="video/mp4">
        </video> 
          <div class="eseidonvideoMessage">
            eseidon’s AquaDetector
          </div>
          <div class="blueinnovationvideoMessage">
            Blue innovation at its’ best
          </div>
          <div class="realtimefeaturevideoMessage">
            AI based real time feature detection and sorting of aquatic organisms
          </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'homescreenvideotext',
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    }
  }
}
</script>
<style lang="scss" scoped>
#videoDiv {
  width: 100%; 
  height: auto;
  z-index: -1;
  position: relative;
  }
@media (min-aspect-ratio: 16/9){
    #videoDiv {
        width: 100%; 
        height: auto;
        }
}
@media (min-aspect-ratio: 16/9){
    #videoDiv {
        width: auto; 
        height: 100%;
        }
}
.eseidonvideoMessage {
    position: absolute;
    top: 0; 
    left: 0;
    display: flex;
    flex-direction: column; 
    justify-content: center;
    align-items: center; 
    width: 100%;
    height: 20%;
    color: #FFFFFF;
    z-index: 1;
}
.blueinnovationvideoMessage {
    position: absolute;
    top: 0; 
    left: 0;
    display: flex;
    flex-direction: column; 
    justify-content: center;
    align-items: center; 
    width: 100%;
    height: 80%;
    color: #FFFFFF;
    z-index: 1;
}
.realtimefeaturevideoMessage {
    position: absolute;
    top: 0; 
    left: 0;
    display: flex;
    flex-direction: column; 
    justify-content: center;
    align-items: center; 
    width: 100%;
    height: 150%;
    color: #FFFFFF;
    z-index: 1;
}
@media all and (min-width: 960px) {
    .eseidonvideoMessage{
      font-size: 36px;
    }
    .blueinnovationvideoMessage {
      font-size: 36px;
    }
    .realtimefeaturevideoMessage {
      font-size: 24px;
    }
}

@media all and (max-width: 959px) and (min-width: 600px) {
    .eseidonvideoMessage{
      font-size: 24px;
    }
    .blueinnovationvideoMessage {
      font-size: 24px;
    }
    .realtimefeaturevideoMessage {
      font-size: 16px;
    }
}
@media all and (max-width: 599px) and (min-width: 50px) {
    .eseidonvideoMessage{
      font-size: 18px;
    }
    .blueinnovationvideoMessage {
      font-size: 18px;
    }
    .realtimefeaturevideoMessage {
      font-size: 12px;
    }
}
</style>