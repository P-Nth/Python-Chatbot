const hideToggler = document.querySelector(".chatclient_container");
const maximizeToggler = document.querySelector("#max_toggler");
const maximizeChatOpener = document.querySelector(".opener");
const alignSendButton = document.querySelector(".send_btn");
const maximizeActualMessage = document.querySelector(".message");
const viewToggleIcon = document.querySelector("#view_toggler");

viewToggleIcon.addEventListener("click", (e) => {
  hideToggler.classList.toggle("hide");
});
maximizeToggler.addEventListener("click", (e) => {
  // hideToggler.classList.toggle("hide");
  hideToggler.classList.toggle("maximize");
  maximizeChatOpener.classList.toggle("maximize");
  maximizeActualMessage.classList.toggle("maximize");
  alignSendButton.classList.toggle("maximize");
});
