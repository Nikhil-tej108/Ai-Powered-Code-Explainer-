document.getElementById("explain").addEventListener("click", () => {
  const code = document.getElementById("code").value;

  fetch("http://127.0.0.1:5000/explain", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code, api: "groq" })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("result").innerText =
        data.success ? data.explanation : `Error: ${data.error}`;
    });
});
