<template>
  <div class="login">
      <h1>Log in</h1>
      <LoginForm />
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue';
// import router from '../router';
export default {
    name: 'Login',
    components: {
      LoginForm,
    },
    // methods: {
    //   isLoggedIn () {
    //     this.$session.start();
    //     if (this.$session.has('jwt')) {  // jwt 가 없으면 => Login 안했으면
    //       router.push('/');
    //     }
    //   }
    // },
    // mounted () {  // logout 이후에 어떻게 되나 확인하기.
    //   this.isLoggedIn()
    // },
}
</script>

<style>

</style>