const input = document.getElementById('user-input');
const chat = document.getElementById('chat');

input.focus();

input.addEventListener('keydown', async (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    const val = input.value.trim();
    if (!val) return;

    chat.innerHTML += `<div class="msg user-msg">${val}</div>`;
    input.value = '';
    chat.innerHTML += `<div class="msg bot-msg typing">${BOT_NAME} is typing...</div>`;
    chat.scrollTop = chat.scrollHeight;

    const res = await fetch('/coach', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_input: val })
    });

    const data = await res.json();
    
    // Replace the typing message with the actual response
    const typingMsg = chat.querySelector('.typing');
    if (typingMsg) {
      chat.removeChild(typingMsg);
    }
    
    // Format the response by replacing newlines with <br> tags
    const formattedResponse = data.result.replace(/\n/g, '<br>');
    chat.innerHTML += `<div class="msg bot-msg">${formattedResponse}</div>`;
    
    input.focus();
    chat.scrollTop = chat.scrollHeight;
  }
});

// Function to handle button click
function handleInput() {
  const val = input.value.trim();
  if (!val) return;
  
  // Trigger the Enter key event handler
  const event = new KeyboardEvent('keydown', {
    key: 'Enter',
    code: 'Enter',
    keyCode: 13,
    which: 13,
    bubbles: true
  });
  input.dispatchEvent(event);
}
