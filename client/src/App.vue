<template>
  <vue3dLoader
      :height="900"
      :showFps="false"
      :filePath="'http://localhost:8081/static/mers.obj'"
      :backgroundColor="0x000000"
  ></vue3dLoader>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
</style>
