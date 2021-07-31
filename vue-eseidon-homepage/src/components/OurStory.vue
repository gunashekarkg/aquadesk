<template>
    <div class="story">
      <div class="scienary">
        <img src="../assets/about_1.jpg" alt="Scienary">
      </div>
      <div class="ourstory container">
        <h1 class="title">Our Story</h1>
        <img src="../assets/footer_image.svg" alt="footer_image" class="titlefooter">
      </div>
      <div class="ourstorydescription container">
        <p class="org-description">During his studies abroad in Brazil, Jan was living by the sea. Through this proximity, he started to be cris abt the overfishing of oceans and aquaculture. </p>
        <p class="org-description">Back in Germany, a new hobby emerged out of the initial interest. Jan began to pursue his fishing license with the goal to operate fish ponds in mind. He now owns ponds with noble crayfish and trouts. He was concerned about sorting crayfish. With some acqaintences he had the idea, to sort prawns according to their sex. With some prawn species, this leads to significant growth rate increases and therefore to enhanced revenue and cost reduction for aquaculture facilities.</p>
        <p class="org-description">Like that, the idea for the AquaDetector was born. eseidon was founded in 2019 together with Chiara Schmitz, a fellow student for his studies abroad.  </p>
      </div>
      <div class="page-footer">
        <img src="../assets/footer_fish.svg" alt="storyFooter" class="pagefooterimage">
      </div>    
    </div>
</template>
<script>
export default {
  data(){
    return{
    }
  }
}
</script>

<style lang="scss" scoped>
.story{
    align-content: center;
    margin-bottom: 100px;
    .title{
      font-size: 36px;
      margin-bottom: 10px;
    }
    .ourstory{
        text-align: center;
        h1{
            color: #3F6993;
        }
    }
    .ourstorydescription{
        color: #3F6993;
        .org-description{
          margin-bottom: 20px;
          font-size: 24px;
        }
    }
    .page-footer{
        text-align: center;
        align-content: center;
        margin-top: 50px;
    }
}
@media all and (max-width: 1023px) and (min-width: 960px) {
.story{
  .title{
      font-size: 36px;
  }
  .ourstorydescription{
  .org-description{
    font-size: 24px;
  }
  }
}
}
@media all and (max-width: 959px) and (min-width: 600px) {
.story{
  .title{
      font-size: 28px;
  }
  .titlefooter{
    width: 100px;
  }
  .ourstorydescription{
  .org-description{
    margin-left: 30px;
    margin-right: 30px;
    font-size: 18px;
  }
  }
}
}
@media all and (max-width: 599px) and (min-width: 50px) {
.story{
  margin-bottom: 70px;
  .title{
      font-size: 20px;
      margin-bottom: 5px;
  }
  .titlefooter{
    width: 70px;
  }
  .ourstorydescription{
  .org-description{
    margin-left: 20px;
    margin-right: 20px;
    font-size: 16px;
  }
  }
  .page-footer{
  margin-top: 10px;
  .pagefooterimage{
    height: 25px;
    }
}
}

}
</style>