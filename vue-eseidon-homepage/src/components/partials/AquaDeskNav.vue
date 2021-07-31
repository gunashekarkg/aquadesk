<template>
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a  href="/">
    <figure class="image-logo">
		<img src="../../assets/eseidon.png" height="90px" width="156px"/>
		</figure>
    </a>
    <a role="button" @click="toggleNav" :class="{'is-active':isActive}" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
    </div>
  <div id="navbar" class="menunav navbar-menu" :class="{'is-active':isActive}">
    <div class="navbar-start">
      <router-link to="/" class="navbar-item">DATA VISUALISATION</router-link>
      <router-link to="/technology" class="navbar-item">CALIBRATION</router-link>
      <router-link to="/sustainability" class="navbar-item">EVALUATED VIDEOS</router-link>
    </div>
  </div>
</nav>
</template>
<script>
export default {
  name: 'AquaDeskNav',
  data() {
	return{
		isActive: false
	}
  },
  methods: {
  // Log the user in
  login() {
    this.$auth.loginWithRedirect();
  },
  // Log the user out
  logout() {
    this.$auth.logout({
      returnTo: window.location.origin
    });
  },
  toggleNav() {
	this.isActive = !this.isActive
  }
  }
}
</script>
<style lang="scss" scoped>
nav {
  // position: fixed;
  // top: 0;
  // z-index: 999;
	height: 160px;
  width: 100%;
  padding: 0;
  background-color: #F2F3F4;
    a {
      font-weight: bold;
      color: #3F6993;

      &.router-link-exact-active {
        color: #d88d00;
        background-color: #F2F3F4;
      }
    }
  }
figure.image-logo{
  margin-top: 30px;
  margin-left: 74px;
  margin-right: 60px;
  }
a:not(.disabled):hover {
    background-color: #F2F3F4;
    color: #3F6993;
}
  
@media all and (max-width: 1023px) and (min-width: 600px) {
nav{
  margin-left: 0;
  height: 100px;
  .navbar-burger{
    top: 25px;
  }
	.menunav{
	position: absolute;
	top: 100px;
	right: 0px;
	align-items: right;
	flex-direction: column;
  padding:0;
	font-size: 16px;
	justify-content: space-between;
  background-color: #F2F3F4;
  transition: 300ms ease all;
  :hover{
    background-color: #F2F3F4;
    color: #3F6993;
  }
	}
a:not(.disabled):hover {
    background-color: #F2F3F4;
    color: #3F6993;
}


}
.container{
	max-width: 1023px;
  max-height: 100px;
	}
figure.image-logo{
  margin-top: 25px;
  margin-left: 15px;
  margin-right: 0px;
  height: 75px;
  width: 75px;
}
}

@media all and (max-width: 599px) and (min-width: 50px) {
nav{
  margin-left: 0;
  height: 70px;
  .navbar-burger{
    top: 15px;
  }
  .menunav{
		position: absolute;
    transition: 300ms ease all;
		top: 70px;
		right: 0px;
		align-items: right;
		flex-direction: column;
		padding:0;
		font-size: 10px;
		justify-content: space-between;
    background-color: #F2F3F4;
    :hover{
      background-color: #F2F3F4;
      color: #3F6993;
    }
    }
  }
  figure.image-logo{
    margin-top: 15px;
    margin-left: 10px;
    margin-right: 0px;
    height: 65px;
    width: 65px;
  }
}
</style>