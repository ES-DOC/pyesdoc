// ECMAScript 5 Strict Mode
"use strict";

// --------------------------------------------------------
// $jq :: JQuery nonconflict reference.
// See :: http://www.tvidesign.co.uk/blog/improve-your-jquery-25-excellent-tips.aspx#tip19
// --------------------------------------------------------
window.$ = jQuery.noConflict();

(function($) {

    // Event handler for document ready event.
    $(document).ready(function() {
		$(".page-content-container h2, article > h3").addClass("bg-primary");
		$("article > section > h4").addClass("well well-sm");
		$("h2 small").addClass("bg-primary");
		$("table").addClass("bg-info");	
		$(".esdoc-field-name").css("text-transform", "capitalize");	
    });

})(window.$);
