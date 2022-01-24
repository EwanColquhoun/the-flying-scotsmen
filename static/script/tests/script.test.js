/**
 * @jest-environment jsdom
*/

import {deleteModal, sidebar, today, passwordMatch} from "../script.js";

// below works for testing purposes


// const deleteModal = require("../script.js").default;
// const sidebar = require("../script.js").default;
// const today = require("../script.js").default;
// const passwordMatch = require("../script.js").default;

describe("Password match test", () => {
    beforeAll(() => {
        document.body.innerHTML = `
            <input type="password" name="password1" placeholder="Password" autocomplete="new-password" required id="id_password1">
            <input type="password" name="password2" placeholder="Password Again" autocomplete="new-password" required id="id_password2">`
    })

    test("Check passwords match", () => {
        let password1 = document.getElementById('id_password1')
        let password2 = document.getElementById('id_password2')
        password1.value = 'testpassword'
        password2.value = 'testpassword'
        const spy = jest.spyOn(passwordMatch, 'passwordMatch')
        passwordMatch.passwordMatch();
        expect(spy).toHaveBeenCalled();
        expect(spy).toBeTruthy()
    })
})

describe("Base.html tests", () => {

    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("templates/booking/base.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });
    
    test("sidebar should exist", () => {
        expect(document.getElementsByClassName("sidebar").length).toBe(1);
    });

    test("btn should exist", () => {
        expect(document.querySelectorAll("#btn").length).toBe(1);
    });

    test("sidebar.open should exist", () => {
        let closeBtn = document.querySelector("#btn");
        const spy = jest.spyOn(sidebar, "sidebar" );
        sidebar.sidebar()
        closeBtn.click()
        expect(document.getElementById("sidebar").classList).toContain("open");
        expect(sidebar.sidebar).toBeCalled();
        closeBtn.click()
        sidebar.sidebar()
        expect(sidebar.sidebar()).toBeFalsy();
    });
});

describe("Bookings tests", () => {
    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("templates/booking/bookings.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });

    test("booking form should exist", () => {
        expect(document.getElementById("booking-form").length).toBe(1);
    });
    test("bookings table should exist", () => {
        expect(document.getElementsByTagName("table").length).toBe(1);
    });
    test("delete booking modal not shown", () => {
        expect(document.getElementById('staticBackdrop')).toBeNull();
    })
});

describe("delete with bookings tests", ()=> {
    beforeAll(() => {
        document.body.innerHTML= `
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title scots" id="staticBackdropLabel">Delete Booking</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="delete-modal-body d-flex justify-content-center mt-4 mb-4">
                        <p><i class="fas fa-exclamation-triangle"></i> Are you sure you want to delete this booking? <i class="fas fa-exclamation-triangle"></i></p>
                    </div>
                    <div class="modal-footer" id="delete-modal-buttons">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <a aria-label="Delete" href="/delete_calendar_booking/{{ booking.id }}" class="btn btn-back delete-button">DELETE</a>
                    </div>
                </div>
            </div>
        </div>
        <tr class="booking-row approved">
            <td>08/12</td>
            <td>MAINT</td>
            <td>G-BSAI</td>
            <td class="notes"></td>
            <td>No</td>
            <td><span><a aria-label="Edit" href="/edit/2"><i class="far fa-edit edit-icon green" aria-hidden="true"></i></a></span></td>
            <td>
                <span><a aria-label="Delete" name="2" class="delete_button" data-ref="0" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
                    <i class="far fa-times-circle cancel-icon red" aria-hidden="true"></i></a>
                </span>
            </td>
        </tr>`
        })

    test("delete booking if activated should pass", () => {
    
        const spy = jest.spyOn(deleteModal, 'deleteModal')
        deleteModal.deleteModal()
        const delete_button = document.querySelectorAll('.delete_button')
        calbut = 0
        delete_button.forEach(button => {
            button.click()
        });
        expect(spy).toHaveBeenCalled();
        let modals= document.querySelectorAll('#staticBackdrop')
        expect(modals.length).toEqual(1);

    })
});

describe("calendar delete with bookings test", () => {
    beforeAll(() => {
        document.body.innerHTML= `
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title scots" id="staticBackdropLabel">Delete Booking</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="delete-modal-body d-flex justify-content-center mt-4 mb-4">
                        <p><i class="fas fa-exclamation-triangle"></i> Are you sure you want to delete this booking? <i class="fas fa-exclamation-triangle"></i></p>
                    </div>
                    <div class="modal-footer" id="delete-modal-buttons">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <a aria-label="Delete" href="/delete_calendar_booking/{{ booking.id }}" class="btn btn-back delete-button">DELETE</a>
                    </div>
                </div>
            </div>
        </div>
        <tr class="booking-row approved">
            <td>08/12</td>
            <td>MAINT</td>
            <td>G-BSAI</td>
            <td class="notes"></td>
            <td>No</td>
            <td><span><a aria-label="Edit" href="/edit/2"><i class="far fa-edit edit-icon green" aria-hidden="true"></i></a></span></td>
            <td>
                <span><a aria-label="Delete" name="2" class="delete_button" data-ref="1" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
                    <i class="far fa-times-circle cancel-icon red" aria-hidden="true"></i></a>
                </span>
            </td>
        </tr>`
        })

    test("delete calendar booking if activated should pass", () => {
    
        const spy = jest.spyOn(deleteModal, 'deleteModal')
        calbut = 1
        deleteModal.deleteModal()
        const delete_button = document.querySelectorAll('.delete_button')
        delete_button.forEach(button => {
            button.click()
        });
        expect(spy).toHaveBeenCalled();
        let modals= document.querySelectorAll('#staticBackdrop')
        expect(modals.length).toEqual(1);

    })
});

describe("calendar tests", () => {
    beforeAll(() => {
        document.body.innerHTML = `
        <table border="0" cellpadding="0" cellspacing="0" class="calendar">
            <tbody><tr><th colspan="7" class="month">January 2022</th></tr>
                <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
                <tr><td class="day-null day"></td><td class="day-null day"></td>
                    <td class="day-null day"></td><td class="day-null day"></td>
                    <td class="day-null day"></td><td class="day-medium"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_1">1</a>
                        <ul class="booking_list"> <li class="event"> <span class="btn-events aircraft-purple calendar-events" data-ref="1" name="1_1">MAINT | admin2021 | <i class="fas fa-check" aria-hidden="true"></i></span> </li> </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_2">2</a>
                        <ul class="booking_list">  </ul></td> 
                </tr>
                <tr><td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_3">3</a>
                    <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_4">4</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_5">5</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-medium"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_6">6</a>
                        <ul class="booking_list"> <li class="event"> <span class="btn-events calendar-events purple-trans" data-ref="0" name="1_6">1100-1300 | admin2021 | <i class="fas fa-user-cog" aria-hidden="true"></i></span> </li> </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_7">7</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_8">8</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_9">9</a>
                        <ul class="booking_list">  </ul></td>
                </tr>
                <tr><td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_10">10</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_11">11</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-medium"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_12">12</a>
                        <ul class="booking_list"> <li class="event"> <span class="btn-events calendar-events purple-trans" data-ref="0" name="1_12">0900-1100 | admin2021 | <i class="fas fa-user-cog" aria-hidden="true"></i></span> </li><li class="event"> <span class="btn-events calendar-events purple-trans" data-ref="0" name="1_12">1500-1700 | admin2021 | <i class="fas fa-user-cog" aria-hidden="true"></i></span> </li> </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_13" id="today">13</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_14">14</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_15">15</a>
                        <ul class="booking_list">  </ul></td>
                    <td class="day-free"><a class="btn date" data-bs-toggle="modal" data-bs-target="#myModal" name="1_16">16</a>
                        <ul class="booking_list">  </ul></td> 
                </tr>
            </tbody>
        </table>`
    });

    test("calendar should highlight today", () => {
        const spy = jest.spyOn(today, 'today')
        let d = 'Thu Jan 13 2022 11:42:12 GMT+0000 (Greenwich Mean Time)'
        const dates = document.querySelectorAll('.date');
        const present = document.querySelectorAll('#today')
        today.today()
        expect(spy).toHaveBeenCalled();
        expect(present.length).toEqual(1);
    });
})


describe("Contact tests", () => {
    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("templates/booking/contact.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });

    test("contact form should exist", () => {
        expect(document.getElementById("contact-form").length).toBe(1);
    });
    test("email has correct path", () => {
        let email = document.getElementById("email-text")
        let attr = email.getAttribute('href')
        expect(attr).toEqual("mailto:theflyingscotsmen.booking@gmail.com");
    });
});