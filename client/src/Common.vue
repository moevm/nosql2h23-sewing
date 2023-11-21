<template>
  <header style="font-family: Ubuntu;">
    <img src="@/assets/logo.png" id="logo"/>
    <div>
      <a href="/constructor" class="header_link">Конструктор</a>
      <a href="/projects" class="header_link">Мои проекты</a>
      <a href="/orders" class="header_link">Мои заказы</a>
      <a href="/chat" class="header_link">Чат с производителем</a>
      <a href="/faq" class="header_link">FAQ</a>
    </div>
    <div style="display: table; float: right; padding-right: 5vw">
      <div style="display: table-cell;">
        <a style="display: table-row">
          Phone number 1
        </a>
        <a style="display: table-row">
          Phone number 2
        </a>
        <a style="display: table-row">
          info@lensiz.ru
        </a>
      </div>
      <div style="display: table-cell; padding-left: 1vw; text-align: center; vertical-align: middle">
        <button class="btn btn-danger" style="height: 2.5vw; background-color: #cb292f">
          Заказать звонок
        </button>
      </div>
    </div>
  </header>
  <hr style="width: 92vw; margin-left: 4vw; margin-top: 0vw">

  <div id="wrapper" style="font-family: Ubuntu">
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
  </div>

  <div id="footer">
    <div style="display: table; float: right; padding-right: 5vw">
      <div id="contacts">
        <div style="display: table-cell;">
          <a style="display: table-row">
            г. Санкт-Петербург, п. Парголово, ул. Заречная, д. 41, стр.1
          </a>
          <a style="display: table-row; text-align: left">
            8 (812) 660 51 41
          </a>
          <a style="display: table-row; text-align: left">
            8 (911) 849 37 70
          </a>
          <a style="display: table-row; text-align: left">
            info@lensiz.ru
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CommonPage"
}
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 2vh;
  margin-bottom: 2vh;
}

.header_link {
  font-size: 1vw;
  padding-left: 2vw;
  color: black;
  text-decoration: none;
}

.header_link:hover {
  text-decoration: underline;
}

#logo {
  display: inline;
  vertical-align: middle;
  margin-right: 5vw;
  width: 15vw;
  padding-left: 5vw;
}

#footer {
  background-color: #062051;
  position: fixed;
  right: 0;
  bottom: 0;
  width: 100%;
  font-size: 19px;
  color: #fafaff;
}

#contacts {
  font-size: 12px;
  padding: 20px;
}

#wrapper {
  margin-left: 5vw;
  width: 90vw;
  height: 70vh;
}
</style>