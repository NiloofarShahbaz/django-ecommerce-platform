$(document).ready(function () {
    $('ul.navbar-nav li.dropdown').hover(function () {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(500);
    }, function () {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeOut(500);
    });

    $('a.nav-link').hover(function () {
        $(this).find('i.fa-sign-in-alt').addClass('login-icon-hover');
    }, function () {
        $(this).find('i.fa-sign-in-alt').removeClass('login-icon-hover');
    });


});