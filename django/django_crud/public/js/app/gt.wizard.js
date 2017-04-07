/**
 * Created by touhid on 15/09/2015.
 */
GT.wizard = (function () {

    var wizard = "", confirmBox = "";
    return {
        confirm: function (title, url) {
            var wizardCount = jQuery(".mis-wizard").length,
                html = "<div class='mis-wizard' id='mis-wizard-" + wizardCount + "'></div>";
            jQuery(document.body).append(html);
            confirmBox = jQuery("#mis-wizard-" + wizardCount);
            var bottomLine = '<div class="form-button-line"><button class="btn btn-danger wizard-close" type="button">Cancel</button><button class="btn btn-success delete-item" name="submit" type="button">Delete</button></div>';
            confirmBox.html("<div class='confirm-box'><h4 class='text-center'>Are You Sure Want to Delete?</h4>" + bottomLine +"</div>").dialog({
                modal: true,
                title: title,
                width: 300,
                close: function (event, ui) {
                    confirmBox.dialog("destroy");
                    confirmBox.remove();
                }
            }).dialog("open");
            confirmBox.find(".delete-item").on("click", function () {
                var _url = GT.baseURL + url;
                window.location.assign(_url);
            });

            confirmBox.find(".wizard-close").click(function () {
                confirmBox.dialog("close");
            });
        }
    }


}());