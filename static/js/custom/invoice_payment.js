(function (window) {
GBL.amount= ko.observable('');
GBL.invoice_number= ko.observable('');

})(this);

function init() {
if (document.readyState == "interactive") {
  var docUrlArr = document.URL.split('/');
  var invoice_number = docUrlArr[docUrlArr.length - 1];
  GBL.invoice_number(invoice_number);
  GBL.hideLoading();
  ko.applyBindings(GBL);
}
}
document.onreadystatechange = init;