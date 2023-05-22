function login() {
    $.ajax({
        url: "/login",
        method: "POST",
        data: $("form").serialize(),  // Serialize the form data
        
        success: function (data) {
            if (data.status == "success") {
                alert(data.message)
                window.location.href = '../index.html'
            }
            else {
                alert(data.message)
            }
        }
        
        
        
    });
}
