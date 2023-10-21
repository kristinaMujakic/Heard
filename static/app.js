$(document).ready(function() {
    const $userInput = $('#userInput');
    const $submitForm = $("#submit-form");
    const $sendBtn = $("#send");
    const $chatBox = $('#chatBox');

    function submitMessage(e) {
        e.preventDefault();

        const message = $userInput.val().trim();
        if (message === '') return;

        console.log(message);
    }

    $submitForm.on('click', submitMessage);

    function sendSubmission(e) {
        const userMessage = $userInput.val().trim();
        const chatMessageHTML = `
            <div class="d-flex flex-row justify-content-start mb-4">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava3-bg.webp" alt="avatar" style="width: 45px; height: 100%;">
                <div>
                    <p class="small p-2 ms-3 mb-1 rounded-3" style="background-color: #f5f6f7;">
                        ${userMessage}
                    </p>
                </div>
            </div>
        `;
        $chatBox.append(chatMessageHTML);
        $userInput.val('');
        return userMessage
    }

    async function getResponse(userMessage) {
        const response = await axios.post(
            "/send", { "user_submission" : userMessage })
        const chatMessageHTML = `
            <div class="d-flex flex-row justify-content-end">
                <div>
                    <p class="small p-2 me-3 mb-1 text-white rounded-3 bg-primary">
                        ${response.data.message.content}
                    </p>
                </div>
                <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava4-bg.webp"
                    alt="avatar 1" style="width: 45px; height: 100%;">
            </div>
        `;
        $chatBox.append(chatMessageHTML);
        console.log(response)
    }


    $sendBtn.on('click', function() {
        const userMessage = sendSubmission()
        getResponse(userMessage)
    });
});