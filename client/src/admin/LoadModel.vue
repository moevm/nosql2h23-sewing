<template>
  <HeaderComponent/>
  <div id="wrapper">
    <AdminMenuComponent/>
    <div class="form-check-inline">
      <form>
        <div class="form-group">
          <label for="login"><b>Загрузка модели</b></label>
          <input class="form-control" placeholder="Выберите файл с моделью" type="file" ref="fileInput"
                 @change="handleFileChange"/>
        </div>

        <div class="form-group">
          <label><b>Имя модели у пользователя</b></label>
          <input class="form-control" placeholder="Введите имя модели у пользователя" type="text" v-model="name"/>
        </div>

        <div class="form-group">
          <label><b>Тип модели</b></label>
          <input class="form-control" placeholder="Введите тип модели" type="text" v-model="model_type"/>
        </div>

        <div class="form-group">
          <label><b>Описание</b></label>
          <input class="form-control" placeholder="Введите описание модели" type="text" v-model="description"/>
        </div>

        <div class="form-group">
          <label><b>Путь к модели на сервере</b></label>
          <input class="form-control" placeholder="Введите путь к модели" type="text" v-model="path_to_model"/>
        </div>

        <button class="btn btn-success" @click.prevent="uploadFile" style="margin-top: 10px; background-color: #0353b2">
          Загрузить модель
        </button>
      </form>
      <p>Статус : {{ message }}</p>
    </div>
  </div>
  <FooterComponent/>
</template>

<script>
import axios from "axios";
import HeaderComponent from "@/customer/HeaderComponent";
import FooterComponent from "@/FooterComponent";
import AdminMenuComponent from "@/admin/AdminMenuComponent";

export default {
  data() {
    return {
      name: "",
      model_type: "",
      description: "",
      path_to_model: "",
      selectedFile: null,

      message: ""
    };
  },
  components: {HeaderComponent, FooterComponent, AdminMenuComponent},
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    uploadFile() {
      if (!this.selectedFile) {
        console.error("No file selected");
        return;
      }

      const formData = new FormData();
      formData.append("file", this.selectedFile);
      formData.append("name", this.name || "");
      formData.append("type_of_model", this.model_type || "");
      formData.append("description", this.description || "");
      formData.append("path_to_model", this.path_to_model || "");


      axios.post("/api/admin/load_model", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
          .then((response) => {
            if (response.data === 201) {
              this.message = "успешно загружена"
            } else {
              this.message = "произошла ошибка"
            }
          })
          .catch((error) => {
            console.error("Error uploading file:", error);
          });
    },
  },
};
</script>

<style scoped>
#wrapper {
  font-family: Ubuntu;
  display: flex;
  margin-left: 4vw;
  width: 92vw;
  min-height: 70vh;
}
</style>