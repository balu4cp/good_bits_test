(function (window) {
  GBL = {};
  
  GBL.showLoading = function() {
    $(".spinner-border").removeClass("d-none");
    $(".d-none").removeClass("active");
    $("body").find("*").attr("disabled", "disabled");
    $("body").find("a").click(function (e) { e.preventDefault(); });
  };

  GBL.hideLoading = function() {
    $(".spinner-border").addClass("d-none");
    $(".d-none").addClass("active");
    $("body").find("*").removeAttr("disabled");
    $("body").find("a").unbind("click");  
  };

  GBL.errorMsg = function (jqXHR) {
    jsonValue = jQuery.parseJSON(jqXHR.responseText);
    var errormessage = "";
    for (index = 0; index < jsonValue.errors.length; index++) {
      errormessage = errormessage + jsonValue.errors[index].message + "<br>";
    }
    alertify.error(errormessage);
  };

  GBL.getCookie = function(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  })(this);