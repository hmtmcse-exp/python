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
        showMessageByString:function (status, message) {
            if (status === "success"){
               GT.messageBox.showMessage(true, message)
            }else{
              GT.messageBox.showMessage(false, message)
            }
        },
        showMessage: function(success, message) {
            if(!jQuery(".alert").length) {
                jQuery(document.body).append(messageHtml);
            }
            var messageType = "alert-success"
            if(success !== true){
                messageType = "alert-danger"
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