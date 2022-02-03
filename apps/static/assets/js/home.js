const vid = document.getElementById("background");
const sound_control = document.getElementById("sound-control");
const sound_icon = document.getElementById("sound-img");
const search_text = document.getElementById("search-text");
const search_phrase = document.getElementById("search-phrase");
const search_button = document.getElementById("search-button");
const result = document.getElementById("raw_text");

sound_control.addEventListener('click', () => {
  vid.muted = !vid.muted;
  if (vid.muted) {
    sound_icon.src = "/static/assets/media/muted.png";
    search_text.disabled = true;
    search_phrase.disabled = true;
    search_phrase.placeholder = "Звук не включен, поиск невозможен";
    search_button.disabled = true;
  }
  else {
    sound_icon.src = "/static/assets/media/unmuted.png";
    search_text.disabled = false;
    search_phrase.disabled = false;
    search_phrase.placeholder = "Введите фразу для поиска...";
    search_button.disabled = false;
  }
});