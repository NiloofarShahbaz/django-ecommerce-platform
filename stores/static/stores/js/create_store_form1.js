$(document).ready(function () {
    $('#id_name').change(function () {
        var store_name = $(this).val();
        console.log(store_name);
        $.ajax({
            url: 'validate_name/',
            data: {
                'store_name': store_name
            },
            dataType: 'json',
            success: function (data) {
                if (data.is_taken) {
                    console.log(data.error_message);
                    $('#id_name').addClass('border-danger').after('<small id="error-msg" class="text-danger">' + data.error_message + '</small>')
                }
                else {
                    $('#id_name').removeClass('border-danger').addClass('border-success').after('<i class="far fa-2x text-success fa-check-circle position-relative icon"></i>');
                    $('#error-msg').remove();
                }
            }

        });
    });
});

