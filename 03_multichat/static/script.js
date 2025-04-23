const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chat = document.getElementById('chat');
const nums = [];

input.focus();

input.addEventListener('keydown', async (e) => {
  if (e.key === 'Enter') {
    e.preventDefault();
    const val = input.value.trim();
    if (!val) return;
    nums.push(Number(val));
    chat.innerHTML += `<div>User: ${val}</div>`;
    input.value = '';
    input.focus();

    if (nums.length === 3) {
      chat.innerHTML += `<div>Bot: Thinking...</div>`;
      const res = await fetch('/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nums })
      });
      const data = await res.json();
      chat.innerHTML += `<div>Bot: ${data.result}</div>`;
      nums.length = 0;
      input.focus();
    }
  }
});
