/**
 * @jest-environment jsdom
*/

const start = require("/workspace/the-flying-scotsmen/static/script/script.js");
const setup = require("/workspace/the-flying-scotsmen/static/script/script.js");
const deleteModal = require("/workspace/the-flying-scotsmen/static/script/script.js");
const sidebar = require("/workspace/the-flying-scotsmen/static/script/script.js");

// wanted this to show that when the passwords matched either true or false is returned from the function----------------------------------

// describe("Password match test", () => {
//     beforeAll(() => {
//         document.body.innerHTML = `<input type="password" name="password1" placeholder="Password" autocomplete="new-password" required="" id="id_password1">
//         <input type="password" name="password2" placeholder="Password Again" autocomplete="new-password" required="" id="id_password2">`
//     })

//     test("Check passwords match", () => {
//         // let password1 = document.getElementById('id_password1')
//         // let password2 = document.getElementById('id_password2')
//         // password1.value = 'testpassword'
//         // password2.value = 'testpassword'
//         // const spy = jest.spyOn(start, 'passwordMatch')
//         // const match = start.passwordMatch();
       
//         // expect(spy).toHaveBeenCalled();
//         // expect(match).toBe(true)
//     })
// })


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

// wanted these to show that the button opens the sidebar ---------------------
    test("sidebar.open should exist", () => {
        let closeBtn = document.querySelector("#btn");
        const spy = jest.spyOn(sidebar, "sidebar" );
        // const side = setup.sidebar();
        // const addEvt = new Event('click');
        // document.dispatchEvent(addEvt);
        sidebar.sidebar()
        closeBtn.click()
        expect(document.getElementById("sidebar").classList).toContain("open");
        expect(sidebar.sidebar).toBeCalled();
        closeBtn.click()
        sidebar.sidebar()
        expect(sidebar.sidebar()).toBeFalsy();
    });
});

// these all pass but dont test the js..----------------------
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
        // expect(deleteModal.deleteModal).toBeCalled();
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
        // expect(deleteModal.deleteModal).toBeCalled();
        let modals= document.querySelectorAll('#staticBackdrop')
        expect(modals.length).toEqual(1);

    })
});

// all pass but again dont really the js..-----------------------------
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