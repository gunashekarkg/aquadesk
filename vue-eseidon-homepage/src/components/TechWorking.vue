<template>
    <div class="techworking">
        <div class="techworkingdata">
            <v-layout row wrap justify-center align-center>
                <v-flex sm6 md6 lg6 xl6 class="primary">
                    <div class="working container">
                        <video playsinline autoplay muted loop class="workingvideo">
                            <source src="../assets/Schematische-Darstellung-komplet.mp4" type='video/mp4'>
                        </video>
                    </div>
                </v-flex>         
                <v-flex sm6 md6 lg6 xl6 class="secondary">
                    <div class="subheading">
                        <h1>
                            How it Works
                        </h1>
                        <img src="../assets/footer_image.svg" alt="footer_image">
                    </div>
                    <div class="subsubheading">
                        <h3>
                            1. Isolator
                        </h3>
                        <div class="information">
                            <p>
                                The organism is inserted to the device and the isolator ensures a reduced frequency of organisms flowing simultaneously.
                            </p>
                        </div>
                    </div>
                    <div class="subsubheading">
                        <h3>
                            2. Image Recognition Device
                        </h3>
                        <div class="information">
                            <p>
                                The organism flows through the AquaDetector, where the AI-based real time detection is initiated.
                                    The data is transferred to the cloud and analyzed. The detected characteristics like amount, size, species, sex and health status are shown in a clear dashboard. 
                            </p>
                        </div>
                    </div>
                    <div class="subsubheading">
                        <h3>
                            3. Sorter
                        </h3>
                        <div class="information">
                            <p>
                                The organisms can be sorted immediately regarding the specified characteristic within seconds.
                            </p>
                        </div>
                    </div>
                </v-flex>
            </v-layout>
            <img src="../assets/footer_fish.svg" alt="storyFooter" class="pagefooterimage">
        </div>
    </div>
</template>
<script>
export default {
  data(){
    return{
        development: [
        {
            name: 'Body size',
            picture: require('../assets/bodysize.svg')
        },
        {
            name: 'Amount',
            picture: require('../assets/amount.svg')
        },
        {
            name: 'Deformations (developing)',
            picture: require('../assets/deformation.svg')
        },
        {
            name: 'Species (developing)',
            picture: require('../assets/species.svg')
        },
        {
            name: 'Sex (developing)',
            picture: require('../assets/sex.svg')
        },
        {
            name: 'Externally visible diseases/parasites (developing)',
            picture: require('../assets/external.svg')
        },
        ]
    }
  }
}
</script>

<style lang="scss" scoped>
.techworking{
    text-align: center;
    margin-top: 10px;
    margin-block-end: 100px;
    .techworkingdata{
        margin-bottom: 50px;
        .pagefooterimage{
            left: 50%;
            margin-left: -55px;
            margin-top: -60px;
            position: absolute;
        }
    } 
    .secondary{
        background-color: #F2F3F4;
        padding-top: 80px;
        padding-bottom: 80px;
        .subheading{
            
            color: #3F6993;
            margin-bottom: 20px;
        }
        .subsubheading{
            font-size: 18px;
            text-align: left;
            color: #3F6993;
            margin-left: 70px;
            margin-right: 75px;
            h3{
                font-weight: bold;
                margin-bottom: 5px;
            }
            
            .information{
            margin-left: 10px;
            margin-right: 15px;
            margin-bottom: 15px;
        }
        }

    }
    .primary{
        background-color: white;
        align-items: center;
        text-align: center;
        margin: auto;
        display: block;
        justify-content: center;
    }
    h1{
      color: #3F6993;
      font-size: 36px;
    }
}
@media all and (max-width: 1023px) and (min-width: 960px) {
.techworking{
    .secondary{
        .subsubheading{
            margin-left: 40px;
            margin-right: 45px;
        }
        h1{
            font-size: 24px;
        }
        h3{
            font-size: 18px;
        }
        p{
            font-size: 18px;
        }
    }
    }
    
}

@media all and (max-width: 959px) and (min-width: 600px) {
.techworking{
    .secondary{
        .subsubheading{
            margin-left: 40px;
            margin-right: 45px;
        }
        h1{
            font-size: 24px;
        }
        h3{
            font-size: 18px;
        }
        p{
            font-size: 18px;
        }
    }
    }
}

@media all and (max-width: 599px) and (min-width: 50px) {
.techworking{
    .secondary{
        .subsubheading{
            margin-left: 40px;
            margin-right: 45px;
        }
        h1{
            font-size: 24px;
        }
        h3{
            font-size: 16px;
        }
        p{
            font-size: 16px;
        }
    }
    }
    .pagefooterimage{
        height: 25px;
    }
}
</style>