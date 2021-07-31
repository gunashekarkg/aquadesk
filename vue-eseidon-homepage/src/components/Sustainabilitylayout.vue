<template>
    <div class="sustainabilitygoal">
        <v-container class="my-5">
            <v-layout row wrap class="sustainabilitygoallayout">
                <v-flex col4 xs6 sm4 md4 lg2 v-for="sustainability in sustainabilities" :key="sustainability.name" class="sustainabilitygoalcomplete">
                    <v-card flat class="sustainabilitycard text-xs-center ma-3">
                        <v-responsive class="pt-4">
                            <img :src="sustainability.picture" class="sustainabilitygoalimage">
                        </v-responsive>
                        <v-card-text class="sustainabilitygoaldescription">
                            <div class="sustainabilityname subheading">{{sustainability.name}}</div>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
        <div class="sustainabilitydivimage">
        <img src="../assets/sustainability/sustainabilitygoal.png" alt="Sustainability" class="sustainabilitygoalimage">
        </div>
        <div class="page-footer">
            <img src="../assets/footer_blue_fish.svg" alt="storyFooter" class="pagefooterimage">
        </div>         
    </div>
</template>
<script>
export default {
  data(){
    return{
        sustainabilities: [
        {
            name: 'Supporting a secured protein food supply chain',
            picture: require('../assets/sustainability/Supporting.png')
        },
        {
            name: 'Increasing effieciency and resource consumption',
            picture: require('../assets/sustainability/Increasing.png')
        },
        {
            name: 'Reducing aquaculture’s CO2 impact',
            picture: require('../assets/sustainability/Reducing.png')
        },
        {
            name: 'Improving health and living conditions',
            picture: require('../assets/sustainability/Improving.png')
        },
        {
            name: 'Strengthening partners in regional markets by cooperation',
            picture: require('../assets/sustainability/Strengthening.png')
        },
        ]
    }
  }
}
</script>

<style lang="scss" scoped>
.sustainabilitygoal{
    text-align: center;
    .sustainabilitygoallayout{
        padding-left: 40px;
        padding-right: 40px;
        .sustainabilitycard{
            width: 500px;
            margin-right: 0;
        }
        .sustainabilitygoalcomplete{
            text-align: center;
            max-width: 210px;
            
            .sustainabilitygoalimage{
                width: 136px;
                height: 128px;
                margin: 0;

        }
        .sustainabilitygoaldescription{
            font-size: 14px;
        }
    }
    }
    .title{
        font-size: 36px;
        margin-bottom: 10px;
    }
      h1{
      color: #3F6993;
    }
  .sustainabilityname{
      color: #3F6993;
      font-size: 20px;
  }
    .page-footer{
        text-align: center;
        align-content: center;
        margin-top: 50px;
    }
    .sustainabilitygoalimage{
        width: 328px;
        height: 40px;
    }
    
}

@media all and (max-width: 959px) and (min-width: 600px) {
.sustainabilitygoal{
    .title{
        font-size: 28px;
    }
    .titlefooter{
    width: 100px;
  }
  .sustainabilitygoallayout{
      padding-left: 80px;
      padding-right: 80px;
  }
  .subheading{
      font-size: 18px;
  }
  .grey-text{
      font-size: 18px;
  }
  .sustainabilitygoalimage{
    max-height:125px;
    max-width: 125px;
  }
}
}
@media all and (max-width: 599px) and (min-width: 50px) {
.sustainabilitygoal{
        .title{
            font-size: 20px;
            margin-bottom: 5px;
        }
        .titlefooter{
            width: 70px;
        }
    .sustainabilitygoallayout{
        padding-left: 50px;
        padding-right: 0px;
        .namejobdescription{
            padding-top: 0;
        }
    }
    .subheading{
        font-size: 16px;
    }
    .grey-text{
        font-size: 16px;
    }
    .sustainabilitygoalimage{
        max-height:100px;
        max-width: 100px;
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