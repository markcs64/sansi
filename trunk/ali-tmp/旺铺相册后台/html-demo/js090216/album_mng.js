/* album_mng.js */

function selectOrder() {
	$D.getElementsByClassName("selectOrder-pull", "span", "main_right_body", function (o) {
		$E.on(o, "click", function (e) {
			$D.setStyle(o.parentNode.getElementsByTagName("ul")[0], "display", "block");
			$E.stopPropagation(e);
		});
	});

	$E.on(document, "click", function () {
		$D.getElementsByClassName("selectOrder-options", "ul", "main_right_body", function (o) {
			$D.setStyle(o, "display", "none");
		});
	});
}

function selectOrder_show() {

}
