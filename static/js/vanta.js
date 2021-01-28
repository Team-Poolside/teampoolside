import "./vendor/three.r119.min.js";
import "./vendor/vanta.waves.min.js";
import "./vendor/vanta.waves.min.js";

let effect = null;

// old color: 0x005182

export const toggleBackgroundEffect = () => {
    if (!effect) {
        effect = VANTA.WAVES({
            el: "#vanta",
            mouseControls: true,
            touchControls: true,
            gyroControls: true,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x005182,
            shininess: 27.00,
            waveHeight: 21.50,
            waveSpeed: 0.90
        });
    } else {
        effect.destroy();
        effect = null;
    }
}

toggleBackgroundEffect();

document.getElementById('effect-control').onclick = toggleBackgroundEffect;
