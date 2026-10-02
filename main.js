let mode = "chat";
const input = document.getElementById("input");
const output = document.getElementById("output");

const bodyFor = {
  chat: (v) => ({ question: v }),
  explain: (v) => ({ topic: v, level: "Beginner" }),
  quiz: (v) => ({ topic: v, count: 5 }),
  summarize: (v) => ({ notes: v }),
};

document.querySelectorAll(".tab").forEach((btn) => {
  btn.addEventListener("click", () => {
    document.querySelector(".tab.active").classList.remove("active");
    btn.classList.add("active");
    mode = btn.dataset.mode;
  });
});

document.getElementById("submit").addEventListener("click", async () => {
  output.textContent = "Thinking...";
  try {
    const res = await fetch("/api/" + mode, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(bodyFor[mode](input.value)),
    });
    const data = await res.json();
    output.textContent = data.result || data.error;
  } catch (e) {
    output.textContent = "Error: " + e.message;
  }
});
