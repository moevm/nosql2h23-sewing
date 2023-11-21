<template>
  <div id="menu">
    <ul class="list-group list-group-flush">
      <li class="menu_button list-group-item" style="border-radius: 10px">
        <a href="/constructor" class="menu_text">Конструктор</a></li>
      <li class="menu_button list-group-item">
        <a href="/projects" class="menu_text">Мои проекты</a></li>
      <li class="menu_button list-group-item">
        <a href="/orders" class="menu_text">Мои заказы</a></li>
      <li class="menu_button list-group-item">
        <a href="/chat" class="menu_text">Чат с производителем</a></li>
      <li class="menu_button list-group-item">
        <a href="/offer" class="menu_text">Оферта</a></li>
      <li class="menu_button list-group-item">
        <a href="/instruction_text" class="menu_text">Инструкция (текстовая)</a></li>
      <li class="menu_button list-group-item">
        <a href="/instruction_video" class="menu_text">Видео-инструкция</a></li>
      <li class="menu_button list-group-item">
        <a href="/edit" class="menu_text">Управление профилем</a></li>
      <li class="menu_button list-group-item" style="border-radius: 10px">
        <a href="/faq" class="menu_text">FAQ</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "MenuComponent"
}
</script>

<style scoped>
#menu {
  display: table-cell;
  float: left;
  width: 20%;
  border-radius: 10px;
  padding-right: 5%;
}

.menu_text:hover {
  text-decoration: underline;
}

.menu_button {
  margin-bottom: 0.2vh;
  border-radius: 10px;
  background-color: #0353b2;
}

.menu_text {
  text-decoration: none;
  color: #f3dfdf;
}
</style>