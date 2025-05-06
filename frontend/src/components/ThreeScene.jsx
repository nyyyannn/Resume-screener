import React, { useEffect, useRef } from "react";
import * as THREE from "three";

const ThreeScene = () => {
  const containerRef = useRef(null);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(
      75,
      container.clientWidth / container.clientHeight,
      0.1,
      1000
    );
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    // Create document stack
    const documentStack = new THREE.Group();
    const paperGeometry = new THREE.BoxGeometry(5, 7, 0.05);
    const paperMaterials = [
      new THREE.MeshBasicMaterial({ color: 0xffffff }),
      new THREE.MeshBasicMaterial({ color: 0xf8fafc }),
      new THREE.MeshBasicMaterial({ color: 0xe2e8f0 }),
    ];

    for (let i = 0; i < 15; i++) {
      const material = paperMaterials[i % paperMaterials.length];
      const paper = new THREE.Mesh(paperGeometry, material);
      paper.position.z = i * 0.07;
      paper.position.x = Math.sin(i * 0.2) * 0.3;
      paper.position.y = Math.cos(i * 0.1) * 0.1;
      paper.rotation.z = (Math.random() - 0.5) * 0.1;
      documentStack.add(paper);
    }

    scene.add(documentStack);

    // Scanner
    const scannerGeometry = new THREE.PlaneGeometry(6, 8);
    const scannerMaterial = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      transparent: true,
      opacity: 0.3,
      side: THREE.DoubleSide,
    });
    const scanner = new THREE.Mesh(scannerGeometry, scannerMaterial);
    scanner.position.z = 2;
    scanner.position.y = -5;
    scene.add(scanner);

    // AI Visualization
    const aiGroup = new THREE.Group();
    const particleCount = 100;
    const particles = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount; i++) {
      const i3 = i * 3;
      positions[i3] = (Math.random() - 0.5) * 8;
      positions[i3 + 1] = (Math.random() - 0.5) * 8;
      positions[i3 + 2] = (Math.random() - 0.5) * 8;
    }

    particles.setAttribute("position", new THREE.BufferAttribute(positions, 3));

    const particleMaterial = new THREE.PointsMaterial({
      color: 0x38bdf8,
      size: 0.2,
      transparent: true,
      opacity: 0.7,
    });

    const particleSystem = new THREE.Points(particles, particleMaterial);
    aiGroup.add(particleSystem);

    const lineGeometry = new THREE.BufferGeometry();
    const linePositions = [];

    for (let i = 0; i < particleCount; i++) {
      for (let j = i + 1; j < particleCount; j++) {
        const dx = positions[i * 3] - positions[j * 3];
        const dy = positions[i * 3 + 1] - positions[j * 3 + 1];
        const dz = positions[i * 3 + 2] - positions[j * 3 + 2];
        const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
        if (dist < 2) {
          linePositions.push(
            positions[i * 3],
            positions[i * 3 + 1],
            positions[i * 3 + 2],
            positions[j * 3],
            positions[j * 3 + 1],
            positions[j * 3 + 2]
          );
        }
      }
    }

    lineGeometry.setAttribute("position", new THREE.Float32BufferAttribute(linePositions, 3));

    const lineMaterial = new THREE.LineBasicMaterial({
      color: 0x38bdf8,
      transparent: true,
      opacity: 0.3,
    });

    const lineSystem = new THREE.LineSegments(lineGeometry, lineMaterial);
    aiGroup.add(lineSystem);

    aiGroup.position.z = -5;
    scene.add(aiGroup);

    camera.position.z = 10;

    const handleResize = () => {
      const width = container.clientWidth;
      const height = container.clientHeight;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    };
    window.addEventListener("resize", handleResize);

    const animate = () => {
      requestAnimationFrame(animate);

      scanner.position.y += 0.05;
      if (scanner.position.y > 5) {
        scanner.position.y = -5;
      }

      aiGroup.rotation.y += 0.002;
      aiGroup.rotation.x += 0.001;

      renderer.render(scene, camera);
    };

    animate();

    return () => {
      window.removeEventListener("resize", handleResize);
      container.removeChild(renderer.domElement);
    };
  }, []);

  return (
    <div
      ref={containerRef}
      className="w-full h-[600px] lg:w-1/2 lg:h-[600px] overflow-hidden"
    />
  );
};

export default ThreeScene;
