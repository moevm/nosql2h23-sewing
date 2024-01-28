<template>
  <div class="container">
    <div>
      <h1 style="margin-bottom: 50px">
        Ваша заявка принята, ожидайте!
        <br>
        Менеджер скоро вам позвонит!
      </h1>
    </div>
    <div>
      <iframe :width=width_of_video :height=height_of_video :src=link_to_video
              title="YouTube video player" frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              allowfullscreen>
      </iframe>
    </div>

  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "WaitPage",

  data() {
    return {
      link_to_video: '',
      width_of_video: 0,
      height_of_video: '',
    }
  },

  methods: {
    loadSettings() {
      axios.get("/api/admin/settings", {
        headers: {
          "Content-Type": "application/json",
        }
      }).then((response) => {
        this.link_to_video = response.data["link_to_video"];
        this.width_of_video = response.data["width_of_video"];
        this.height_of_video = response.data["height_of_video"];
      })
    }
  },

  mounted() {
    this.loadSettings()
  }
}
</script>

<style scoped>
body {
  font-family: Ubuntu;
  height: 100vh;
  width: 100vw;
}

.container {
  margin-top: 15vh;
  width: 100vw;
  height: 60vh;
  vertical-align: middle;
  text-align: center;
}
</style>