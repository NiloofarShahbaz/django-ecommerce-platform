$(document).ready(function () {
    $(".text-less").each(function () {
        text = $(this).text();
        if (text.length > 100) {
            $(this).html(text.substr(0, 100) + '<span class="elipsis">' + text.substr(100) +
                '</span><a class="elipsis" href="#">...بیشتر</a>');
        }
    });

    $(".text-less > a.elipsis").click(function (e) {
        e.preventDefault();
        text = $(this).text();
        $(this).prev('span.elipsis').fadeToggle(0);
        if (text === '...کمتر') {
            $(this).text("...بیشتر");
        }
        else {
            $(this).text("...کمتر");
        }
    });
});