/* f.js
 *
 *
 */

var g_lifeCount = 9;

var park = {
	ga: null,
	init: function () {
		park.ga = new GA({
			lifeCount: g_lifeCount,
			geneLength: 41 * 50
		});
		var canvas;
		for (var i = 0; i < g_lifeCount; i ++) {
			canvas = new drjs.Canvas({
					width: 128,
					height: 128
				}, "cell-" + i);
			park.cells.push(canvas);
			canvas.show();
		}
	},
	busy: true,
	cells: [],
	clear: function () {
		for (var i = 0; i < g_lifeCount; i ++) {
			park.cells[i].clear();
		}
	},
	draw: function () {
		park.clear();
		for (var i = 0; i < g_lifeCount; i ++) {
			park.drawOne(park.cells[i], park.ga.lives[i].gene);
		}
	},
	drawOne: function (canvas, gene) {
		var i, l = gene.length;
		for (i = 0; i < l; i += 50) {
			park.drawOneClip(canvas, gene.substr(i, 50));
		}
	},
	drawOneClip: function (canvas, geneClip) {
		var x0 = parseInt(geneClip.substr(0, 7), 2),
			y0 = parseInt(geneClip.substr(7, 7), 2),
			x1 = parseInt(geneClip.substr(14, 7), 2),
			y1 = parseInt(geneClip.substr(21, 7), 2),
			r = parseInt(geneClip.substr(28, 4), 2).toString(16),
			g = parseInt(geneClip.substr(32, 4), 2).toString(16),
			b = parseInt(geneClip.substr(36, 4), 2).toString(16),
			s = parseInt(geneClip.substr(40, 1), 2) + 1;
		canvas.draw("line", [[x0, y0], [x1, y1]], 0, 0, "#" + r + g + b, 0, s);
	},
	addScore: function (i) {
		var reward = parseInt($("#reward").val()) || 1;
		park.ga.lives[i].addScore(reward);
		$("#reward").val(reward);
	},
	next: function (i) {
		var processInfo = $("#process").html();
		park.busy = true;
		var t0 = new Date(), t1;
		park.addScore(i);
		park.ga.next();
		park.draw();

		t1 = new Date();
		$("#gen").html(park.ga.generation);
		$("#mutation").html(park.ga.mutationCount.toString());
		$("#time").html(Math.floor(t1 - t0));
		park.busy = false;
		$("#park ul li").removeClass("selected");
	}
};

$(document).ready(function () {
	park.init();

	$("#park ul li").mouseover(function () {
		$(this).addClass("hover");
	}).mouseout(function () {
		$(this).removeClass("hover");
	}).click(function () {
		if (park.busy) return;
		$(this).removeClass("hover");
		$(this).addClass("selected");
		var i = parseInt(this.id.match(/\d+/)[0]);
		setTimeout(function () {
			park.next(i);
		}, 1);
	});

	$("#start").click(function () {
		setTimeout(park.draw, 1);
		this.disabled = true;
		park.busy = false;
	});
});
