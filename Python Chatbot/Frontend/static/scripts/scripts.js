// const hideToggler = document.querySelector(".chatclient_container");
// const viewToggleIcon = document.querySelector("#view_toggler");

const { get } = require("express/lib/response");

// viewToggleIcon.addEventListener("click", (e) => {
//   hideToggler.classList.toggle("hide");
// });

class ChatClient {
  constructor() {
    this.args = {
      viewToggleIcon: document.querySelector(".chatclient_container"),
      chatClient: document.querySelector(".chatclient_container"),
      sendButton: document.querySelector(".chatclient_container"),
    };

    this.state = false;
    this.messages = [];
  }

  display() {
    const { viewToggleIcon, chatClient, sendButton } = this.args;

    viewToggleIcon.addEventListener("click", () =>
      this.toggleState(chatClient)
    );

    sendButton.addEventListener("click", () =>
      this.onSubmitMessage.state(chatClient)
    );

    const node = chatClient.querySelector("input");
    node.addEventListener("keyup", ({ key }) => {
      if (key === "Enter") {
        this.onSubmitMessage(chatClient);
      }
    });
  }

  toggleState(chatClient) {
    this.state = !this.state;

    if (this.state) {
      chatClient.classList.add("unhide");
    } else {
      chatClient.classList.remove("unhide ");
    }
  }

  onSubmitMessage(chatClient) {
    let inputField = chatClient.querySelector("input");
    let inputMessage = inputMessage.value;
    if (inputMessage === "") {
      return;
    }

    let getMessage = { name: "User", user_message: inputMessage };
    this.messages.push(getMessage);

    fetch("http://127.0.0.1:5000/analy", {
      method: "POST",
      body: JSON.stringify({ user_message: inputMessage }),
      mode: "cors",
      headers: {
        "Content-Type": "webApp/json",
      },
    })
      .then((r) => r.json())
      .then((r) => {
        let getSecondMessage = { name: "AI", message: r.reply };
        this.messages.push(getSecondMessage);
        this.updateReplyText(chatClient);
        inputField.value = "";
      })
      .catch((error) => {
        console.log("Error", error);
        this.updateReplyText(chatClient);
        inputField.value = "";
      });
  }

  updateReplyText(chatClient) {
    let plainText = "";
    this.messages
      .slice()
      .reverse()
      .forEach(function (item) {
        if (item.name == "AI") {
          plainText +=
            '<div class="incoming"> <div class="profile"> <img class="profilepic" src="../static/images/incoming.png" alt="incoming profile"/> </div> <div class="actual_msg"> <div class="message" id="actual_msg">' +
            item.reply +
            "</div> </div>";
        } else {
          plainText +=
            '<div class="outgoing" key=""> <div class="actual_msg"> <div class="message" id="actual_msg">' +
            item.reply +
            '</div> <div class="profile"> <img class="profilepic" src="../static/images/outgoing.png" alt="outgoing profile"/> </div> </div>';
        }
      });

    const messageChats = chatClient.querySelector(".scroll_view");
    messageChats.innerHTML = plainText;
  }
}

const chatClient = new ChatClient();
chatClient.display();
