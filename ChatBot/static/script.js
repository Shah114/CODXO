// Function to convert markdown-like text to HTML
function formatMarkdown(text) {
    let formattedText = text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>') // Bold
        .replace(/\*(.*?)\*/g, '<em>$1</em>')             // Italic
        .replace(/\n/g, '<br>');                          // New line -> break line
    return formattedText;
}

// Function to append chat messages to the chat box
function appendMessage(role, text) {
    let messageDiv = document.createElement('div');
    messageDiv.classList.add(role);

    // Apply markdown formatting to the response text
    messageDiv.innerHTML = formatMarkdown(text);

    // Add the copy button only for assistant messages
    if (role === 'assistant') {
        const copyButton = document.createElement('button');
        copyButton.textContent = 'Copy';
        copyButton.classList.add('copy-btn');
        
        // Set the copy function to run when the button is clicked
        copyButton.onclick = function() {
            copyToClipboard(text);
        };
        
        messageDiv.appendChild(copyButton);
    }

    document.getElementById('chat-box').appendChild(messageDiv);

    // Scroll chat to the latest message
    document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;
}

// Function to copy bot's message to clipboard
function copyToClipboard(text) {
    const tempTextArea = document.createElement('textarea');
    tempTextArea.value = text;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand('copy');
    document.body.removeChild(tempTextArea);
    alert('Copied to clipboard!');
}

// Submit form and send the user's message to the server
$('#chat-form').submit(function(event) {
    event.preventDefault();

    const userInput = $('#user-input').val();
    appendMessage('user', userInput);

    // Send user input to the Flask server
    $.post('/get_response', { user_input: userInput }, function(data) {
        $('#user-input').val(''); // Clear the input field

        // Append chat history with formatted messages
        for (let message of data) {
            appendMessage(message.role, message.text);
        }
    });
});