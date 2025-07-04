async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div><b>You:</b> ${message}</div>`;
  input.value = "";

  try {
    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    if (!response.ok) {
      chatBox.innerHTML += `<div style="color:red;"><b>Error:</b> ${response.statusText}</div>`;
      return;
    }

    const data = await response.json();
    chatBox.innerHTML += `<div><b>Him:</b> ${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    chatBox.innerHTML += `<div style="color:red;"><b>Exception:</b> ${error.message}</div>`;
  }
}
