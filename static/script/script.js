// Message Timeout
function alerts() {
  setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    if (messages) {
      messages.classList.remove('show');
    }
  }, 5000);
}

// Sidebar functions
function sidebar() {
  let sidebar = document.querySelector(".sidebar");
  let closeBtn = document.querySelector("#btn");

  closeBtn.addEventListener("click", function open() {

    sidebar.classList.toggle("open");
    if (sidebar.classList.contains('open')) {
      return true;
    } else {
      return false;
    }
  });
}

// Calendar functions
function deleteModal() {
  // Gets the delete modal working
  const modal_buttons = document.getElementById('delete-modal-buttons');
  const delete_button = document.querySelectorAll('.delete_button');

  if (delete_button.length !== 0) {
    delete_button.forEach((button) => {
      button.addEventListener('click', function () {
        const booking_id = button.getAttribute('name');
        let calbut = button.getAttribute('data-ref');
        if (calbut === '0') {
          modal_buttons.innerHTML = `
          <button type="button" class="btn btn-secondary" data-ref="0" data-bs-dismiss="modal">Close</button>
          <a href="/delete/${booking_id}" class="btn btn-back">DELETE</a>
          `;
        } else {
          modal_buttons.innerHTML = `
          <button type="button" class="btn btn-secondary" data-ref="1" data-bs-dismiss="modal">Close</button>
          <a href="/delete_calendar_booking/${booking_id}" class="btn btn-back">DELETE</a>
          `;
        }
      });
    });
  }
}

function today() {
  // Highlights today on the calendar
  const dates = document.querySelectorAll('.date');
  let d = new Date();
  let month = d.getMonth() + 1;
  let day_of_the_month = d.getDate();
  let now = `${month}_${day_of_the_month}`;
  getToday();

  function getToday() {
    dates.forEach((date) => {
      let today = date.getAttribute('name');
      if (today == now) {
        date.setAttribute('id', 'today');
      }
    });
  }
}

function calendarBookingModal() {
  // Activates the calendar booking modal
  const dates = document.querySelectorAll('.date');
  const modal = document.getElementById('myModal');
  const noBookings = document.getElementById('no-bookings-text');
  const bookingTable = document.getElementById('booking-table');

  dates.forEach((date) => {
    date.addEventListener('click', function () {
      let today = date.getAttribute('name');
      let bookings = document.querySelectorAll(`.booking_${today}`);

      if (bookings.length === 0) {
        bookingTable.classList.replace('show', 'hide');
        noBookings.classList.replace('hide', 'show');
      } else {
        noBookings.classList.replace('show', 'hide');
        bookingTable.classList.replace('hide', 'show');
        for (let a = 0; a <= bookings.length; a++) {
          bookings[a].classList.replace('hide', 'show');
          modal.addEventListener('hidden.bs.modal', function () {
            bookings[a].classList.replace('show', 'hide');

          });
        }
      }
    });
  });
}

function calendar() {
  deleteModal();
  today();
  calendarBookingModal();
}

// Map with Markers
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {
      lat: 52.3308,
      lng: 1.6851
    },
    zoom: 4.5
  });
}

function googleMapApi() {
  var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  var locations = [{
      lat: 55.9508,
      lng: -3.3615
    },
    {
      lat: 58.2139,
      lng: -6.3219
    },
    {
      lat: 57.2037,
      lng: -2.2002
    },
    {
      lat: 57.3406,
      lng: -5.6491
    },
    {
      lat: 53.8981,
      lng: -0.3660
    },
    {
      lat: 55.0372,
      lng: -8.3414
    },
    {
      lat: 50.9660,
      lng: -2.1572
    },
    {
      lat: 50.1024,
      lng: -5.6681
    },
    {
      lat: 50.9557,
      lng: 0.9335
    },
    {
      lat: 47.4072,
      lng: 8.6396
    },
    {
      lat: 52.4825,
      lng: 13.3891
    },
    {
      lat: 48.5897,
      lng: -2.0758
    },
    {
      lat: 51.9555,
      lng: 4.4399
    },
    {
      lat: 48.9812,
      lng: 6.2437
    },
    {
      lat: 48.8335,
      lng: 3.0056
    },
    {
      lat: 56.4391,
      lng: -3.3714
    },
    {
      lat: 55.6836,
      lng: -6.2483
    },
  ];

  var markers = locations.map(function (location, i) {
    return new google.maps.Marker({
      position: location,
      label: labels[i % labels.length]
    });
  });
  var markerCluster = new MarkerClusterer(map, markers, {
    imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m",
  });
}

// flatpickr
function flatpickrInit() {
  const myInput = document.querySelector("#id_date");
  const fp = flatpickr(myInput, {
    minDate: "today"
  });
}

// provides UI feedback if passwords match
function passwordMatch() {

  let password1 = document.getElementById('id_password1');
  let password2 = document.getElementById('id_password2');

  password2.addEventListener("input", function pMatch() {
    if (password2.value === password1.value) {
      password2.classList.add('matched');
      password1.classList.add('matched');
      return true;
    } else {
      password2.classList.remove('matched');
      password1.classList.remove('matched');
      return false;
    }
  });
}

// Site initialisation
let password = document.querySelectorAll('#id_password1');
let date_input = document.querySelectorAll('#id_date');
let map_div = document.querySelectorAll('#map');
let calendar_page = document.querySelectorAll('#calendar-page');

function setup() {
  alerts();
  sidebar();
  if (password.length >= 1) {
    passwordMatch();
    return 'password';
  } else if (calendar_page.length >= 1) {
    calendar();
    return 'calendar';
  } else if (date_input.length && map_div.length >= 1) {
    flatpickrInit();
    deleteModal();
    googleMapApi();
    return 'contact';
  } else if (date_input.length >= 1) {
    flatpickrInit();
    return 'bookings';
  }
}

window.addEventListener('load', () => {
    setup();
  });

module.exports = { deleteModal, sidebar, today, passwordMatch, calendar };