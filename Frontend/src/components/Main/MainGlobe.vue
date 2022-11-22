<template>
  <div class="canvas-container">
    <div
      id="tooltip"
      style="
        left: 0;
        top: 0;
        position: fixed;
        min-width: 15px;
        text-align: center;
        font-family: monospace;
        font-weight: bold;
        display: none;
        opacity: 0;
        border : 1px, solid, black
        transition: opacity 0.25s linear;
        border-radius: 3px;
        width: 55px;
        height: 55px;
      "
    ></div>
  </div>
</template>

<script>
import {
  // DoubleSide,
  PCFSoftShadowMap,
  MeshPhysicalMaterial,
  TextureLoader,
  FloatType,
  PMREMGenerator,
  Scene,
  PerspectiveCamera,
  WebGLRenderer,
  Color,
  ACESFilmicToneMapping,
  sRGBEncoding,
  Mesh,
  SphereGeometry,
  Vector2,
  DirectionalLight,
  Clock,
  Vector3,
  PlaneGeometry,
  Group,
  Raycaster,
} from "three";
import { watchEffect } from "vue";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { RGBELoader } from "three/examples/jsm/loaders/RGBELoader";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader";
import { onMounted } from "@vue/runtime-core";
import { useStore } from "vuex";
// import { useRouter } from "vue-router";
export default {
  setup() {
    // const router = useRouter();
    const store = useStore();
    // const router = useRouter();
    // const canvas = document.querySelector('.canvas-container')
    const scene = new Scene();
    const camera = new PerspectiveCamera(
      45,
      innerWidth / innerHeight,
      0.1,
      1000
    );

    camera.position.set(0, 15, 30); // model camera set
    const renderer = new WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(innerWidth, innerHeight); // 캔버스 사이즈 때문에 조정함

    renderer.toneMapping = ACESFilmicToneMapping;
    renderer.outputEncoding = sRGBEncoding;
    renderer.physicallyCorrectLights = true;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = PCFSoftShadowMap;
    onMounted(() => {
      let flag = false;
      if (flag === false) {
        // router.go();
        flag = true;
      }
      document.querySelector(".globe-area").appendChild(renderer.domElement);
    });
    function sleep(sec) {
      return new Promise((resolve) => setTimeout(resolve, sec * 1000));
    } // 함수정의
    const checkglobeloading = watchEffect(async () => {
      await sleep(3);
      if (document.querySelector(".globe-area > canvas")) {
        store.commit("SET_DATALABVIEWLOADING", false);
      }
    });
    const sunLight = new DirectionalLight(
      new Color("#FFFFFF").convertSRGBToLinear(),
      3.5
    );
    sunLight.position.set(10, 20, 10);
    sunLight.castShadow = true;
    sunLight.shadow.mapSize.width = 512;
    sunLight.shadow.mapSize.height = 512;
    sunLight.shadow.camera.near = 0.5;
    sunLight.shadow.camera.far = 100;
    sunLight.shadow.camera.left = -10;
    sunLight.shadow.camera.bottom = -10;
    sunLight.shadow.camera.top = 10;
    sunLight.shadow.camera.right = 10;
    scene.add(sunLight);

    const moonLight = new DirectionalLight(
      new Color("#77ccff").convertSRGBToLinear(),
      0
    );
    moonLight.position.set(-10, 20, 10);
    moonLight.castShadow = true;
    moonLight.shadow.mapSize.width = 512;
    moonLight.shadow.mapSize.height = 512;
    moonLight.shadow.camera.near = 0.5;
    moonLight.shadow.camera.far = 100;
    moonLight.shadow.camera.left = -10;
    moonLight.shadow.camera.bottom = -10;
    moonLight.shadow.camera.top = 10;
    moonLight.shadow.camera.right = 10;
    scene.add(moonLight);

    // orbitcontrols
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.target.set(0, 0, 0);
    controls.dampingFactor = 0.05;
    controls.enableDamping = true;
    controls.enableZoom = false;
    controls.enablePan = false;

    let mousePos = new Vector2(0, 0);

    (async function () {
      let pmrem = new PMREMGenerator(renderer);
      let envmapTexture = await new RGBELoader()
        .setDataType(FloatType)
        .loadAsync("texture/4k.hdr");

      //globetexture
      let envMap = pmrem.fromEquirectangular(envmapTexture).texture;
      let textures = {
        bump: await new TextureLoader().loadAsync("texture/earthbump.jpg"),
        map: await new TextureLoader().loadAsync("texture/earthsample4.jpg"),
        spec: await new TextureLoader().loadAsync("texture/earthspec.jpg"),
        planeTrailMask: await new TextureLoader().loadAsync("texture/mask.png"),
      };

      //globe
      let sphere = new Mesh(
        new SphereGeometry(10.5, 70, 70),
        new MeshPhysicalMaterial({
          map: textures.map,
          roughnessMap: textures.spec,
          bumpMap: textures.bump,
          bumpScale: 0.05,
          envMap,
          envMapIntensity: 0.4,
          sheen: 1,
          sheenRoughness: 0.75,
          sheenColor: new Color("#ff8a00").convertSRGBToLinear(),
          clearcoat: 0.5,
        })
      );
      sphere.sunEnvIntensity = 0.4;
      sphere.moonEnvIntensity = 0.1;
      sphere.rotation.y += Math.PI * 1.25;
      sphere.receiveShadow = true;
      scene.add(sphere);

      let plane = (await new GLTFLoader().loadAsync("texture/scene.glb")).scene
        .children[0];

      // marker model

      var hoveredObj = undefined;
      var tooltipEnabledObjects = [];
      var latestMouseProjection = undefined;
      var tooltipDisplayTimeout = undefined;

      // us
      let marker = (await new GLTFLoader().loadAsync("texture/pointer.glb"))
        .scene.children[0];
      marker.scale.set(0.05, 0.05, 0.05);
      marker.position.set(-5, 6, -8);

      marker.userData.tooltipText = "미국";
      marker.userData.name = "미국";
      tooltipEnabledObjects.push(marker);
      scene.add(marker);
      // uk
      let marker1 = (await new GLTFLoader().loadAsync("texture/pointer.glb"))
        .scene.children[0];
      marker1.scale.set(0.05, 0.05, 0.05);
      marker1.position.set(-6, 8.5, 3.5);
      tooltipEnabledObjects.push(marker1);
      scene.add(marker1);
      // jp
      let marker2 = (await new GLTFLoader().loadAsync("texture/pointer.glb"))
        .scene.children[0];
      marker2.scale.set(0.05, 0.05, 0.05);
      marker2.position.set(8.5, 7, 1);
      tooltipEnabledObjects.push(marker2);
      scene.add(marker2);
      // vi
      let marker3 = (await new GLTFLoader().loadAsync("texture/pointer.glb"))
        .scene.children[0];
      marker3.scale.set(0.05, 0.05, 0.05);
      marker3.position.set(8.5, 3, 7);
      tooltipEnabledObjects.push(marker3);
      scene.add(marker3);
      // ind
      let marker4 = (await new GLTFLoader().loadAsync("texture/pointer.glb"))
        .scene.children[0];
      marker4.scale.set(0.05, 0.05, 0.05);
      marker4.position.set(10, 0, 5.5);
      tooltipEnabledObjects.push(marker4);
      scene.add(marker4);
      // br
      let marker5 = (await new GLTFLoader().loadAsync("texture/pointer.glb"))
        .scene.children[0];
      marker5.scale.set(0.05, 0.05, 0.05);
      marker5.position.set(-10.5, -2.5, -4);
      tooltipEnabledObjects.push(marker5);
      scene.add(marker5);

      // marker event =======================================================================
      // TODO: object - id 로 접근, parmas로 분기처리
      const pointer = new Vector2();
      const raycaster = new Raycaster();

      const showTooltip = function () {
        var divElement = document.getElementById("tooltip");
        if (divElement && latestMouseProjection) {
          divElement.style.display = "block";
          divElement.style.opacity = 0.0;

          var canvasHalfWidth = renderer.domElement.offsetWidth / 2;
          var canvasHalfHeight = renderer.domElement.offsetHeight / 2;

          var tooltipPosition = latestMouseProjection.clone().project(camera);
          tooltipPosition.x =
            tooltipPosition.x * canvasHalfWidth +
            canvasHalfWidth +
            renderer.domElement.offsetLeft;
          tooltipPosition.y =
            -(tooltipPosition.y * canvasHalfHeight) +
            canvasHalfHeight +
            renderer.domElement.offsetTop;

          // var tootipWidth = divElement.width;
          // var tootipHeight = divElement.height;
          // 여기가 툴팁 위치
          // divElement.style.left = `${tooltipPosition.x - tootipWidth / 2}px`;
          divElement.style.left = `${tooltipPosition.x}px`;
          divElement.style.top = `${tooltipPosition.y}px`;
          // console.log(hoveredObj, "hoveredObj");

          if (hoveredObj.id == 51) {
            divElement.innerHTML =
              '<img src="/texture/us.png" style="width: 100%; height: 100%;">';
          }
          if (hoveredObj.id == 57) {
            divElement.innerHTML =
              '<img src="/texture/uk.png" style="width: 100%; height: 100%;">';
          }
          if (hoveredObj.id == 63) {
            divElement.innerHTML =
              '<img src="/texture/jp.png" style="width: 100%; height: 100%;">';
          }
          if (hoveredObj.id == 69) {
            divElement.innerHTML =
              '<img src="/texture/vi.png" style="width: 100%; height: 100%;">';
          }
          if (hoveredObj.id == 75) {
            divElement.innerHTML =
              '<img src="/texture/in.png" style="width: 100%; height: 100%;">';
          }
          if (hoveredObj.id == 81) {
            divElement.innerHTML =
              '<img src="/texture/br.png" style="width: 100%; height: 100%;">';
          }

          // divElement.innerText = hoveredObj.userData.name;

          setTimeout(function () {
            divElement.style.opacity = 1.0;
          }, 25);
        }
      };

      const hideTooltip = function () {
        var divElement = document.querySelector("#tooltip");
        if (divElement) {
          divElement.style.display = "none";
        }
      };

      const updateMouseCoords = function (event, coordsObj) {
        coordsObj.x =
          ((event.clientX - renderer.domElement.offsetLeft + 0.5) /
            window.innerWidth) *
            2 -
          1;
        coordsObj.y =
          -(
            (event.clientY - renderer.domElement.offsetTop + 0.5) /
            window.innerHeight
          ) *
            2 +
          1;
      };

      const handleManipulationUpdate = function () {
        raycaster.setFromCamera(pointer, camera);
        const intersects = raycaster.intersectObjects(tooltipEnabledObjects);
        if (intersects.length > 0) {
          latestMouseProjection = intersects[0].point;
          hoveredObj = intersects[0].object;
        }

        if (tooltipDisplayTimeout || !latestMouseProjection) {
          clearTimeout(tooltipDisplayTimeout);
          tooltipDisplayTimeout = undefined;
          hideTooltip();
        }

        if (!tooltipDisplayTimeout && latestMouseProjection) {
          tooltipDisplayTimeout = setTimeout(function () {
            tooltipDisplayTimeout = undefined;
            showTooltip();
          }, 100);
        }
      };

      const onMouseMove1 = (e) => {
        updateMouseCoords(e, pointer);
        latestMouseProjection = undefined;
        hoveredObj = undefined;
        handleManipulationUpdate();
      };

      window.addEventListener("mousemove", onMouseMove1, false);

      const onMouseMove = (e) => {
        pointer.x = (e.clientX / window.innerWidth) * 2 - 1;
        pointer.y = -(e.clientY / window.innerHeight) * 2 + 1;
        raycaster.setFromCamera(pointer, camera);
        const intersects = raycaster.intersectObjects(scene.children);
        // console.log(intersects, "inter감지");
        if (intersects.length >= 2) {
          if (intersects[0].object.id == 51) {
            // alert(intersects[0].object.id + "미국클릭");
            // local 53
            // 배포 51
            const nation = 1;
            store.dispatch("setNation", { nation });
            store.dispatch("getNationRate", { nation });

            const data = true;
            store.dispatch("setIsOverlay", { data });
          }
          if (intersects[0].object.id == 57) {
            // alert(intersects[0].object.id + "영국클릭");
            // local 59
            // 배포 57

            const nation = 2;
            store.dispatch("setNation", { nation });
            store.dispatch("getNationRate", { nation });

            const data = true;
            store.dispatch("setIsOverlay", { data });
          }
          if (intersects[0].object.id == 63) {
            // local 65
            // 배포 63
            const nation = 3;
            store.dispatch("setNation", { nation });
            store.dispatch("getNationRate", { nation });

            const data = true;
            store.dispatch("setIsOverlay", { data });
          }
          if (intersects[0].object.id == 69) {
            //local 71
            //배포 69
            const nation = 4;
            store.dispatch("setNation", { nation });
            store.dispatch("getNationRate", { nation });

            const data = true;
            store.dispatch("setIsOverlay", { data });
          }
          if (intersects[0].object.id == 75) {
            // local 77
            // 배포 75
            const nation = 5;
            store.dispatch("setNation", { nation });
            store.dispatch("getNationRate", { nation });

            const data = true;
            store.dispatch("setIsOverlay", { data });
          }
          if (intersects[0].object.id == 81) {
            // local 83
            // 배포 81
            const nation = 6;
            store.dispatch("setNation", { nation });
            store.dispatch("getNationRate", { nation });

            const data = true;
            store.dispatch("setIsOverlay", { data });
          }
        }
      };
      window.addEventListener("click", onMouseMove);
      // 절대 수정하지 마세용 ==================================================

      // plane model
      let planesData = [
        makePlane(plane, textures.planeTrailMask, envMap, scene),
        makePlane(plane, textures.planeTrailMask, envMap, scene),
        makePlane(plane, textures.planeTrailMask, envMap, scene),
        makePlane(plane, textures.planeTrailMask, envMap, scene),
        makePlane(plane, textures.planeTrailMask, envMap, scene),
      ];

      let clock = new Clock();

      renderer.setAnimationLoop(() => {
        let delta = clock.getDelta();
        scene.rotation.y += delta * 0.05;

        controls.update();
        renderer.render(scene, camera);

        planesData.forEach((planeData) => {
          let plane = planeData.group;

          plane.position.set(0, 0, 0);
          plane.rotation.set(0, 0, 0);
          plane.updateMatrixWorld();

          planeData.rot += delta;
          plane.rotateOnAxis(planeData.randomAxis, planeData.randomAxisRot); // random axis
          plane.rotateOnAxis(new Vector3(0, 1, 0), planeData.rot); // y-axis rotation
          plane.rotateOnAxis(new Vector3(0, 0, 1.1), planeData.rad); // this decides the radius
          plane.translateY(planeData.yOff);
          plane.rotateOnAxis(new Vector3(1, 0, 0), +Math.PI * 0.5);
        });

        renderer.autoClear = false;
        // renderer.render(ringsScene, ringsCamera);
        renderer.autoClear = true;
      });
    })();

    function nr() {
      return Math.random() * 2 - 1;
    }

    function makePlane(planeMesh, trailTexture, envMap, scene) {
      let plane = planeMesh.clone();
      plane.scale.set(0.001, 0.001, 0.001);
      plane.position.set(0, 0, 0);
      plane.rotation.set(0, 0, 0);
      plane.updateMatrixWorld();

      plane.traverse((object) => {
        if (object instanceof Mesh) {
          object.material.envMap = envMap;
          object.sunEnvIntensity = 1;
          object.moonEnvIntensity = 0.3;
          object.castShadow = true;
          object.receiveShadow = true;
        }
      });

      let trail = new Mesh(
        new PlaneGeometry(1, 2),
        new MeshPhysicalMaterial({
          envMap,
          envMapIntensity: 3,

          roughness: 0.4,
          metalness: 0,
          transmission: 1,

          transparent: true,
          opacity: 1,
          alphaMap: trailTexture,
        })
      );
      trail.sunEnvIntensity = 3;
      trail.moonEnvIntensity = 0.7;
      trail.rotateX(Math.PI);
      trail.translateY(1.1);

      let group = new Group();
      group.add(plane);
      group.add(trail);

      scene.add(group);

      return {
        sleep,
        checkglobeloading,
        group,
        yOff: 10.5 + Math.random() * 1.0,
        rot: Math.PI * 2, // just to set a random starting point
        rad: Math.random() * Math.PI * 0.45 + Math.PI * 0.05,
        randomAxis: new Vector3(nr(), nr(), nr()).normalize(),
        randomAxisRot: Math.random() * Math.PI * 2,
      };
    }

    window.addEventListener("mousemove", (e) => {
      let x = e.clientX - innerWidth * 0.5;
      let y = e.clientY - innerHeight * 0.5;

      mousePos.x = x * 0.0003;
      mousePos.y = y * 0.0003;
    });
  },
};
</script>

<style scoped>
.sun-background {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, rgb(255 219 158), rgb(253 243 220));
  opacity: 1;
}
.moon-background {
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(313deg, #0b1a2b, #3a6291 111%);
  opacity: 1;
}
canvas {
  /* position: absolute;
  top: 20%;
  right: 15%; */
  z-index: 100;
}
</style>
