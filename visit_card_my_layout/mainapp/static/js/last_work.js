function on_check(event) {
    works($(event).prop('checked'));
}

function works(slice) {
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: '/works/',
        type: 'POST',
        data: {'slice': slice?'2':''},
        dataType: 'json',

        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);

        },

        success: function (response) {
            $('#place_works').html(response.html);
        },

        error: function (xhr, status, error) {
            console.log('error: ', error)
        }
    })
}