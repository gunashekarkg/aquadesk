<template>
    <div class="datavisualisation">
        <Navbar></Navbar>
        <div class="container mt-4">
        <v-simple-table :items-per-page="7" class="elevation-1">
        <!-- <table class="table table-bordered" id="table"> -->
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Date</th>
              <th scope="col">location</th>
              <th scope="col">Length</th>
              <th scope="col">type</th>
              <th scope="col">Deformed</th>
            </tr>
          </thead>
          <tbody>
            <tr  v-for="(value,index) in APIData" :key="index">
              <td>{{value.id}}</td>
              <td>{{value.Date}}</td>
              <td>{{value.location}}</td>
              <td>{{value.length}}</td>
              <td>{{value.type}}</td>
              <td>{{value.deformed}}</td>
            </tr>
          </tbody>
        </v-simple-table>
        </div>
    </div>

</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar.vue'
    export default{
    name : 'Datavisualisation',
     data () {
      return {
          APIData: [],
          id:0,
        }
    },
    components:{
            Navbar
        },

    created () {
        getAPI.get('datavisualisation/flatten?type_filter=Shrimps')
        .then((response) => {
            this.APIData = response.data
            // for (var i=0; i<this.APIData.length;i++){
            //   for(var j=0; j<this.APIData.countsessiontotank[i].length;j++){
            //     console.log("success")
            //   }

            // }
          })
        .catch(err => {
            console.log(err)
          })
    }
  }
</script>

<style scoped>

</style>
