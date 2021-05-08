import "./vendor/three.r119.min.js";
import "./vendor/vanta.waves.min.js";
import "./vendor/vanta.waves.min.js";

let effect = null
const color = new URL(import.meta.url).searchParams.get('color')
console.log('color from url', color)
const theme_color = color ? parseInt(`0x${color}`) : 0x005182
console.log('theme color', theme_color)

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
