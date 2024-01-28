<template>
  <HeaderComponent/>
  <div id="wrapper">
    <AdminMenuComponent/>
    <div class="form-check-inline">
      <form>
        <div class="form-group">
          <label><b>Ссылка на приветственное видео</b></label>
          <input class="form-control" placeholder="Вставьте на видео" type="text" v-model="link_to_video"/>
        </div>

        <div class="form-group">
          <label><b>Ширина приветственного видео</b></label>
          <input class="form-control" placeholder="Ширина видео" type="text" v-model="width_of_video"/>
        </div>

        <div class="form-group">
          <label><b>Высота приветственного видео</b></label>
          <input class="form-control" placeholder="Высота видео" type="text" v-model="height_of_video"/>
        </div>

        <!--        <div class="form-group" style="display: inline-block">-->
        <!--          <label><b>Цвет фона конструктора</b></label>-->
        <!--          <br>-->
        <!--          <input class="form-control" placeholder="Цвет фона" type="text" v-model="background_color" style="width: 78%; margin-right: 5px; display: inline-block"/>-->
        <!--          <color-picker v-model:pureColor="background_color"-->
        <!--                        :disableAlpha="true" style="display: inline-block"/>-->
        <!--        </div>-->

        <hr>

        <button class="btn btn-success" @click="updateSettings" style="margin-top: 10px; background-color: #0353b2">
          Обновить настройки
        </button>
      </form>
    </div>
  </div>
  <FooterComponent/>
</template>

<script>
// import axios from "axios";
import HeaderComponent from "@/customer/HeaderComponent";
import FooterComponent from "@/FooterComponent";
import AdminMenuComponent from "@/admin/AdminMenuComponent";
import axios from "axios";

export default {
  name: "ConstructorSettings",
  data() {
    return {
      link_to_video: '',
      width_of_video: '',
      height_of_video: '',
    };
  },
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},
  methods: {
    updateSettings() {
      axios.post("/api/admin/update_settings", {
            "link_to_video": String(this.link_to_video),
            "width_of_video": this.width_of_video,
            "height_of_video": this.height_of_video,
          }, {
            headers: {
              'Accept':
                  'application/json',
              'Content-Type':
                  'application/json'
            }
          }
      )
    },
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
.form-group {
  margin-bottom: 20px;
}

#wrapper {
  font-family: Ubuntu;
  display: flex;
  margin-left: 4vw;
  width: 92vw;
  min-height: 70vh;
}
</style>