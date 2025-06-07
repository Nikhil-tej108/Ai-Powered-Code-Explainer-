chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "explain-code") {
    const selectedCode = request.selectedText;

    fetch("http://127.0.0.1:5000/explain", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        code: selectedCode,
        api: "groq"  // or "openrouter"
      })
    })
    .then(res => res.json())
    .then(data => {
      alert(data.success ? data.explanation : "Error: " + data.error);
    })
    .catch(err => alert("Request failed: " + err.message));
  }
});
