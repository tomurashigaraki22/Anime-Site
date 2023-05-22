function signup() {
    $.ajax({
        url: "/signups",
        method: "POST",
        success: function(response) {
            console.log(response);
            // Handle the response from the Python function
        },
        error: function(xhr, status, error) {
            console.log(error);
            // Handle errors
        }
    });
}