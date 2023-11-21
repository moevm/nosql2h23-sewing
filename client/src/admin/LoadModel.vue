<template>
  <section>
    <div>
      <form action="//msiter.ru/action_page.php">
        <div class="container">
          <div>
            <div class="form-group">
              <label for="login"><b>Загрузка модели</b></label>
              <input class="form-control" type="file" placeholder="Выберите файл с моделью" name="model"
                     id="model" required>
            </div>

            <div class="form-group">
              <label for="psw"><b>Путь к модели на сервере</b></label>
              <input class="form-control" placeholder="Введите путь"
                     name="path" id="path" required>
            </div>
          </div>
          <button type="submit" class="btn btn-success">Регистрация</button>
        </div>
      </form>
    </div>
  </section>
</template>

<script>
export default {
  name: "LoadModel"
}
</script>

<style scoped>

</style>