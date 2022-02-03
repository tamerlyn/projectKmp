const body = document.getElementById("trigger");
const background = document.getElementById("auth-background");

body.addEventListener('click', () => {
  background.muted = false;
  background.play()
});