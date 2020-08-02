(function (window) {

    jQuery.validator.addMethod("firstSPace", function(value, element) {
    return this.optional(element) || /^[a-z,0-9]/i.test(value);
  }, "First space is not allowed");


    var userLoginValidator = $("#createInvoice").validate({
    ignore: [],
    errorElement: 'small',
    errorClass: 'error text-danger',
    errorPlacement: function (error, element) {
      if (element.parent().hasClass("input-group")) {
        error.appendTo(element.parent().parent());
      } else {
        error.appendTo(element.parent());
      }
    },
    rules: {
      name: {
        required: true,
        firstSPace:true,
      },
      project: {
        required: true,
        firstSPace:true,
      },
      email: {
        required: true,
      },
      amount: {
        required:true,
        number: true,
      },
    },
    messages: {
      name: {
        required: "Please enter a name"
      },
      project: {
        required: "Please enter a project name",
      },
      department: {
        required: "Please enter a department"
      },
      email: {
        required: "Please enter a email id"
      },
      amount: {
        required: "Please enter a amount"
      }
    },
    submitHandler: function() {
     GBL.createInvoice();
    }
  });

  GBL.name = ko.observable('');
  GBL.project = ko.observable('');
  GBL.email = ko.observable('');
  GBL.amount = ko.observable('');

  GBL.createInvoice = function(){
    var csrftoken = GBL.getCookie('csrftoken');
    var formdata = new FormData();
    formdata.append('name', GBL.name());
    formdata.append('project', GBL.project());
    formdata.append('email', GBL.email());
    formdata.append('amount', GBL.amount());
    $.ajax({
      method: 'POST',
      url: '/api/invoice/create',
      data: formdata,
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
      GBL.showLoading();
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      alert(d)
      location.href='/invoices'
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText)
    })
    .always(function(){
      GBL.hideLoading();
    });
  };

})(this);

function init() {
  if (document.readyState == "interactive") {
    GBL.hideLoading();
    ko.applyBindings(GBL);
  }
}
document.onreadystatechange = init;