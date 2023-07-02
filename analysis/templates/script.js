const chatHistoryElement = document.getElementById("chat-history");
const userInputElement = document.getElementById("user-input");

// Replace 'YOUR_API_KEY' with your actual API key from OpenAI
const apiKey = "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";

async function sendMessage() {
    const userMessage = userInputElement.value;
    if (!userMessage.trim()) return;

    appendMessage(userMessage, "user");

    // Make the API call to ChatGPT
    try {
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo",
                messages: [
                    {
                        role: "system",
                        content: "You are a chatbot."
                    },
                    {
                        role: "user",
                        content: userMessage
                    }
                ]
            })
        });

        const data = await response.json();

        if (data.choices && data.choices.length > 0) {
            const botMessage = data.choices[0].message.content;
            appendMessage(botMessage, "bot");
        }
    } catch (error) {
        console.error("Error fetching from ChatGPT API:", error);
    }

    userInputElement.value = "";
}

function appendMessage(message, role) {
    const messageElement = document.createElement("div");
    messageElement.classList.add(role === "user" ? "user-message" : "bot-message");
    messageElement.textContent = message;
    chatHistoryElement.appendChild(messageElement);
    chatHistoryElement.scrollTop = chatHistoryElement.scrollHeight;
}


userInputElement.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
