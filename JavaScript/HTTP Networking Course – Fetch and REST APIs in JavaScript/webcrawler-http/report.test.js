const {sortPages} = require('./report.js')
const {test, expect} = require('@jest/globals')

test('sortPages 2 pages', () => {
    const input = {
        'https://waslane.dev' : 3,
        'https://waslane.dev/path' : 1,

    }
    const actual = sortPages(input)
    const expected = [
        ['https://waslane.dev', 3],
        ['https://waslane.dev/path', 1],
    ]
    expect(actual).toEqual(expected)
})

test('sortPages 5 pages', () => {
    const input = {
        'https://waslane.dev/path' : 1,
        'https://waslane.dev' : 3,
        'https://waslane.dev/path2' : 5,
        'https://waslane.dev/path3' : 2,
        'https://waslane.dev/path4' : 9,

    }
    const actual = sortPages(input)
    const expected = [
        ['https://waslane.dev/path4', 9],
        ['https://waslane.dev/path2', 5],
        ['https://waslane.dev', 3],
        ['https://waslane.dev/path3', 2],
        ['https://waslane.dev/path', 1],
    ]
    expect(actual).toEqual(expected)
})
