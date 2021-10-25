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
let dayBookings = document.querySelectorAll('.calendar-events');
let modalBody = document.querySelector('.modal-body')

dates.forEach((date) => {
  date.addEventListener('click', function() {
    let today = date.getAttribute('name'); //gets the number of the date from the buttons

   dayBookings.forEach((day) => {
      let now = day.getAttribute('name') // gets the number from the event
      if (now === today){
        modalBody.innerHTML += `<div><p>You have bookings for today!</p></div>`

      } else {
        modalBody.innerHTML += `<div><p>You have no bookings for today!</p></div>`
      };
   });
});
});
