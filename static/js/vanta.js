import "./vendor/three.r119.min.js";
import "./vendor/vanta.waves.min.js";
import "./vendor/vanta.waves.min.js";

let effect = null;

const yuleside_red  = 0x6e001a
const wavepool_pink = 0x9e0a8e
const poolside_blue = 0x005182

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
            color: poolside_blue,
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
