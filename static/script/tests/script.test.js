/**
 * @jest-environment jsdom
 */

const script = require("/workspace/the-flying-scotsmen/static/script/script.js");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("templates/booking/base.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

describe("Base.html tests", () => {
    // test("Expects content to change", () => {
    //     buttonClick();
    //     expect(document.getElementById("par")
    //         .innerHTML).toEqual("You Clicked");
    // });
    test("sidebar should exist", () => {
        open();
        expect(document.getElementById("sidebar").classList).toContain("open");
    });
});