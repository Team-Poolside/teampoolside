import "./vendor/three.r119.min.js";
import "./vendor/vanta.waves.min.js";
import "./vendor/vanta.waves.min.js";

let effect = null;
let theme_color;

if (!document.currentScript) {
    theme_color = 0x005182; // fallback to poolside blue
} else {
    theme_color = parseInt(document.currentScript.getAttribute("color"))
}

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
            color: theme_color,
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
