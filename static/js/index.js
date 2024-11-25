(() => {
    'use strict';

    // 亮度调节
    const adjustLightInput = document.getElementById('adjust-light');
    let lightAlpha = localStorage.getItem('GraphPreviewerLightAlpha');
    if (lightAlpha === null) {
        lightAlpha = adjustLightInput.value;
    } else {
        lightAlpha = parseInt(lightAlpha);
    }
    adjustLight({target: {value: lightAlpha}});
    adjustLightInput.addEventListener('input', adjustLight);

    function adjustLight(e) {
        const a = parseFloat((e.target.value * 0.01).toFixed(2));
        document.querySelector('body > .shade').style.backgroundColor = `rgba(0, 0, 0, ${a})`;
        localStorage.setItem('GraphPreviewerLightAlpha', e.target.value);
        adjustLightInput.value = e.target.value;
    }
})();
