const input = document.getElementById('user-input');
const chat = document.getElementById('chat');

input.focus();

input.addEventListener('keydown', async (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    const val = input.value.trim();
    if (!val) return;

    chat.innerHTML += `<div>User: ${val}</div>`;
    input.value = '';
    chat.innerHTML += `<div>${BOT_NAME}: ...</div>`;
    chat.scrollTop = chat.scrollHeight;

    const res = await fetch('/coach', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_input: val })
    });

    const data = await res.json();
    chat.innerHTML += `<div>${BOT_NAME}: ${data.result}</div>`;
    input.focus();
    chat.scrollTop = chat.scrollHeight;
  }
});
