const $body = $('body');
const $loginForm = $("#login-form");
const $userInput = $('#user-input');
const $submitForm = $("#submit-form");
const $sendsubmission = $("#send");

function submitMessage(e) {
    e.preventDefault();

    const message = $userInput.val().trim();
    if (message === '') return;

    console.log(message);
}

$submitForm.on('click', submitMessage);

