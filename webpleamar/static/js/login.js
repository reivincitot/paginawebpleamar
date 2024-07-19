// login.js
$(document).ready(function () {
    $('#login-form').on('submit', function (event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: "{% url 'login' %}",
            data: formData,
            success: function (response) {
                window.location.href = "{% url 'home' %}";
            },
            error: function (response) {
                $('#error-message').html('Nombre de usuario o contraseña incorrectos.').show();
            }
        });
    });
});

































