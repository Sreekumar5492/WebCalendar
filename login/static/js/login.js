/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

$('#signupform').validate({
    errorClass: "invalid",
    validClass: "valid",
    rules: {
        name: {
            required: true,
            minlength: 2
        },
        email: {
            required: true,
            email: true
        },
        username: {
            required: true,
            minlength: 3
        },
        password1: {
            required: true,
            minlength: 4
        },
        password2: {
            required: true,
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
