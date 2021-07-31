<template>
    <div class="techintro">
        <div class="techintrodata">
            <v-layout row wrap justify-center align-center>
                <v-flex sm6 md6 lg6 xl6 class="primary">
                    <div class="techintrotitle container">
                        <h1 class="title">Eseidon develops the  AquaDetector, the first smart sorting device for your facility!</h1>
                        <img src="../assets/footer_image.svg" alt="footer_image">
                    </div>
                    <div class="subheading">
                        The following characteristics can be detected:
                    </div>
                    <v-container class="characteristics">
                        <v-list-item
                        v-for="dev in development" :key=dev.name
                        class="characteristicslist">
                        <v-avatar class="characteristicsavatar">
                                    <img :src="dev.picture" class="characteristics-logo">
                        </v-avatar>
                        <v-list-item-content>
                            <v-list-item-title v-text="dev.name" class="characteristicscontent wrap-text"></v-list-item-title>
                        </v-list-item-content>
                        </v-list-item>
                    </v-container>
                </v-flex>         
                <v-flex sm6 md6 lg6 xl6 class="secondary">
                    <div class="subheading">
                        <h1>
                            Tailored for your Needs
                        </h1>
                        <img src="../assets/footer_image.svg" alt="footer_image">
                    </div>
                    <div class="information">
                            <p class="hatchery">
                                From hatchery to grow out-facility - the AquaDetector is suitable for every life stadium from little larvae to adult fish - a perfectly fitting, animal friendly sorting device and variable software module allow uncomplicated alignment to your needs. 
                            </p>
                            <p class="Possible">
                                Possible application fields are therefore the improvement of the stock management, early detection of diseases, a permanent monitoring of size differences and many more.
                            </p>
                    </div>
                    <div class="second subheading">
                        <h1>
                            Do you need more?
                        </h1>
                        <img src="../assets/footer_image.svg" alt="footer_image">
                    </div>
                    <div class="information">
                        <p class="Collected">
                            Collected data can be reviewed and evaluated any time. A data export is possible as well.
                            Do you need to evaluate further characteristics?
                            Please feel free to contact us anytime.
                        </p>
                     </div>
                </v-flex>
            </v-layout>
            
        </div>
        <img src="../assets/footer_blue_fish.svg" alt="storyFooter" class="pagefooterimage">
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
.techintro{
    text-align: center;
    .pagefooterimage{
            left: 50%;
            margin-left: -55px;
            margin-top: -60px;
            position: absolute;
        }
    .techintrodata{
        margin-bottom: 0px;
        margin-top: 0px;
        
    }
    .techintrotitle{
        margin-top: 20px;
    }
    .secondary{
        background-color: white;
        .subheading{
            margin-top: 50px;
        }
        .second{
            margin-top: 20px;
        }
        .information{
            color: #3F6993;
            margin-left: 70px;
            margin-right: 75px;
            margin-top: 10px;
            //font-size: 18px;
            
            .hatchery{
                text-align: left;
                margin-bottom: 20px;
            }
            .Possible{
                text-align: left;
                margin-bottom: 20px;
            }
            .Collected{
                text-align: left;
            }
        }
    }
    .primary{
        background-color: #F2F3F4;
        padding-bottom: 70px;
        .title{
            padding: 0 50px 0 50px;
        }
        .characteristics{
            align-items: center;
            margin: 0px 140px 0px 140px;
            .characteristicslist{
                margin-bottom: 8px;
            }
            
            .characteristicscontent{
                margin-left: 15px;
                color: #3F6993;
                text-align: left;
                
            }
            .characteristicsavatar{
                .characteristics-logo{
                    max-height:35px;
                    max-width: 35px;
                }
            }
        }
        .subheading{
            color: #3F6993;
            margin-bottom: 20px;
        }
    }
    h1{
      color: #3F6993;
      font-size: 36px;
    }
    p{
        font-size: 18px;
    }

    
}
.wrap-text {
  white-space: normal;
}

@media all and (max-width: 1023px) and (min-width: 960px) {
    .techintro{
        .pagefooterimage{
            margin-top: -30px;      
        }
        .techintrotitle{
            margin: 10px
        }
        h1{
            font-size: 24px;
            margin-bottom: 5px;
        }
        .subheading{
            font-size: 18px;
            margin-bottom: 10px;
        }
        .primary{
            padding-bottom: 100px;
            .characteristics{
                align-items: center;
                margin: 0px 80px 0px 80px;
                .characteristicscontent{
                    font-size: 16px;
                }
                .characteristicsavatar{
                    .characteristics-logo{
                        max-height:40px;
                        max-width: 40px;
                    }
                }
            }
            .techintrotitle{
                  margin-top: 20px;
            }
        }
        .secondary{
            .information{
                margin-left: 40px;
                margin-right: 45px;
                .subheading{
                    margin-top: 10px;
                }
                .hatchery{
                    text-align: left;
                    margin-bottom: 16px;
                }
                .Possible{
                    text-align: left;
                    margin-bottom: 16px;
                }
                .Collected{
                    text-align: left;
                }
            }
        }
    }
.wrap-text {
  white-space: normal;
}
}

@media all and (max-width: 959px) and (min-width: 600px) {
    .techintro{
        .pagefooterimage{
            margin-top: -20px;      
        }
        .techintrotitle{
            margin: 10px
        }
        h1{
            font-size: 20px;
            margin-bottom: 5px;
        }
        .subheading{
            font-size: 16px;
            margin-bottom: 10px;
        }
        .primary{
            padding-bottom: 150px;
            .characteristics{
                align-items: center;
                margin: 0px 60px 0px 60px;
                .characteristicscontent{
                    font-size: 18px;
                }
                .characteristicsavatar{
                    .characteristics-logo{
                        max-height:40px;
                        max-width: 40px;
                    }
                }
            }
        }
        .secondary{
            .information{
                margin-left: 40px;
                margin-right: 45px;
                font-size: 14px;
                .hatchery{
                    text-align: left;
                    margin-bottom: 14px;
                }
                .Possible{
                    text-align: left;
                    margin-bottom: 0;
                }
                .Collected{
                    text-align: left;
                }
            }
        }
    }
.wrap-text {
  white-space: normal;
}
}
@media all and (max-width: 599px) and (min-width: 50px) {
    .techintro{
        margin-bottom: 70px;
        .pagefooterimage{
            margin-top: 20px;
            height: 25px; 
        }
        .techintrotitle{
            margin: 15px
        }
        h1{
            font-size: 18px;
            margin-bottom: 5px;
        }

        .primary{
            .characteristics{
                align-items: center;
                margin: 0px 60px 0px 100px;
                .characteristicscontent{
                    font-size: 14px;
                }
                .characteristicsavatar{
                    .characteristics-logo{
                        max-height:25px;
                        max-width: 25px;
                    }
                }
            }
        }
        .secondary{
            .information{
                margin-left: 40px;
                margin-right: 45px;
                
                .hatchery{
                    text-align: left;
                    margin-bottom: 14px;
                }
                .Possible{
                    text-align: left;
                    margin-bottom: 0;
                }
                .Collected{
                    text-align: left;
                }
                p{
                    font-size: 16px;
                }
            }
        }
    }
    .wrap-text {
    white-space: normal;
    }

    
}
</style>