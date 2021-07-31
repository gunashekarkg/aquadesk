<template>
    <div class="vision">
        <div class="worldmap">
          <img src="../assets/ourvision.svg" alt="world map">
        </div>
        <div class="ourvisionlayout">
        <div class="ourvision container">
          <h1 class="title">Our Vision</h1>
          <img src="../assets/footer_image.svg" alt="footer_image" class="titlefooter">
        </div>
        <div class="ourvisioncontent container">
            <p class="org-description">The population growth especially in emerging markets is going to increase regional food shortages as an increased demand in protein food is to be expected. In a world which becomes always further connected we want to create the possibility to balance supply and demand by early detection of regional supply bottlenecks and resolving them. At the same time, we can establish an early alert system for diseases within populations of aquatic organisms that can prevent their spreading. Furthermore, we can provide data for research to an unprecedented extent.</p>
        </div>
        <div class="page-footer">
            <img src="../assets/footer_fish.svg" alt="storyFooter" class="pagefooterimage">
        </div>
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
.vision{
    align-content: center;
    margin-bottom: 100px;
    .ourvision{
        text-align: center;
        .title{
            font-size: 36px;
            margin-bottom: 10px;
        }
        h1{
            color: #3F6993;
        }
    }
    .ourvisioncontent{
        color: #3F6993;
        .org-description{
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
.vision{
    .ourvisionlayout{
        padding-left: 20px;
        padding-right: 20px;
    }
    .ourvision{
        .title{
            font-size: 28px;
        }
        .titlefooter{
            width: 100px;
        }
    }

    .ourvisioncontent{
        .org-description{
            font-size: 18px;
        }
    }
}
}
@media all and (max-width: 599px) and (min-width: 50px) {
.vision{
    .ourvisionlayout{
        padding-left: 10px;
        padding-right: 10px;
    }
    .ourvision{
        .title{
            font-size: 20px;
            margin-bottom: 5px;
        }
        .titlefooter{
            width: 70px;
        }
    }

    .ourvisioncontent{
        .org-description{
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