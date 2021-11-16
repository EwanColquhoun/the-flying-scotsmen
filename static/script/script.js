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
}, 3000);


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

// Only displays approved bookings on the calendar
// let dayEvents = document.querySelectorAll('.btn-events')
// console.log(dayEvents)
// dayEvents.forEach(de => {
//   console.log(de.getAttribute('data-ref'))
//   if (de.getAttribute('data-ref') == 0){
//     de.classList.add('hide')
//   } else {
//     de.classList.add('show')
//   }
// });