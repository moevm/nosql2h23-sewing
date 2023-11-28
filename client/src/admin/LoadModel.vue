<template>
  <section>
    <div>
      <form action="//msiter.ru/action_page.php">
        <div class="container">
          <div class="form-group">
            <label for="login"><b>Загрузка модели</b></label>
            <input class="form-control" placeholder="Выберите файл с моделью" type="file" ref="fileInput"
                   @change="handleFileChange"/>
          </div>
          <div class="form-group">
            <label for="login"><b>Путь к модели на сервере</b></label>
            <input class="form-control" placeholder="Введите путь к модели" type="text" :value="path_to_model"
                   @input="event => path_to_model = event.target.value"/>
          </div>

          <button type="submit" class="btn btn-success" @click="uploadFile">Загрузить модель</button>
        </div>
      </form>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      path_to_model: "",
      selectedFile: null,
    };
  },
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
      formData.append("path_to_model", this.path_to_model || "");

      console.log(this.path_to_model)
      console.log(this.selectedFile)

      for (var key of formData.entries()) {
        console.log(key[0] + ', ' + key[1]);
      }


      axios.post("http://127.0.0.1:3000/api/admin/load_model", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((response) => {
            console.log(response.data);
          })
          .catch((error) => {
            console.error("Error uploading file:", error);
          });
    },
  },
};
</script>

<style scoped>

</style>