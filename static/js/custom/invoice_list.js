(function (window) {

  GBL.invoice_list = ko.observableArray([]);

  GBL.getInvoiceList = function(){
    var csrftoken = GBL.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/api/invoice/list/get',
      contentType: false,
      processData: false,
      beforeSend: function(xhr, settings) {
      GBL.showLoading();
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done( function (d, textStatus, jqXHR) {
      // console.log(d)
      GBL.invoice_list([])
      GBL.invoice_list(d)
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText)
    }).always(function(){
      GBL.hideLoading();
    });
  };


  GBL.redirectToCreatePage = function()
  {
    location.href='/create'
  }

  GBL.sendEmail = function (data) {
    var csrftoken = GBL.getCookie('csrftoken');
    $.ajax({
      method: 'GET',
      url: '/api/invoice/paylink/email',
      data:{'invoice_number': data.invoice_number},
      dataType: 'json',
      beforeSend: function(xhr, settings) {
      GBL.showLoading();
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    .done(function (d, textStatus, jqXHR) {
      alert(d)
    })
    .fail( function (jqXHR, textStatus, errorThrown) {
      alert(jqXHR.responseText)
    }).always(function(){
      GBL.hideLoading();
    });
  };

})(this);

function init() {
  if (document.readyState == "interactive") {
     GBL.getInvoiceList();
    ko.applyBindings(GBL);
  }
}
document.onreadystatechange = init;