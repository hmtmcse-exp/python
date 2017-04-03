GT.messageBox =  (function () {
    var messageHtml = '<div class="alert"><span class="message"></span></div>',
        timeOut = null;
    function hideMessage() {
        $(".alert").slideUp();
        timeOut = null;
    }
    function checkTimeOut() {
        if(timeOut !== null) {
            clearTimeout(timeOut);
        }
    }

    return {
        showMessage: function(success, message) {


            console.log("------------------ success -------------------------" + success);
            if(!jQuery(".alert").length) {
                jQuery(document.body).append(messageHtml);
            }
            var messageType = "alert-success"
            if(success !== true){
                messageType = "alert-danger"
                console.log("-------------------------------------------")
            }

            checkTimeOut();
            var messageElement = $(document.body).find(".alert");
            messageElement.find(".message").text(message);
            messageElement.removeClass("alert-success").removeClass("alert-danger").addClass(messageType);
            messageElement.slideDown();
            timeOut = setTimeout(function() {
                hideMessage();
            }, 5000);
        }
    }
}());