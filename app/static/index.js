var formEl = $('#form_id')
var locationField = $('#id_location')
var selectedLocationEchoEl = $('#selected_location_id')
var isTzAvailableEchoEl = $('#is_tz_available')


function processSelectedLocation() {
  if (typeof locationField.select2('data')[0] !== "undefined") {
    let selectedLocationId = locationField.select2('data')[0].id
    let selectedLocationTzAvailable = locationField.select2('data')[0].is_tz_available

    console.log('Selected Location:', selectedLocationId, 'TZ:', selectedLocationTzAvailable)

    selectedLocationEchoEl.html(selectedLocationId)
    if (typeof selectedLocationTzAvailable === "undefined") {
      isTzAvailableEchoEl.html('Already selected, attr is undefined, raw value: ' + selectedLocationTzAvailable)
    } else {
      isTzAvailableEchoEl.html(selectedLocationTzAvailable)
    }

  }
}


formEl.change(function () {
  console.log('change')
  processSelectedLocation()
});

formEl.ready(function () {
  console.log('ready')
  processSelectedLocation()
});
