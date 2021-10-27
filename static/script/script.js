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

// Bootstrap alert

// var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
// var alertTrigger = document.getElementById('new_booking')

// function alert(message, type) {
//   var wrapper = document.createElement('div')
//   wrapper.innerHTML = '<div class="alert alert-' + type + ' alert-dismissible" role="alert">' + message + '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'

//   alertPlaceholder.append(wrapper)
// }

// if (alertTrigger) {
//   alertTrigger.addEventListener('click', function () {
//     alert('This is a double booking, please check your date/slot/aircraft and try again.', 'warning')
//   })
// }

// const dates = document.querySelectorAll('.date')

// dates.forEach((date) => {
//   date.addEventListener("click", function(e){
//     let bookingDisplay = document.getElementById('booking-display');
//     console.log('click', e)

//     if (bookingDisplay.classList.contains('hide')) {
//       bookingDisplay.classList.replace('hide', 'show');
//     } else {
//       bookingDisplay.classList.replace('show', 'hide')
//     }
//   });
// });


const dates = document.querySelectorAll('.date')
let modalBody = document.querySelector('.modal-body')
let dayBookings = document.querySelectorAll('.calendar-events');
const modal = document.getElementById('myModal')
const noBookings = document.getElementById('no-bookings-text') 
const bookingTable = document.getElementById('booking-table')

dates.forEach((date) => {
  date.addEventListener('click', function() {
    let today = date.getAttribute('name');
    console.log(today,'= today'); 
    let bookings = document.querySelectorAll(`.booking_${today}`)

    console.log(bookings, 'bookings')
    if (bookings.length === 0 ){
      bookingTable.classList.replace('show', 'hide')
      noBookings.classList.replace('hide', 'show')
    } else {
      noBookings.classList.replace('show', 'hide')
      bookingTable.classList.replace('hide', 'show')
      for (let a = 0; a <= bookings.length; a++){
          console.log(bookings[a], 'bookings[i]')
          num = ''
          num += today
          console.log(num, '/', today)
          if (num !== today && bookings[a].classList.contains('show')){
            bookings[a].classList.replace('show', 'hide')
            // console.log('booking hide2')
          } else {
            bookings[a].classList.replace('hide', 'show')
            // console.log('booking show');
            modal.addEventListener('hidden.bs.modal', function () {
              bookings[a].classList.replace('show', 'hide')
              // console.log('modal to close booking')
            });
          }  
      }
    }
  }); 
});

function modalBookingContent(){
  return modalBody.innerHTML = ` <div class="d-grid gap-3">
  <table>

{% if bookings %}

      <tr class="table-headings">
          <td>Date</td>
          <td>Slot</td>
          <td>Aircraft</td>
          <td>day</td>    
          <td>Edit | Cancel</td>    
      </tr>
{% endif %}

{% for booking in bookings %} 
          <tr class="booking-row hide booking_{{booking.date.day}}">
              <td>{{ booking.date }}</td>
              <td>{{ booking.slot.slot }}</td>
              <td>{{ booking.aircraft }}</td>
              <td>{{ booking.notes }}</td>
              <td><span><a href="/edit/{{ booking.id }}"><i class="far fa-edit edit-icon green"></i></a></span>
                  <span><a href="/delete/{{ booking.id }}"><i class="far fa-times-circle cancel-icon red"></i></a></span>
              </td>
          </tr>
{% empty %}

      <span>Your bookings will appear here once approved by admin.</span> 

{% endfor %}
  </table>
</div>`
}

function modalEmpty(){
 return modalBody.innerHTML = `<div>There are no bookings for the selected day</div>`
}