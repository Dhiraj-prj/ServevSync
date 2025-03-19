// admin_custom.js

$(document).ready(function() {
    // Optional: Add an animation for the sidebar toggle
    $(".sidebar-toggle").on("click", function() {
        $(".main-sidebar").toggleClass("collapsed");
        $("body").toggleClass("sidebar-collapsed");
    });

    // Optional: More custom JS can be added here as needed
});
