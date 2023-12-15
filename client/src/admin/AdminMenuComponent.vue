<template>
  <div id="menu">
    <ul class="menu_container list-group list-group-flush">
      <li class="menu_button list-group-item" style="border-radius: 10px">
        <a href="/admin/new_applications" class="menu_text">Новые регистрации</a></li>
      <li class="menu_button list-group-item">
        <a href="/admin/clients" class="menu_text">Покупатели</a></li>
      <li class="menu_button list-group-item">
        <a href="/admin/providers" class="menu_text">Поставщики</a></li>
      <li class="menu_button list-group-item">
        <a href="admin/clients/chat" class="menu_text">Чат с покупателями</a></li>
      <li class="menu_button list-group-item">
        <a href="admin/providers/chat" class="menu_text">Чат с поставщиками</a></li>
      <li class="menu_button list-group-item">
        <a href="/admin/constructor_edit" class="menu_text">Управление конструктором</a></li>
      <li class="menu_button list-group-item">
        <a href="/admin/offer_edit" class="menu_text">Редактирвоание оферты</a></li>
      <li class="menu_button list-group-item">
        <a href="/admin/text_instruction" class="menu_text">Инструкция (текстовая)</a></li>
      <li class="menu_button list-group-item">
        <a href="/admin/video_instruction" class="menu_text">Видео-инструкция</a></li>
      <li class="menu_button list-group-item" style="border-radius: 10px">
        <a href="/admin/profile_management" class="menu_text">Управление профилем</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "AdminMenuComponent"
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
  width: 100%;
}

.menu_text {
  text-decoration: none;
  color: #f3dfdf;
}

.menu_container {
  padding-top: 50%;
  padding-left: 5%;
}
</style>