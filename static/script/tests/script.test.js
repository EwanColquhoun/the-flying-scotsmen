/**
 * @jest-environment jsdom
*/

const myScript = require("/workspace/the-flying-scotsmen/static/script/script.js");

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

    // test("sidebar.open should exist", () => {
    //     sidebar();
    //     expect(document.getElementById("sidebar").classList).toContain("open");
    // });


    test('resize to test the navbar exists', () => {
        // render(<Component />);
        const resizeWindow = (width, height) => {
            window.innerWidth = width
            window.innerHeight = height
            window.dispatchEvent(new Event('resize'))
          }
        resizeWindow(1200, 1200)
    
        const element = document.getElementById('navbar');
        const styles = getComputedStyle(element);
    
        expect(styles.display).toBe('block');
    })
});

describe("Calendar tests", () => {
    beforeAll(() => {
        let fs = require("fs");
        let fileContents = fs.readFileSync("templates/booking/calendar.html", "utf-8");
        document.open();
        document.write(fileContents);
        document.close();
    });
    
    test("Test today is today", () => {
        const date = document.querySelectorAll(".date")
        console.log(date.length)
        expect(date).toBe(1)
    })

    test("Test today is highlighted", () => {
            
        const element = document.getElementById('today');
        const styles = getComputedStyle(element);
    
        expect(styles.backgroundColor).toBe('#0065bd');
    })
    test("h1 should exist", () => {
        expect(document.getElementsByTagName("h1").length).toBe(1);
    });
    test("p should exist", () => {
        expect(document.getElementsByTagName("p").length).toBe(5);
    });
});