$(document).ready(function() {
    $("#formularioContacto").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 3
            },
            apellido: {
                required: true,
                minlength: 3
            },
            correo: {
                required: true,
                email: true
            },
            telefono: {
                required: true,
                number: true,
                minlength: 9,
                maxlength: 9
            },
            mensaje: {
                required: true,
                minlength: 10,
                maxlength: 150
            }

        },
        messages: {
            nombre: {
                required: "Debe ingresar su nombre",
                minlength: "El nombre debe tener mínimo 3 carácteres"
            },
            apellido: {
                required: "Debe ingresar su apellido",
                minlength: "El apellido debe tener mínimo 3 carácteres"
            },
            correo: {
                required: "Debe ingresar su correo electrónico",
                email: "El email debe tener un formato válido"
            },
            telefono: {
                required: "Debe ingresar su teléfono",
                number: "Debe ingresar sólo números",
                minlength: "El teléfono debe tener 9 dígitos",
                maxlength: "El teléfono debe tener 9 dígitos"
            },
            mensaje: {
                required: "Debe ingresar un mensaje",
                minlength: "El mensaje debe tener mínimo 10 carácteres",
                maxlength: "El mensaje no debe tener mas de 150 carácteres"
            }
        }

    });

});





$("#btn_enviar").click(function () {

    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let celular = $("#celular").val()
    let email = $("#email").val()
    let mensaje = $("#mensaje").val()
    console.log(nombre)
});




