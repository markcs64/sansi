/* f.js
 *
 *
 */

var park = {
	init: function () {
		var canvas;
		for (var i = 0; i < 9; i ++) {
			canvas = new drjs.Canvas({
					width: 128,
					height: 128
				}, "cell-" + i);
			park.cells.push(canvas);
			canvas.show();
		}
	},
	cells: []
};

$(document).ready(function () {
	park.init();

	$("#park ul li").mouseover(function () {
		$(this).addClass("hover");
	}).mouseout(function () {
		$(this).removeClass("hover");
	}).click(function () {
		$(this).removeClass("hover");
		$(this).addClass("selected");
	});
});
