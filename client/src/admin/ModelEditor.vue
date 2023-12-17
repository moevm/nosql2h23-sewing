<template>
  <HeaderComponent/>
  <h1 class="display-1"
      style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Редактор модели</h1>
  <div id="wrapper" style="font-family: Ubuntu">
    <AdminMenuComponent/>
  </div>
  <FooterComponent/>
</template>

<script>
import {defineComponent} from "vue";
import AdminMenuComponent from "@/admin/AdminMenuComponent";
import HeaderComponent from "@/HeaderComponent";
import FooterComponent from "@/FooterComponent";

export default defineComponent({
  name: 'App',
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},
})
</script>

<style scoped>
</style>