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
		// Headers.
		$(".esdoc-document h2, .esdoc-document h3").addClass("bg-print");
		$(".esdoc-document h2 small").addClass("bg-print");
		$(".esdoc-document h4").addClass("bg-print");
		$(".esdoc-document h5").addClass("bg-print");

		// Tables.
		$(".esdoc-document table").addClass("bg-info table table-hover table-condensed");	
		$(".esdoc-document table tr td.esdoc-field-name").addClass("col-md-3");
		$(".esdoc-document table tr td.esdoc-field-subname").addClass("col-md-1");
		$(".esdoc-document table tr td.esdoc-field-name").css("text-transform", "capitalize");

		// Navigation when appropriate.
		if ($(".esdoc-document nav").length) {
			$(".esdoc-document nav ul").addClass("nav nav-inverse nav-tabs nav-justified");	
			$(".esdoc-document nav ul li a").attr("data-toggle", "tab");	
			$(".esdoc-document article").addClass("tab-content");	
			$(".esdoc-document article > section").addClass("tab-pane");	
			$(".esdoc-document article > section > h3").hide();	
			$('.esdoc-document nav ul li:first').addClass('active');
		}

		// Hide null fields.
		$('.esdoc-document .esdoc-field-value:contains(--)').parent().hide();
    });

})(window.$);
