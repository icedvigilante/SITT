const keys = {}

window.addEventListener('keydown', (ev) => {
  keys[ev.key] = true
})

window.addEventListener('keyup', (ev) => {
  if (keys['z'] && keys['g']) {
    console.log("F1 + 1 pressed!")
      document.getElementById('loginhidden').click();
  }
  keys[ev.key] = false
})