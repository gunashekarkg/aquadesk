<template>
    <div class="datavisualisation1">
        <Navbar></Navbar>
        <div class="container mt-4">
        <table class="table table-bordered mt-5" id="MyTable">
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
          </tbody>
        </table>
        </div>
    </div>

</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar.vue'
    import $ from 'jquery';
    export default{
    name : 'DataVisualisation1',
        mounted () {
        this.getResults()
    },
    methods:{
        getResults(){
            getAPI.get('datavisualisation/flatten?type_filter=Shrimps')
            .then((response) => {
            $('#MyTable').DataTable( {
            dom: 'Bfrtip',
            buttons: ['colvis'],
            data: response.data,
                columns: [
                    { data: 'id' },
                    { data: 'Date' },
                    { data: 'location' },
                    { data: 'length' },
                    { data: 'type' },
                    { data: 'deformed' }
                ]
            });
            })
            .catch(err => {
            console.log(err)
            })            
        }
    },
    components:{
            Navbar
        },


  }
</script>

<style scoped>

</style>
