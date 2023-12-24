<template>
  <header style="font-family: Ubuntu,serif;">
    <img src="@/assets/logo.png" id="logo" alt=""/>
    <div class="header_core">
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

  <hr style="width: 92vw; margin-left: 4vw; margin-top: 0">
  <h1 class="display-1" style="text-align: center; font-size: 46px; font-family: Ubuntu,serif; color: #24509c">
    Конструктор спецодежды</h1>
  <br>
  <div id="wrapper" style="font-family: Ubuntu,serif">
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
    <div id="viewer" @mousemove="mouseMove" @mousedown.left="mouseDownLeft" @mouseup.left="mouseUpLeft"
         @mousewheel='mouseWheel' oncontextmenu="return false;"
         @mousedown.right="mouseDownRight" @mouseup.right="mouseUpRight">
    </div>
    <div id="select">
      <div style="padding-bottom: 10px; text-align: center">
        <select v-model="work_selected" @change="work_change($event)" class="select form-select"
                style="display: inline-block; width: 75%; margin-bottom: 10px">
          <option v-for="option in work_options" :value="option.value" :key="option.value">
            {{ option.text }}
          </option>
        </select>

        <select v-model="season_selected" @change="season_change($event)" class="select form-select"
                style="display: inline-block; width: 75%; margin-bottom: 10px">
          <option v-for="option in season_options" :value="option.value" :key="option.value">
            {{ option.text }}
          </option>
        </select>

        <select v-model="sex_selected" @change="sex_change($event)" class="select form-select"
                style="display: inline-block; width: 75%; margin-bottom: 10px">
          <option v-for="option in sex_options" :value="option.value" :key="option.value">
            {{ option.text }}
          </option>
        </select>
      </div>
      <div style="padding-bottom: 10px; text-align: center">
        Начальный цвет:
        <color-picker style="width: 10%" v-model:pureColor="start_color"
                      :disableAlpha="true" class="inline-element"/>
      </div>

      <div style="padding-bottom: 10px; text-align: center">
        Цвет ниток:
        <color-picker style="width: 10%" v-model:pureColor="ropes_color"
                      @pureColorChange="changeRopesColor($event)"
                      :disableAlpha="true" class="inline-element"/>
      </div>

      <hr>

      <ul class="row-container" style="margin-left: 0; padding-left: 0">
        <li v-for="index in Object.keys(elements)" v-bind:key="index"
            style="list-style-type: none; padding-bottom: 10px">
          <color-picker style="width: 10%" v-model:pureColor="elements_color[index]"
                        @pureColorChange="change_color($event, index)"
                        :disableAlpha="true" class="inline-element"/>
          <treeselect style="width: 80%" class="inline-element"
                      v-model="elements[index]" :close-on-select="false" :clearable="false"
                      :options="tree_options" placeholder="Выберите элемент..." :disable-branch-nodes="true"/>
          <CCloseButton style="width: 10%" @click="deleteRow(index)" class="inline-element"/>
        </li>
      </ul>

      <button @click="addRow" class="btn btn-primary small" id="add_button">
        Добавить
      </button>

      <hr>
      <button class="btn btn-primary small"
              style="width: 70%; margin-left: 15%; color: #f3dfdf; background-color: #0353b2;">
        Сохранить макет
      </button>
    </div>
  </div>
  <div id="footer">
    © Компания ООО "ЛенСИЗ", 2019.
  </div>
</template>

<script>

import {CCloseButton} from '@coreui/vue'
import * as Three from 'three';
import {reactive, defineComponent} from 'vue';
import {GLTFLoader} from "three/addons/loaders/GLTFLoader";
import {ColorPicker} from "vue3-colorpicker";
import "vue3-colorpicker/style.css";

import Treeselect from 'vue3-treeselect'
import 'vue3-treeselect/dist/vue3-treeselect.css'

