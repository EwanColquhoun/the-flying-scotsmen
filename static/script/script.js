// Sidebar

let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");


  closeBtn.addEventListener("click", ()=>{
    sidebar.classList.toggle("open");
    menuBtnChange();//calling the function(optional)
  });

  // following are the code to change sidebar button(optional)
  function menuBtnChange() {
   if(sidebar.classList.contains("open")){
     closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
   }else {
     closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the iocns class
   }
  }

  // Messages 
  setTimeout(function() {
    let messages = document.getElementById('msg')
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);


// Gets the delete modal working
const modal_buttons = document.getElementById('delete-modal-buttons')
const delete_button = document.querySelectorAll('.delete_button')

if (delete_button.length !== 0){
  // console.log('delete_button not 0')
  delete_button.forEach((button) => {
    button.addEventListener('click', function() {
      const booking_id = button.getAttribute('name')
      modal_buttons.innerHTML = `
      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      <a href="/delete/${booking_id}" class="btn btn-back">DELETE</a>
      `
    });
  })
}

// Highlights today on the calendar
const dates = document.querySelectorAll('.date')
d = new Date();
month = d.getMonth() + 1
day_of_the_month = d.getDate()
now = `${month}_${day_of_the_month}`

window.onload = function() {
  dates.forEach((date) => {
    let today = date.getAttribute('name');
    // console.log(today, 't/n', now)
    if (today == now){
      date.setAttribute('id', 'today')
    }
  })
}


// Activates the calendar booking modal
let modalBody = document.querySelector('.modal-body')
let dayBookings = document.querySelectorAll('.calendar-events');
const modal = document.getElementById('myModal')
const noBookings = document.getElementById('no-bookings-text') 
const bookingTable = document.getElementById('booking-table')

dates.forEach((date) => {
  date.addEventListener('click', function() {
    let today = date.getAttribute('name');
    let bookings = document.querySelectorAll(`.booking_${today}`)

    if (bookings.length === 0 ){
      bookingTable.classList.replace('show', 'hide')
      noBookings.classList.replace('hide', 'show')
    } else {
      noBookings.classList.replace('show', 'hide')
      bookingTable.classList.replace('hide', 'show')
      for (let a = 0; a <= bookings.length; a++){
        bookings[a].classList.replace('hide', 'show')
        modal.addEventListener('hidden.bs.modal', function () {
          bookings[a].classList.replace('show', 'hide')
              
            });
          } 
    }
  }); 
});

// GoogleMaps API

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 52.3308, lng: 1.6851},
    zoom: 4.5
  });

  var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  var locations = [
    { lat: 55.9508, lng: -3.3615},
    { lat: 58.2139, lng: -6.3219},
    { lat: 57.2037, lng: -2.2002},
    { lat: 57.3406, lng: -5.6491},
    { lat: 53.8981, lng: -0.3660},
    { lat: 55.0372, lng: -8.3414},
    { lat: 50.9660, lng: -2.1572},
    { lat: 50.1024, lng: -5.6681},
    { lat: 50.9557, lng: 0.9335},
    { lat: 47.4072, lng: 8.6396},
    { lat: 52.4825, lng: 13.3891},
    { lat: 48.5897, lng: -2.0758},
    { lat: 51.9555, lng: 4.4399},
    { lat: 48.9812, lng: 6.2437},
    { lat: 48.8335, lng: 3.0056},
    { lat: 56.4391, lng: -3.3714},
    { lat: 55.6836, lng: -6.2483},
  ]

  var markers = locations.map(function(location, i) {
    return new google.maps.Marker({
      position: location,
      label: labels[i % labels.length]
    });
  });

  var markerCluster = new MarkerClusterer(map, markers, {
    imagePath:
    "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
});
}


// lets the date to the future
// let date = document.getElementById('id_date')
// console.log(date)
// var today = new Date();
// var dd = String(today.getDate()).padStart(2, '0');
// var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
// var yyyy = today.getFullYear();

// today = yyyy + '/' + mm + '/' + dd;
// console.log(today)
// att = document.createAttribute('min')
// att.value = today
// date.setAttributeNode(att)

// flatpickr
const myInput = document.querySelector("#id_date");
const fp = flatpickr(myInput, {
  minDate: "today"
});  // flatpickr