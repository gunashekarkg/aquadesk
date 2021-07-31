<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand img-responsive" href="#">
      <img
        src="../assets/eseidon.png"
        height="90px"
        width="156px"
        class="d-inline-block align-top"
        alt=""
        loading="lazy"
      />
    </a>
    <!-- Toggler/collapsibe Button -->
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarToggler"
      aria-controls="navbarToggler"
      aria-expanded="true"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarToggler">
      <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
        <li class="nav-item active">
          <router-link
            :to="{ name: 'Datavisualisation' }"
            class="nav-link"
            exact
            >Data Visualisation</router-link
          >
        </li>
        <li class="nav-item active">
          <router-link :to="{ name: 'DatabaseTable' }" class="nav-link" exact
            >DatabaseTable</router-link
          >
        </li>
        <li class="nav-item active">
          <router-link :to="{ name: 'DataVisualisation1' }" class="nav-link" exact
            >Datavisualisation1</router-link
          >
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
a {
  color: #000;
}
.navbar img {
  min-height: 60px;
  min-width: 126;
}
</style>