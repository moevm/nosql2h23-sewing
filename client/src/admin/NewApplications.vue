<template>
  <h1 class="display-1" style="text-align: center; font-size: 46px; font-family: Ubuntu; padding-top: 10px; color: #24509c">
    Новые регистрации</h1>
  <div class="inner">
    <AdminMenuComponent/>
  </div>
</template>

<script>
import {defineComponent} from "vue";
import AdminMenuComponent from "@/admin/AdminMenuComponent";

export default defineComponent({
  name: 'App',
  components: {AdminMenuComponent},
})
</script>

<style scoped>
.inner {
  vertical-align: middle;
}
</style>