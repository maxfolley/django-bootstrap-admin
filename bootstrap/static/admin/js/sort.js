$(function() {
    var model = window.location.pathname.match(/([^\/]+)\/$/)[1],
        $sortedItem = $(".sortable tbody");
    
    $.csrftoken();

    $sortedItem.sortable({
        axis: "y",
        handle: ".handle",
        items: "tr",
        helper: function(event, ui) {
            ui.children().each(function() {
                $(this).width($(this).width());
            });
            return ui;
        },
        update: function(event, ui) {
            var indices = [];
            $("tr", $sortedItem).each(function() {
                indices.push(parseInt($("a", this).first().attr("href").replace(/\/$/, ""), 10));
            });
            submitOrder(indices);
        }
    });

    function onError(data) {
        $("#messages").append("<div class='alert alert-error'><button type='button' class='close' data-dismiss='alert'>×</button><i class='icon-warning-sign'></i> " + model.replace(/(^\w)/, function (i) { return i.toUpperCase(); }) + " order failed to updated. If problem persists contact your system administrator.</div>");
    }

    function onSuccess(data) {
        $("#messages").append("<div class='alert alert-success'><button type='button' class='close' data-dismiss='alert'>×</button><i class='icon-thumbs-up'></i> " + model.replace(/(^\w)/, function (i) { return i.toUpperCase(); }) + " order updated.</div>");
    }

    function submitOrder(indices) {
        $.post('/admin/' + model + '/update_order/', {indices: indices.join(",")})
            .error(onError)
            .success(onSuccess);
    }
});
