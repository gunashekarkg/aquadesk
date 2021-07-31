<template>
  <vuetable ref="vuetable"
    api-url="http://127.0.0.1:8000/datavisualisation/flatten?type_filter=Shrimps"
    :fields="['Date', 'location', 'length']"
  ></vuetable>
</template>

<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'

export default {
  components: {
    Vuetable
  }
}
</script>