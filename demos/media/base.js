// ECMAScript 5 Strict Mode
"use strict";

// --------------------------------------------------------
// $jq :: JQuery nonconflict reference.
// See :: http://www.tvidesign.co.uk/blog/improve-your-jquery-25-excellent-tips.aspx#tip19
// --------------------------------------------------------
window.$ = jQuery.noConflict();

(function($) {

	// Set of navigable document types.
	var navigableDocumentTypes = [
		"cim-1-software-modelcomponent"
	]

	// Predicate returning whether a document type is navigable or not.
	var isNavigableDocument = function () {
		return !_.isUndefined(_.find(navigableDocumentTypes, function (docType) {
			return $("body").hasClass(docType);
		}));	
	};

    // Event handler for document ready event.
    $(document).ready(function() {
		// Pointers.
		var $doc = $(".esdoc-document");
		var $header = $doc.find("> header");
		var $nav = $doc.find("> nav");
		var $article = $doc.find("> article");
		var $footer = $doc.find("> footer");
		var $tables = $doc.find("table");

		// Style headers.
		$doc.find("h2, h3, h4, h5").addClass("bg-primary");

		// Style tables.
		$tables.addClass("table table-hover table-condensed bg-info");	
		$tables.find("tr td.esdoc-field-name").addClass("col-md-3");
		$tables.find("tr td.esdoc-field-subname").addClass("col-md-1");

		// Style navbars.
		if (isNavigableDocument()) {
			$nav.find("ul").addClass("nav nav-inverse nav-tabs nav-justified");	
			$nav.find("ul li a").attr("data-toggle", "tab");
			$nav.find("ul li:first").addClass('active');
			$article.addClass("tab-content");	
			$article.find(" > section").addClass("tab-pane");
			$article.find(" > section > header").hide();	
		} else {
			$nav.hide();
		}

		// Hide null fields.
		// $('.esdoc-document .esdoc-field-value:contains(--)').parent().hide();
    });

})(window.$);
