<template>
  <div class="cavas-container">
    <div class="moon-background"></div>
    <div class="sun-background"></div>
  </div>
</template>

<script>
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { RGBELoader } from "three/examples/jsm/loaders/RGBELoader";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader";

export default {
  setup() {
    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(
      45,
      innerWidth / innerHeight,
      0.1,
      1000
    );
    camera.position.set(0, 15, 50);

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(innerWidth, innerHeight);
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 0.5;
    renderer.outputEncoding = THREE.sRGBEncoding;
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFShadowMap;
    document.body.appendChild(renderer.domElement);

    // for sunLight Mode
    const sunLight = new THREE.DirectionalLight(
      new THREE.Color("#FFFFFF").convertSRGBToLinear(),
      1.5
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

    // for moonLight Mode
    const moonLight = new THREE.DirectionalLight(
      new THREE.Color("#77ccff").convertSRGBToLinear(),
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

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.target.set(0, 0, 0);
    controls.dampingFactor = 0.05;
    controls.enableDamping = true;
    controls.enableZoom = false;

    // 3D Lighting
    const loader = new RGBELoader();
    loader.load("texture/4k.hdr", function (texture) {
      texture.mapping = THREE.EquirectangularReflectionMapping;
      // scene.background = texture;
      scene.environment = texture;
    });

    let textures = {
      bump: new THREE.TextureLoader().load("texture/earthbump.jpg"),
      spec: new THREE.TextureLoader().load("texture/earthspec.jpg"),
      map: new THREE.TextureLoader().load("texture/earthsample4.jpg"),
      // planeTrailMask: new THREE.TextureLoader.load("texture/mask.png"),
    };

    // let plane = new GLTFLoader().load("texture/scene.glb");
    // let planeData = [makePlane(plane, textures.planeTrailMask, scene)];

    // renderer.setAnimationLoop(() => {
    //   planesData.forEach((planeData) => {
    //     let plane = planeData.group;

    //     plane.position.set(0, 0, 0);
    //     plane.rotation.set(0, 0, 0);
    //     plane.updateMatrixWorld();

    //     plane.translateY(planeData.yOff);
    //     plane.rotateOnAxis(new THREE.Vector3(1, 0, 0), +Math.PI * 0.5);
    //   });
    // });

    // function makePlane(planeMesh, trailTexture, scene) {
    //   let plane = planeMesh.clone();
    //   plane.scale.set(0.001, 0.001, 0.001);
    //   plane.position.set(0, 0, 0);
    //   plane.rotation.set(0, 0, 0);
    //   plane.updateMatrixWorld();

    //   plane.traverse((object) => {
    //     if (object instanceof THREE.Mesh) {
    //       object.castShadow = true;
    //       object.receiveShadow = true;
    //     }
    //   });

    //   let group = new THREE.Group();
    //   group.add(plane);
    //   scene.add(group);

    //   return {
    //     group,
    //     rot: 0,
    //     rad: 0.5,
    //     yOff: 10.5 + Math.random() * 1.0,
    //   };
    // }

    let globe = new THREE.Mesh(
      new THREE.SphereGeometry(12, 70, 70),
      new THREE.MeshPhysicalMaterial({
        map: textures.map,
        roughnessMap: textures.spec,
        bumpMap: textures.bump,
        bumpScale: 0.05,
        envMapIntensity: 1,

        // make globe feel cool
        sheen: 1,
        sheenRoughness: 0.75,
        sheenColor: new THREE.Color("#ff8a00").convertSRGBToLinear(),
        clearcoat: 0.5,
      })
    );
    globe.receiveShadow = true;

    scene.add(globe);

    // pointer Load
    function convertLatLng(p) {
      let lat = (90 - p.lat * Math.PI) / 180;
      let lng = (180 + p.lng * Math.PI) / 180;

      let x = -Math.sin(lat) * Math.cos(lng) - 3;
      let y = Math.sin(lat) * Math.sin(lng) + 8;
      let z = Math.cos(lat) + 10;

      return {
        x,
        y,
        z,
      };
    }

    // country coordinates
    let point1 = {
      lat: 38.895,
      lng: 77.015,
    };
    let pos = convertLatLng(point1);

    let pointer = new GLTFLoader();
    pointer.load("texture/pointer.glb", function (gltf) {
      gltf.scene.position.set(pos.x, pos.y, pos.z);
      gltf.scene.scale.set(0.05, 0.05, 0.05);
      scene.add(gltf.scene);
    });
    pointer.load("texture/pointer.glb", function (gltf) {
      gltf.scene.position.set(pos.x - 3.5, pos.y, pos.z - 19.5);
      gltf.scene.scale.set(0.05, 0.05, 0.05);
      scene.add(gltf.scene);
    });
    pointer.load("texture/pointer.glb", function (gltf) {
      gltf.scene.position.set(pos.x + 11, pos.y + 2.5, pos.z - 8);
      gltf.scene.scale.set(0.05, 0.05, 0.05);
      scene.add(gltf.scene);
    });

    // show model
    function animate() {
      renderer.setAnimationLoop(() => {
        scene.rotation.y += 0.0015;
        renderer.render(scene, camera);
      });
    }
    animate();
  },
};
</script>

<style>
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
  position: relative;
}
</style>