export default defineComponent({
  name: 'App',
  components: {ColorPicker, CCloseButton, Treeselect},

  data() {
    return {
      sex: "Man",
      season: "Summer",
      last_element_id: 0,
      start_color: "rgb(215, 215, 215)",
      ropes_color: "rgb(0, 0, 0)",
      elements: {},
      active_elements: {},
      elements_to_models: {},
      elements_color: {},
      sex_selected: 'Man/Man/Man',
      sex_options: [
        {text: 'Мужчина', value: 'Man/Man/Man'},
        {text: 'Женщина', value: 'Woman/Human/Woman'},
      ],
      season_selected: 'Summer',
      season_options: [
        {text: 'Лето', value: 'Summer'},
        {text: 'Зима', value: 'Winter'},
      ],
      work_selected: 'Factory',
      work_options: [
        {text: 'Рабочий', value: 'Factory'}
      ],
      tree_options: [
        {
          id: -1,
          label: "Выберите элемент...",
          isDisabled: true
        },
        {
          id: "jackets",
          label: "Куртки",
          children: [
            {
              id: "Jacket/Jac_Main",
              label: "Jac_Col",
            },
            {
              id: "Lols",
              label: "Навесы",
              children: [
                {
                  id: "Jacket/Jac_Col",
                  label: "Jac_Col",
                },
                {
                  id: "Jacket/Jac_COP_BEHIND_V1",
                  label: "Jac_COP_BEHIND_V1",
                },
                {
                  id: "Jacket/Jac_COP_BEHIND_V2",
                  label: "Jac_COP_BEHIND_V2",
                },
                {
                  id: "Jacket/Jac_COP_FACE",
                  label: "Jac_COP_FACE",
                },
                {
                  id: "Jacket/Jac_COP_Hands",
                  label: "Jac_COP_Hands",
                },
                {
                  id: "Jacket/Jac_COP_Hands_FULL",
                  label: "Jac_COP_Hands_FULL",
                },
                {
                  id: "Jacket/Jac_COP_Hands_LIM",
                  label: "Jac_COP_Hands_LIM",
                },
                {
                  id: "Jacket/Jac_COP_TOP",
                  label: "Jac_COP_TOP",
                },
                {
                  id: "Jacket/Jac_COP_UNDERJac_Back",
                  label: "Jac_COP_UNDERJac_Back",
                },
                {
                  id: "Jacket/Jac_COP_UNDERJac_Face",
                  label: "Jac_COP_UNDERJac_Face",
                },
                {
                  id: "Jacket/Jac_Decor_Back",
                  label: "Jac_Decor_Back",
                },
                {
                  id: "Jacket/Jac_Decor_Pocket_LEFT_V2",
                  label: "Jac_Decor_Pocket_LEFT_V2",
                },
                {
                  id: "Jacket/Jac_Decor_Pocket_RIGHT_V2",
                  label: "Jac_Decor_Pocket_RIGHT_V2",
                },
                {
                  id: "Jacket/Jac_Decor_TOP",
                  label: "Jac_Decor_TOP",
                },
                {
                  id: "Jacket/Jac_Decor_TOP_FACE",
                  label: "Jac_Decor_TOP_FACE",
                },
                {
                  id: "Jacket/Jac_Hands",
                  label: "Jac_Hands",
                },
                {
                  id: "Jacket/Jac_Main",
                  label: "Jac_Main",
                },
                {
                  id: "Jacket/Jac_Planka",
                  label: "Jac_Planka",
                },
                {
                  id: "Jacket/Jac_Pocket_LEFT_V1",
                  label: "Jac_Pocket_LEFT_V1",
                },
                {
                  id: "Jacket/Jac_Pocket_LEFT_V1_Dop",
                  label: "Jac_Pocket_LEFT_V1_Dop",
                },
                {
                  id: "Jacket/Jac_Pocket_LEFT_V2",
                  label: "Jac_Pocket_LEFT_V2",
                },
                {
                  id: "Jacket/Jac_Pocket_RIGHT_V1",
                  label: "Jac_Pocket_RIGHT_V1",
                },
                {
                  id: "Jacket/Jac_Pocket_RIGHT_V1_Dop",
                  label: "Jac_Pocket_RIGHT_V1_Dop",
                },
                {
                  id: "Jacket/Jac_Pocket_RIGHT_V2",
                  label: "Jac_Pocket_RIGHT_V2",
                },
                {
                  id: "Jacket/Jac_Rope_Sleeves_V1",
                  label: "Jac_Rope_Sleeves_V1",
                },
                {
                  id: "Jacket/Jac_Rope_Sleeves_V2",
                  label: "Jac_Rope_Sleeves_V2",
                },
              ],
            },
          ],
        },
        {
          label: "Штаны",
          id: "pants",
          children: [
            {
              label:
                  "Штаны 1",
              id: "Pants/Pants_Main",
            },
            {
              label:
                  "Навесы",
              id: "Keks",
              children: [
                {
                  id: "Pants/Pants_COP_Knee_Back",
                  label: "Pants_COP_Knee_Back",
                },
                {
                  id: "Pants/Pants_COP_Knee_Face",
                  label: "Pants_COP_Knee_Face",
                },
                {
                  id: "Pants/Pants_COP_UNDERKnee",
                  label: "Pants_COP_UNDERKnee",
                },
                {
                  id: "Pants/Pants_Decor_Pocket_Left_V1",
                  label: "Pants_Decor_Pocket_Left_V1",
                },
                {
                  id: "Pants/Pants_Decor_Pocket_Left_V2",
                  label: "Pants_Decor_Pocket_Left_V2",
                },
                {
                  id: "Pants/Pants_Decor_Pocket_Right_V1",
                  label: "Pants_Decor_Pocket_Right_V1",
                },
                {
                  id: "Pants/Pants_Decor_Pocket_Right_V2",
                  label: "Pants_Decor_Pocket_Right_V2",
                },
                {
                  id: "Pants/Pants_Knee",
                  label: "Pants_Knee",
                },
                {
                  id: "Pants/Pants_Main",
                  label: "Pants_Main",
                },
                {
                  id: "Pants/Pants_Pocket_BEHINDE",
                  label: "Pants_Pocket_BEHINDE",
                },
                {
                  id: "Pants/Pants_Pocket_TOP",
                  label: "Pants_Pocket_TOP",
                },
                {
                  id: "Pants/Pocket_Left_V1",
                  label: "Pocket_Left_V1",
                },
                {
                  id: "Pants/Pocket_Left_V2",
                  label: "Pocket_Left_V2",
                },
                {
                  id: "Pants/Pocket_Right_V1",
                  label: "Pocket_Right_V1",
                },
                {
                  id: "Pants/Pocket_Right_V2",
                  label: "Pocket_Right_V2",
                },
              ],
            },
          ],
        },
      ],
    }
  },
  methods: {
    init: function () {
      this.rotation_angle = 0

      this.color = reactive({
        alpha: 1,
      });

      this.loader = new GLTFLoader();
      this.scene = new Three.Scene();

      this.models = [];

      this.lastMPos = {
        x: 0,
        y: 0
      };
      this.mouseClickedLeft = false;
      this.mouseClickedRight = false;

      let container = document.getElementById('viewer');

      this.camera = new Three.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.01, 100);
      this.camera.position.y = 1.0;
      this.camera.position.z = 2.5;
      this.camera.lookAt(0, 0.7, -1)

      const color = 0xFFFFFF;
      const intensity = 2.5;

      const light = new Three.AmbientLight(color, 0.5);
      this.scene.add(light);


      const light1 = new Three.DirectionalLight(color, intensity);
      light1.castShadow = true;
      light1.position.set(1, 5, 5);
      light1.target.position.set(-2, 0, -1);
      light1.shadow.mapSize.width = 4096;
      light1.shadow.mapSize.height = 4096;
      this.scene.add(light1);
      this.scene.add(light1.target);

      const light2 = new Three.DirectionalLight(color, 1);
      light2.castShadow = true;
      light2.position.set(-6, 3, 5);
      light2.target.position.set(-2, 0, -1);
      light2.shadow.mapSize.width = 4096;
      light2.shadow.mapSize.height = 4096;
      this.scene.add(light2);
      this.scene.add(light2.target);

      const loadManager = new Three.LoadingManager();
      const loader = new Three.TextureLoader(loadManager);
      const lensiz_texture = loader.load("lensiz_logo.jpg");

      let width = 8;

      const logoGeo = new Three.PlaneGeometry(width, width / 2.4);
      const logoMat = new Three.MeshPhongMaterial({map: lensiz_texture});

      const logo = new Three.Mesh(logoGeo, logoMat);
      logo.receiveShadow = true;
      logo.position.x = 0;
      logo.position.y = 1.1;
      logo.position.z = -1.99;
      this.scene.add(logo);

      const planeGeo = new Three.PlaneGeometry(40, 40);
      const planeMat = new Three.MeshPhongMaterial({color: 0xFFFFFF});
      const mesh1 = new Three.Mesh(planeGeo, planeMat);
      mesh1.receiveShadow = true;
      mesh1.rotation.x = Math.PI * -.5;
      mesh1.position.y = -1;
      this.scene.add(mesh1);

      const mesh2 = new Three.Mesh(planeGeo, planeMat);
      mesh2.receiveShadow = true;
      mesh2.position.z = -2;
      this.scene.add(mesh2);

      this.renderer = new Three.WebGLRenderer({antialias: true});
      this.renderer.shadowMap.enabled = true;
      this.renderer.setClearColor(0xaaaaaa, 1);
      this.renderer.setSize(container.clientWidth, container.clientHeight);

      container.appendChild(this.renderer.domElement);
    },

    UpdateModel(value, option) {
      this.scene.remove(this.models[this.elements_to_models[option]]);

      let color = this.elements_color[option]
      console.log(this.ropes_color)
      console.log(typeof (this.ropes_color))
      this.load_model(value, color, false, option, this.ropes_color);
    },

    addRow() {
      this.elements[this.last_element_id] = -1;
      this.elements_color[this.last_element_id] = this.start_color;
      this.last_element_id += 1;
    },
    deleteRow(index) {
      this.scene.remove(this.models[this.elements_to_models[index]]);
      delete this.elements[index];
      delete this.elements_color[index];
    },

    animate: function () {
      requestAnimationFrame(this.animate);
      this.renderer.render(this.scene, this.camera);
    },

    changeRopesColor: function () {
      let color = this.ropes_color
      for (let i = 0; i < this.models.length; i++) {
        this.models[i].traverse(function (model) {
          if (model.isMesh) {
            if (model.material.name === "Rope") {
              model.material.color = new Three.Color(color);
            }
          }
        })
      }
    },

    work_change: function (event) {
      if (typeof (event) != "string") {
        event = event.target.value;
      }
      this.work = event;
      console.log(event)
    },

    season_change: function (event) {
      if (typeof (event) != "string") {
        event = event.target.value;
      }
      this.season = event;
      if (this.season === "Winter" && this.work === "Factory") {
        this.tree_options = [
          {
            id: -1,
            label: "Выберите элемент...",
            isDisabled: true
          },
          {
            id: "Comb",
            label: "Комбинезоны",
            children: [
              {
                id: "Comb/Combinezon",
                label: "Combinezon",
              },
              {
                id: "Comb/COP_Back",
                label: "COP_Back",
              },
              {
                id: "Comb/COP_Front",
                label: "COP_Front",
              },
              {
                id: "Comb/COP_Under",
                label: "COP_Under",
              },
              {
                id: "Comb/Decor_Under",
                label: "Decor_Under",
              },
              {
                id: "Comb/Knee",
                label: "Knee",
              },
              {
                id: "Comb/Pocket",
                label: "Pocket",
              },
              {
                id: "Comb/Ziplock_Center",
                label: "Ziplock_Center",
              },
              {
                id: "Comb/Ziplock_L",
                label: "Ziplock_L",
              },
              {
                id: "Comb/Ziplock_R",
                label: "Ziplock_R",
              },
            ],
          },
          {
            label: "Hood1",
            id: "hood1",
            children: [
              {
                id: "Hood1/Hood1",
                label: "Hood1",
              },
            ],
          },
          {
            label: "Hood2",
            id: "hood2",
            children: [
              {
                id: "Hood2/Decor_Hood_Back",
                label: "Decor_Hood_Back",
              },
              {
                id: "Hood2/Hood2",
                label: "Hood2",
              },
              {
                id: "Hood2/Screed",
                label: "Screed",
              },
            ],
          },
          {
            label: "Jac_Winter",
            id: "Jac_Winter",
            children: [
              {
                id: "Jac_Winter/COP_Arm_Down",
                label: "COP_Arm_Down",
              },
              {
                id: "Jac_Winter/COP_Arm_Up",
                label: "COP_Arm_Up",
              },
              {
                id: "Jac_Winter/COP_Bust_V1",
                label: "COP_Bust_V1",
              },
              {
                id: "Jac_Winter/COP_Bust_V2",
                label: "COP_Bust_V2",
              },
              {
                id: "Jac_Winter/COP_Spine_V1",
                label: "COP_Spine_V1",
              },
              {
                id: "Jac_Winter/COP_Spine_V2",
                label: "COP_Spine_V2",
              },
              {
                id: "Jac_Winter/Decor_Breast",
                label: "Decor_Breast",
              },
              {
                id: "Jac_Winter/Decor_Hand_Down",
                label: "Decor_Hand_Down",
              },
              {
                id: "Jac_Winter/Decor_Hand_Up_V1",
                label: "Decor_Hand_Up_V1",
              },
              {
                id: "Jac_Winter/Decor_Hand_Up_V2",
                label: "Decor_Hand_Up_V2",
              },
              {
                id: "Jac_Winter/Decor_Planka",
                label: "Decor_Planka",
              },
              {
                id: "Jac_Winter/Decor_Pocket_Left_V1",
                label: "Decor_Pocket_Left_V1",
              },
              {
                id: "Jac_Winter/Decor_Pocket_Right_V1",
                label: "Decor_Pocket_Right_V1",
              },
              {
                id: "Jac_Winter/Decor_Shoulder",
                label: "Decor_Shoulder",
              },
              {
                id: "Jac_Winter/Decor_Strap_Hands",
                label: "Decor_Strap_Hands",
              },
              {
                id: "Jac_Winter/Jac_Winter",
                label: "Jac_Winter",
              },
              {
                id: "Jac_Winter/Jac_Winter_V2",
                label: "Jac_Winter_V2",
              },
              {
                id: "Jac_Winter/Neck",
                label: "Neck",
              },
              {
                id: "Jac_Winter/Planka",
                label: "Planka",
              },
              {
                id: "Jac_Winter/Pocket_Left_V1",
                label: "Pocket_Left_V1",
              },
              {
                id: "Jac_Winter/Pocket_Left_V2",
                label: "Pocket_Left_V2",
              },
              {
                id: "Jac_Winter/Pocket_Right_V1",
                label: "Pocket_Right_V1",
              },
              {
                id: "Jac_Winter/Pocket_Right_V2",
                label: "Pocket_Right_V2",
              },
              {
                id: "Jac_Winter/Rukav",
                label: "Rukav",
              },
              {
                id: "Jac_Winter/Strap_Hands",
                label: "Strap_Hands",
              },
              {
                id: "Jac_Winter/Ziplock_Center",
                label: "Ziplock_Center",
              },
            ],
          },
        ]
      }
      else if (this.season === "Summer" && this.work === "Factory") {
        this.tree_options = [
          {
            id: -1,
            label: "Выберите элемент...",
            isDisabled: true
          },
          {
            id: "jackets",
            label: "Куртки",
            children: [
              {
                id: "Jacket/Jac_Main",
                label: "Jac_Col",
              },
              {
                id: "Lols",
                label: "Навесы",
                children: [
                  {
                    id: "Jacket/Jac_Col",
                    label: "Jac_Col",
                  },
                  {
                    id: "Jacket/Jac_COP_BEHIND_V1",
                    label: "Jac_COP_BEHIND_V1",
                  },
                  {
                    id: "Jacket/Jac_COP_BEHIND_V2",
                    label: "Jac_COP_BEHIND_V2",
                  },
                  {
                    id: "Jacket/Jac_COP_FACE",
                    label: "Jac_COP_FACE",
                  },
                  {
                    id: "Jacket/Jac_COP_Hands",
                    label: "Jac_COP_Hands",
                  },
                  {
                    id: "Jacket/Jac_COP_Hands_FULL",
                    label: "Jac_COP_Hands_FULL",
                  },
                  {
                    id: "Jacket/Jac_COP_Hands_LIM",
                    label: "Jac_COP_Hands_LIM",
                  },
                  {
                    id: "Jacket/Jac_COP_TOP",
                    label: "Jac_COP_TOP",
                  },
                  {
                    id: "Jacket/Jac_COP_UNDERJac_Back",
                    label: "Jac_COP_UNDERJac_Back",
                  },
                  {
                    id: "Jacket/Jac_COP_UNDERJac_Face",
                    label: "Jac_COP_UNDERJac_Face",
                  },
                  {
                    id: "Jacket/Jac_Decor_Back",
                    label: "Jac_Decor_Back",
                  },
                  {
                    id: "Jacket/Jac_Decor_Pocket_LEFT_V2",
                    label: "Jac_Decor_Pocket_LEFT_V2",
                  },
                  {
                    id: "Jacket/Jac_Decor_Pocket_RIGHT_V2",
                    label: "Jac_Decor_Pocket_RIGHT_V2",
                  },
                  {
                    id: "Jacket/Jac_Decor_TOP",
                    label: "Jac_Decor_TOP",
                  },
                  {
                    id: "Jacket/Jac_Decor_TOP_FACE",
                    label: "Jac_Decor_TOP_FACE",
                  },
                  {
                    id: "Jacket/Jac_Hands",
                    label: "Jac_Hands",
                  },
                  {
                    id: "Jacket/Jac_Main",
                    label: "Jac_Main",
                  },
                  {
                    id: "Jacket/Jac_Planka",
                    label: "Jac_Planka",
                  },
                  {
                    id: "Jacket/Jac_Pocket_LEFT_V1",
                    label: "Jac_Pocket_LEFT_V1",
                  },
                  {
                    id: "Jacket/Jac_Pocket_LEFT_V1_Dop",
                    label: "Jac_Pocket_LEFT_V1_Dop",
                  },
                  {
                    id: "Jacket/Jac_Pocket_LEFT_V2",
                    label: "Jac_Pocket_LEFT_V2",
                  },
                  {
                    id: "Jacket/Jac_Pocket_RIGHT_V1",
                    label: "Jac_Pocket_RIGHT_V1",
                  },
                  {
                    id: "Jacket/Jac_Pocket_RIGHT_V1_Dop",
                    label: "Jac_Pocket_RIGHT_V1_Dop",
                  },
                  {
                    id: "Jacket/Jac_Pocket_RIGHT_V2",
                    label: "Jac_Pocket_RIGHT_V2",
                  },
                  {
                    id: "Jacket/Jac_Rope_Sleeves_V1",
                    label: "Jac_Rope_Sleeves_V1",
                  },
                  {
                    id: "Jacket/Jac_Rope_Sleeves_V2",
                    label: "Jac_Rope_Sleeves_V2",
                  },
                ],
              },
            ],
          },
          {
            label: "Штаны",
            id: "pants",
            children: [
              {
                label:
                    "Штаны 1",
                id: "Pants/Pants_Main",
              },
              {
                label:
                    "Навесы",
                id: "Keks",
                children: [
                  {
                    id: "Pants/Pants_COP_Knee_Back",
                    label: "Pants_COP_Knee_Back",
                  },
                  {
                    id: "Pants/Pants_COP_Knee_Face",
                    label: "Pants_COP_Knee_Face",
                  },
                  {
                    id: "Pants/Pants_COP_UNDERKnee",
                    label: "Pants_COP_UNDERKnee",
                  },
                  {
                    id: "Pants/Pants_Decor_Pocket_Left_V1",
                    label: "Pants_Decor_Pocket_Left_V1",
                  },
                  {
                    id: "Pants/Pants_Decor_Pocket_Left_V2",
                    label: "Pants_Decor_Pocket_Left_V2",
                  },
                  {
                    id: "Pants/Pants_Decor_Pocket_Right_V1",
                    label: "Pants_Decor_Pocket_Right_V1",
                  },
                  {
                    id: "Pants/Pants_Decor_Pocket_Right_V2",
                    label: "Pants_Decor_Pocket_Right_V2",
                  },
                  {
                    id: "Pants/Pants_Knee",
                    label: "Pants_Knee",
                  },
                  {
                    id: "Pants/Pants_Main",
                    label: "Pants_Main",
                  },
                  {
                    id: "Pants/Pants_Pocket_BEHINDE",
                    label: "Pants_Pocket_BEHINDE",
                  },
                  {
                    id: "Pants/Pants_Pocket_TOP",
                    label: "Pants_Pocket_TOP",
                  },
                  {
                    id: "Pants/Pocket_Left_V1",
                    label: "Pocket_Left_V1",
                  },
                  {
                    id: "Pants/Pocket_Left_V2",
                    label: "Pocket_Left_V2",
                  },
                  {
                    id: "Pants/Pocket_Right_V1",
                    label: "Pocket_Right_V1",
                  },
                  {
                    id: "Pants/Pocket_Right_V2",
                    label: "Pocket_Right_V2",
                  },
                ],
              },
            ],
          },
        ]
      }

      for (let index in this.elements) {
        console.log(index)
        this.scene.remove(this.models[this.elements_to_models[index]]);
        delete this.elements[index];
        delete this.elements_color[index];
      }
    },

    sex_change: function (model) {
      if (typeof (model) != "string") {
        model = model.target.value;
      }
      this.sex = model.split('/')[2]
      let model_path = model.split('/').slice(1).join('/');
      this.load_model(model_path, null, true)
    },

    load_model: function (model, color, sex_change_flag, index) {
      if (typeof (model) != "string") {
        model = model.target.value;
      }
      let rope_color = this.ropes_color;
      this.loader.load(`models/${this.work}/${this.season}/${this.sex}/${model}.glb`, (gltf) => {
        gltf.scene.position.y = -1;
        gltf.scene.position.z = -0.8;
        gltf.scene.rotation.y = this.rotation_angle;
        gltf.scene.traverse(function (model) {
          if (model.isMesh) {
            model.castShadow = true;
            if (color) {
              model.material.color = new Three.Color(color);
            }
            if (model.material.name === "Rope") {
              model.material.color = new Three.Color(rope_color);
            }
          }
        });
        if (sex_change_flag) {
          for (let i = 0; i < this.models.length; i++) {
            this.scene.remove(this.models[i]);
          }

          this.models = [];
          this.models.push(gltf.scene);

          for (let key in this.elements) {
            console.log(this.elements[key])
            if (this.elements[key] !== -1) {
              this.load_model(this.elements[key], this.elements_color[key], false, key, this.ropes_color)
            }
          }
        } else {
          this.models.push(gltf.scene);
        }
        this.elements_to_models[index] = this.models.length - 1;
        this.scene.add(gltf.scene);
      }, undefined, function (error) {
        console.error(error);
      });
    },

    change_color(value, index) {
      this.models[this.elements_to_models[index]].traverse(function (model) {
        if (model.isMesh) {
          if (model.material.name !== "Rope") {
            model.material.color = new Three.Color(value);
          }
        }
      })
    },

    mouseDownLeft() {
      this.mouseClickedLeft = true;
    },
    mouseUpLeft() {
      this.mouseClickedLeft = false;
    },
    mouseDownRight() {
      this.mouseClickedRight = true;
    },
    mouseUpRight() {
      this.mouseClickedRight = false;
    },
    mouseWheel(event) {
      this.camera.position.z = this.camera.position.z + event.deltaY / 500
      this.camera.position.z = Math.max(this.camera.position.z, -0.2)
      this.camera.position.z = Math.min(this.camera.position.z, 5)
    },
    mouseMove(event) {
      if (this.mouseClickedLeft) {
        for (let i = 0; i < this.models.length; i++) {
          this.models[i].rotation.y -= (this.lastMPos.x - event.clientX) * .005;
          this.rotation_angle = this.models[i].rotation.y
        }
      }
      if (this.mouseClickedRight) {
        this.camera.position.y -= (this.lastMPos.y - event.clientY) * 0.001;
        this.camera.position.y = Math.max(this.camera.position.y, -0.6)
        this.camera.position.y = Math.min(this.camera.position.y, 2.2)

        this.camera.position.x += (this.lastMPos.x - event.clientX) * 0.002;
        this.camera.position.x = Math.max(this.camera.position.x, -0.3)
        this.camera.position.x = Math.min(this.camera.position.x, 0.3)
      }

      this.lastMPos = {
        x: event.clientX,
        y: event.clientY
      };
    }
  },
  change_start_color(value) {
    this.start_color = value;
  },

  watch: {
    elements: {
      handler(val) {
        for (let key in val) {
          if (!(key in Object.keys(this.active_elements)) || val[key] !== this.active_elements[key]) {
            if (val[key] !== -1) {
              this.UpdateModel(val[key], key);
            }
          }
        }
        Object.assign(this.active_elements, val)
      },
      deep: true,
    }
  },

  mounted() {
    this.init();
    this.animate();
    this.work_change(this.work_selected);
    this.season_change(this.season_selected);
    this.sex_change(this.sex_selected);
  }
})
</script>

