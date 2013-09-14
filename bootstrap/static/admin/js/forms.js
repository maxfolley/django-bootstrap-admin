(function() {
    var methods = {
        init: function(options) {
            return this.each(function() {
                var $this = $(this),
                    $btn = $("button", this), 
                    $text = $(":text", this),
                    $file = $(":file", this);
                $file.on("change", function(e) {
                    $text.val($file.val().match(/([^\\]+$)/)[0]);
                });
                $file.mouseenter(function() {
                    $btn.addClass("hover");
                }).mouseleave(function() {
                    $btn.removeClass("hover");
                });
            });
        }
    };

    $.fn.prettyUpload = function(method) {
        if (methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof method === "object" || !method) {
            return methods.init.apply(this, arguments);
        } else {
            $.error('Method ' + method + ' does not exist on jQuery.fluidtext');
        }
    }
}(jQuery));

$(function () {
    $(".pretty-file-input").prettyUpload();
    $chznSelects = $('.chosen');
    $chznSelects.chosen();
    $chznSelects.change(function (e) {
        console.log("CHANGE!", e);
    });

    if ($("#wysihtml5-textarea").length) {
        var editor = new wysihtml5.Editor("wysihtml5-textarea", {
            toolbar: "wysihtml5-toolbar",
            parserRules: wysihtml5ParserRules 
        });
    }
});

function finishAddPopup(win, newId, newRepr) {
    dismissAddAnotherPopup(win, newId, newRepr);
    $('.chosen').trigger("liszt:updated");
    /*
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem) {
        var elemName = elem.nodeName.toUpperCase();
        if (elemName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
        } else if (elemName == 'INPUT') {
            if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                elem.value += ',' + newId;
            } else {
                elem.value = newId;
            }
        }
    } else {
        var toId = name + "_to";
        elem = document.getElementById(toId);
        var o = new Option(newRepr, newId);
        SelectBox.add_to_cache(toId, o);
        SelectBox.redisplay(toId);
    }
    win.close();
    */
}
