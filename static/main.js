function createBar(container, p) {
   return new ProgressBar.Line(container, {
      strokeWidth: 4,
      easing: "easeInOut",
      duration: 800,
      color: "#069",
      trailColor: "none",
      trailWidth: 1,
      svgStyle: { width: "100%", height: "100%" },

      step: (state, bar) => {
         p.innerHTML = Math.round(bar.value() * 100) + " %";
      }
   });
}
