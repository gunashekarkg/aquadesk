<template>
    <div class="benifits">
        <div class="majorbenifits container">
          <h1 class="title">Major Benefits</h1>
          <img src="../assets/footer_image.svg" alt="footer_image">
        </div>
        <div class="benifits container">
        <v-container class="benifitlist" align-center>
            <v-layout row wrap class="layoutrowwrap">
                <v-flex xs12 md4 lg4 xl4 v-for="benifitslist in firstbenifitlist" :key=benifitslist.name>
                            <div class="firstbenifitslistcontent">
                            <v-avatar size="50">
                                <img :src="benifitslist.picture" class="image-logo">
                            </v-avatar>
                            {{benifitslist.name}}</div>
                </v-flex>
                <v-flex xs12 md6 lg6 xl6 v-for="benifitslist in secondbenifitlist" :key=benifitslist.name>
                            <div class="secondbenifitslistcontent">
                            <v-avatar size="50">
                                <img :src="benifitslist.picture" class="image-logo">
                            </v-avatar>
                            {{benifitslist.name}}</div>
                </v-flex>
            </v-layout>
        </v-container>
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
        firstbenifitlist: [
        {
            name: 'Expandable functional scope',
            picture: require('../assets/Expandable.svg')
        },
        {
            name: 'Modularity',
            picture: require('../assets/Modularity.svg')
        },
         {
            name: 'Data Acquisition',
            picture: require('../assets/Data.svg')
        },
        ],
        secondbenifitlist:[
        {
            name: 'Enhanced animal welfare',
            picture: require('../assets/Enhanced.svg')
        },
        {
            name: 'Cost reduction',
            picture: require('../assets/Cost.svg')
        },
        ]
    }
  }
}
</script>

<style lang="scss" scoped>
.benifits{
    margin-block: 20px;
    text-align: center;
    .title{
        color: #3F6993;
        font-size: 36px;
    }
    .firstbenifitslistcontent{
        margin-bottom: 10px;
        color: #3F6993;
        font-size: 24px;
    }
    .secondbenifitslistcontent{
        margin-bottom: 10px;
        color: #3F6993;
        font-size: 24px;
    }
}
.page-footer{
    text-align: center;
    align-content: center;
    margin-top: 50px;
}
@media all and (max-width: 1023px) and (min-width: 960px) {
    .majorbenifits{
        
        .title{
            margin-bottom: 10px;
            font-size: 24px;
        }
    }
    .container{
        .layoutrowwrap{
        .firstbenifitslistcontent{
            font-size: 18px;
            .image-logo{
                height: 40px;
            }
        }
        .secondbenifitslistcontent{
            font-size: 18px;
            .image-logo{
                height: 40px;
            }
        }
    }
    }
}
@media all and (max-width: 959px) and (min-width: 600px) {
.benifits{
    margin-left: 60px;
    margin-top: 0;
    .majorbenifits{
        padding-bottom: 0; 
        .title{
            margin-bottom: 10px;
            font-size: 20px;
        }
    }  
    .container{
        .layoutrowwrap{
            padding: 0 80px 0 100px;
        .firstbenifitslistcontent{
            float: left;
            font-size: 16px;            
            margin-bottom: 0px;
            .image-logo{
                height: 30px;
                align-items: left;
                justify-content: space-between;
            }
        }
        .secondbenifitslistcontent{
            text-align: left;
            margin-bottom: 0px;
            font-size: 16px;
            .image-logo{
                height: 30px;
            }
        }
    }
    }
}
}
@media all and (max-width: 599px) and (min-width: 50px) {
.benifits{
    margin-left: 10px;
    margin-top: 0;
.majorbenifits{
    padding-bottom: 0;        
    .title{
        margin-bottom: 0;
        padding: 0;
        font-size: 18px;
    }
    }
    .benifitlist{
        font-size: 14px;
        justify-content: justify-start;
    }
    .benifits.container{
        padding-left: 100px;
        padding-right: 100px;
        .firstbenifitslistcontent{
            align-items: left;
            text-align: left;
            margin-bottom: 0px;
            font-size: 16px;
            .image-logo{
                height: 30px;
            }
        }
        .secondbenifitslistcontent{
            text-align: left;
            margin-bottom: 0px;
            font-size: 16px;
            .image-logo{
                height: 30px;
            }
        }
    }
    .page-footer{
        .pagefooterimage{
            width: 100%;
            height: 25px;
        }
    }
}
}


</style>