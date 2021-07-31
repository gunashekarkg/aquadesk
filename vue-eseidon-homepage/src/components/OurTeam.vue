<template>
    <div class="team">
        <div class="ourteam container">
          <h1 class="title">Our Team</h1>
          <img src="../assets/footer_image.svg" alt="footer_image" class="titlefooter">
        </div>
        <v-container class="my-5">
            <v-layout row wrap class="ourteamlayout">
                <v-flex xs6 sm4 md4 lg4 v-for="person in ourTeam" :key="person.name" class="ourteamcomplete">
                    <v-card flat class="text-xs-center ma-3">
                        <v-responsive class="pt-4">
                            <v-avatar size="160">
                                <img :src="person.picture" class="ourteamimage">
                            </v-avatar>
                        </v-responsive>
                        <v-card-text class="namejobdescription">
                            <div class="name subheading">{{person.name}}</div>
                            <div class="jobdescription grey-text">{{person.role}}</div>
                        </v-card-text>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
        <div class="page-footer">
            <img src="../assets/footer_blue_fish.svg" alt="storyFooter" class="pagefooterimage">
        </div>         
    </div>
</template>
<script>
export default {
  data(){
    return{
        ourTeam: [
        {
            name: 'ANIL',
            role: 'CSO',
            picture: require('../assets/OurTeam/Anil.png')
        },
        {
            name: 'JAN',
            role: 'CEO & CTO, CO-Founder',
            picture: require('../assets/OurTeam/Jan.png')
        },
        {
            name: 'CHIARA',
            role: 'CFO, CO-Founder',
            picture: require('../assets/OurTeam/Chiara.png')
        },
        {
            name: 'GUNA',
            role: 'Front-End and Database Expert',
            picture: require('../assets/OurTeam/Guna.jpg')
        },
        {
            name: 'SVEN',
            role: 'Back-End & AI Expert',
            picture: require('../assets/OurTeam/Sven.png')
        },
        {
            name: 'THILO',
            role: 'Hardware Enthusiast',
            picture: require('../assets/OurTeam/Thilo.png')
        },
        ]
    }
  }
}
</script>

<style lang="scss" scoped>
.team{
    text-align: center;
    margin-bottom: 120px;
    .ourteam{
    padding: 5px;
    text-align: center;
    border: none;
    margin-bottom: 50px;
    .title{
        font-size: 36px;
        margin-bottom: 10px;
    }
      h1{
      color: #3F6993;
    }
  }
  .subheading{
      color: #3F6993;
      font-size: 24px;
  }
  .grey-text{
      color: #3F6993;
      font-size: 24px;
  }
    .page-footer{
        text-align: center;
        align-content: center;
        margin-top: 50px;
    }
    .ourteamcomplete{
        padding-bottom: 20px;
    }
}
@media all and (max-width: 959px) and (min-width: 600px) {
.team{
.ourteam{
    .title{
        font-size: 28px;
    }
    .titlefooter{
    width: 100px;
  }
  }
  .ourteamlayout{
      padding-left: 20px;
      padding-right: 20px;
  }
  .subheading{
      font-size: 18px;
  }
  .grey-text{
      font-size: 18px;
  }
  .ourteamimage{
    max-height:125px;
    max-width: 125px;
  }
}
}
@media all and (max-width: 599px) and (min-width: 50px) {
.team{
    .ourteam{
        .title{
            font-size: 20px;
            margin-bottom: 5px;
        }
        .titlefooter{
            width: 70px;
        }
    }
    .ourteamlayout{
        padding-left: 10px;
        padding-right: 10px;
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
    .ourteamimage{
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