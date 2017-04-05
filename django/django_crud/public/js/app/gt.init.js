/**
 * Created by touhid on 30/08/2015.
 */

jQuery(document).ready(function(){
    jQuery(".apply-chosen").chosen();
    jQuery(".open-confirm-box").click(function (event) {
        var url = $(this).attr("wizard-url"),
            title = $(this).attr("wizard-title");
        GT.wizard.confirm(title, url);
        event.preventDefault();
    });

    var object = jQuery(".auto-complete-input"),
        url = GT.baseURL + object.attr("url");
    object.autocomplete({
        source: url,
        minLength: 1,
        select: function( event, ui ) {
            var form = object.closest(".auto-submit-form")
            if(form !== undefined){
                form.find(".id-add-input").val(ui.item.id)
            }
        }
    });

    function updateQueryStringParameter(uri, key, value) {
        var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
        var separator = uri.indexOf('?') !== -1 ? "&" : "?";
        if (uri.match(re)) {
            return uri.replace(re, '$1' + key + "=" + value + '$2');
        }
        else {
            return uri + separator + key + "=" + value;
        }
    }

    jQuery(".item-per-page-changed").change(function () {
        var url = window.location.href;
        window.location.href = updateQueryStringParameter(url, "limit", $(this).val())
    });

    var searchArea = jQuery("#search-area");
    searchArea.find(".selected-column-name li").click(function(e){
        e.preventDefault();
        var _this = $(this);
        searchArea.find(".selected-column-label").text(_this.text());
        searchArea.find(".selected-column-name").val(_this.attr('data'));
    });

    var selected = searchArea.find(".selected-column-name");
    if(selected.attr("selected-data") !== ""){
        var colAttr = "li[data='" + selected.attr("selected-data") + "']",
            colName = selected.find(colAttr).text();
        if(colName !== undefined){
            searchArea.find(".selected-column-label").text(colName);
        }
    }
    searchArea.find(".selected-column-name").val(selected.attr("selected-data"));
    jQuery('.datepicker').datepicker({
        dateFormat: 'dd-mm-yy'
    });

});
