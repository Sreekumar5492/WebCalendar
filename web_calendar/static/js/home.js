/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$(document).ready(function() {

    // page is now ready, initialize the calendar...

    $('#calendar').fullCalendar({
        // put yheight:465our options and callbacks here
        events: [
        {
            title  : 'event1',
            start  : '2016-02-01'
        },
        {
            title  : 'event2',
            start  : '2016-02-05',
            end    : '2016-02-07'
        },
        {
            title  : 'event3',
            start  : '2016-02-09T12:30:00',
            allDay : false // will make the time show
        }
    ]
    });

});