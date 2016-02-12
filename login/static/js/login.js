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
                noSpace:true
            },
            email: {
                required: true,
                email: true,
                noSpace:true
            },
            username: {
                required: true,
                noSpace:true,
                minlength: 3,
                remote: {
                    url: "/user_available/",
                    type: "post",
                    data: {
                        username: function () {
                            return $("#username").val();
                        }
                    }
                }
            },
            password1: {
                required: true,
                noSpace:true,
                minlength: 4
            },
            password2: {
                required: true,
                noSpace:true,
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

})