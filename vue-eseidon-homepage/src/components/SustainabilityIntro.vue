<template>
    <div class="sustainabilityintro">
      <div class="sustainabilitydivimage">
        <img src="../assets/sustainability.jpg" alt="Sustainability" class="sustainabilityimage">
      </div>
      <div class="sustainability container">
        <h1 class="title">Sustainability</h1>
        <img src="../assets/footer_image.svg" alt="footer_image" class="titlefooter">
      </div>
      <div class="sustainabilitydescription container">
        <p class="org-description">eseidon’s AquaDetector enables the careful use of available resources. Using the AquaDetector reduces the consumption of land and food necessary in the aquaculture industry and thereby its CO2 emissions,  Furthermore, we are supporting a  sustainable, animal friendly and a more efficient breeding of aquatic organisms. We aim to work towards the following UN sustainable development goals:</p>
      </div>
      <sustainabilitylayout />
    </div>
</template>
<script>
import sustainabilitylayout from "../components/Sustainabilitylayout";
export default {
   components: {
    sustainabilitylayout
  },
  data(){
    return{
    }
  }
}
</script>

<style lang="scss" scoped>
.sustainabilityintro{
    align-content: center;
    .sustainabilityimage{
      max-height: 206px;
      width: 100%;
    }
    .title{
      font-size: 36px;
      margin-bottom: 10px;
    }
    .sustainability{
        text-align: center;
        h1{
            color: #3F6993;
        }
    }
    .sustainabilitydescription{
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

@media all and (max-width: 959px) and (min-width: 600px) {
.sustainabilityintro{
  .title{
      font-size: 28px;
  }
  .titlefooter{
    width: 100px;
  }
  .sustainabilitydescription{
  .org-description{
    margin-left: 30px;
    margin-right: 30px;
    font-size: 18px;
  }
  }
}
}
@media all and (max-width: 599px) and (min-width: 50px) {
.sustainabilityintro{
  margin-bottom: 70px;
  .title{
      font-size: 20px;
      margin-bottom: 5px;
  }
  .titlefooter{
    width: 70px;
  }
  .sustainabilitydescription{
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