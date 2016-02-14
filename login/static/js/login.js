/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
$(document).ready(function () {
    jQuery.validator.addMethod("noSpace", function (value, element) {
        return value.indexOf(" ") < 0 && value != "";
    }, "No space please and don't leave it empty");
    $('#signupform').validate({
        errorClass: "invalid",
        validClass: "valid",
        rules: {
            name: {
                required: true,
                minlength: 2,
                noSpace: true
            },
            email: {
                required: true,
                noSpace: true,
                email: true
            },
            username: {
                required: true,
                noSpace: true,
                minlength: 3,
                remote: {
                    url: "/user_available/",
                    type: "post",
                    data: {
                        username: function () {
                            return $("#username1").val();
                        }
                    }
                }
            },
            password1: {
                required: true,
                noSpace: true,
                minlength: 4
            },
            password2: {
                required: true,
                noSpace: true,
                minlength: 4,
                equalTo: '#password1'
            }

        },
        errorElement: 'div',
        errorPlacement: function (error, element) {
            var placement = $(element).data('error');
            if (placement) {
                $(placement).append(error);
            } else {
                error.insertAfter(element);
            }

        }
    });
    $('#loginform').validate({
        errorClass: "invalid",
        validClass: "valid",
        rules: {
            username: {
                required: true,
                minlength: 3
            },
            password: {
                required: true,
                minlength: 3
            }
        },
        errorElement: 'div',
        errorPlacement: function (error, element) {
            var placement = $(element).data('error');
            if (placement) {
                $(placement).append(error);
            } else {
                error.insertAfter(element);
            }
        }
    });
    $('#loginform').on('submit', function (e) {
        $('#msg').hide();
        if ($('#loginform').valid()) {
            e.preventDefault();
            $('.login_loader').show();
            $.ajax({
                type: 'POST',
                url: '/loginuser/',
                data: {
                    'username': $('#username:visible').val(),
                    'password': $('#password').val(),
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function (data) {
                    var d = $.parseJSON(data);
                    if (d.login) {
                        $('#msg').show();
                        $('#msg').text(d.message).css('color', 'green');
                        window.location.href = '/web_calendar/home/';
                    } else {
                        $('.login_loader').hide();
                        $('#username').addClass('invalid');
                        $('#password').addClass('invalid');
                        $('#msg').show();
                        $('#msg').text(d.message).css('color', 'red');


                    }
                }

            });
        }

    });
    $('#signupform').on('submit', function (e) {
        $('#msg1').hide();
        if ($('#signupform').valid()) {
            e.preventDefault();
            $('.signup_loader').show();
            $.ajax({
                type: 'POST',
                url: '/signup/',
                data: {
                    'name': $('#name').val(),
                    'email': $('#email1').val(),
                    'username': $('#username1').val(),
                    'password1': $('#password1').val(),
                    'password2': $('#password2').val(),
                    'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function (data) {
                    $('.signup_loader').hide();
                    var d = $.parseJSON(data);
                    if (d.status) {
                        $('#signup_form').velocity('fadeOut', {duration: 50});
                        $('#login_form').velocity('fadeIn', {duration: 500});
                        $('#msg1').show();
                        $('#msg1').text(d.message).css('color', 'green');
                    } else {
                        $('#msg1').show();
                        $('#msg1').text(d.message).css('color', 'red');
                    }
                }

            });
        }

    });
    $(document).on('click', '#signup', function (e) {
        e.preventDefault();
        $('#login_form').velocity('fadeOut', {duration: 500});
        $('#signup_form').velocity('fadeIn', {duration: 1500});

    });
    $(document).on('click', '#login', function (e) {
        e.preventDefault();
        $('#signup_form').velocity('fadeOut', {duration: 500});
        $('#login_form').velocity('fadeIn', {duration: 1500});

    });
    $('#calendar').fullCalendar({
        // put your options and callbacks here
        height: 100,
        header: {
            left: 'title',
            center: '',
            right: ''
        },
        fixedWeekCount:false,
        contentHeight: 50
    });
});