/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


$(document).ready(function () {
    var pdata;
    var event = [];
    // page is now ready, initialize the calendar...
    $.ajax({
        method: 'POST',
        url: '/web_calendar/get_events/',
        data: {
            'data': 'events'
        },
        success: function (data) {
            pdata = JSON.parse(data);
            console.log('parsed' + pdata);
            $.each(pdata, function (i, ele) {
                var event_dict = {};
                event_dict.title = ele.name;
                event_dict.start = ele.start;
                event_dict.end = ele.end;
                console.log(event_dict)
                event.push(event_dict);
            });
            $('#calendar').fullCalendar({
                events: event
            });
        }

    });


});