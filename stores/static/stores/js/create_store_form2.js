Dropzone.autoDiscover = false;
$(document).ready(function () {
    var myDropzone1 = new Dropzone('form#myDropzone1', {
        maxFilesize: 2,
        paramName: 'file',
        maxFiles: 1,
        dictDefaultMessage: "تصویر لوگو فروشگاه را اینجا آپلود کنید.",
        dictMaxFilesExceeded: "شما فقط میتوانید یک عکس آپلود کنید.",
        addRemoveLinks: true,
        init: function () {
            this.on("complete", function (file) {
                $(".dz-remove").addClass('btn btn-primary mt-2').html('<i class="fas fa-trash-alt text-white ml-1"></i>حذف تصویر');
            });
        }

    });

    myDropzone1.on("maxfilesexceeded", function (file) {
        myDropzone1.removeFile(file);
    });

    var myDropzone2 = new Dropzone('form#myDropzone2', {
        maxFilesize: 2,
        paramName: 'file',
        maxFiles: 1,
        dictDefaultMessage: "تصویر کاور فروشگاه را اینجا آپلود کنید.",
        dictMaxFilesExceeded: "شما فقط میتوانید یک عکس آپلود کنید.",
        addRemoveLinks: true,
        init: function () {
            this.on("complete", function (file) {
                $(".dz-remove").addClass('btn btn-primary mt-2').html('<i class="fas fa-trash-alt text-white ml-1"></i>حذف تصویر');
            });
        }

    });

    myDropzone2.on("maxfilesexceeded", function (file) {
        myDropzone2.removeFile(file);
    });

});