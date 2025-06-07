chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "explain-code",
    title: "Explain Code",
    contexts: ["selection"]
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "explain-code") {
    chrome.tabs.sendMessage(tab.id, {
      action: "explain-code",
      selectedText: info.selectionText
    });
  }
});