<style>
@font-face {
  font-family: Verdana;
  src: url('~@/assets/fonts/Verdana.ttf');
}

@font-face {
  font-family: Ubuntu;
  src: url('~@/assets/fonts/Ubuntu.ttf');
}

#menu {
  display: table-cell;
  float: left;
  width: 20%;
  border-radius: 10px;
  padding-right: 5%;
}

#viewer {
  display: table-cell;
  width: 70vw;
  height: 60vh;
  text-align: center;
}

#select {
  right: 0;
  top: 0;
  display: table-cell;
  vertical-align: middle;
  width: 30%;
  padding-left: 5%;
  margin-left: auto;
  margin-right: 0;
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

#logo {
  display: inline;
  vertical-align: middle;
  margin-right: 5vw;
  width: 15vw;
  padding-left: 5vw;
}

#wrapper {
  margin-left: 5vw;
  width: 90vw;
  height: 70vh;
}


#footer {
  background-color: #062051;
  position: fixed;
  right: 0;
  bottom: 0;
  text-align: center;
  width: 100%;
  font-size: 19px;
  color: #fafaff;
}

#add_button {
  text-align: center;
  background-color: #1ea83a;
  width: 70%;
  margin-left: 15%;
}

#add_button:hover {
  background-color: #96ff40;
}

header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 2vh;
  margin-bottom: 2vh;
}

.header_core {

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


.row-container {
  white-space: nowrap;
}

.inline-element {
  display: inline-block;
  vertical-align: middle;
  height: 100%;
}

</style>
