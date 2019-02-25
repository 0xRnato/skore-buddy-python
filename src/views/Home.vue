<template>
  <div class="home">
    <Header />
    <ChatComponent/>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Header from '@/components/Header.vue'
import ChatComponent from '@/components/ChatComponent.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'home',
  components: {
    Header, ChatComponent, Footer
  }
}
</script>

<style lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
