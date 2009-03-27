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
			geneLength: 41 * 15,
			xRate: parseFloat($("#xRate").val()) || 0.7,
			mutationRate: parseFloat($("#mutationRate").val()) || 0.005
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
		park.draw();
		park.updateInfo(0);
		park.hideHistory();
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
		for (i = 0; i < l; i += 41) {
			park.drawOneClip(canvas, gene.substr(i, 41));
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
	updateInfo: function (t0) {
		t1 = new Date();
		if (!t0) t0 = t1;
		$("#gen").html(park.ga.generation.toString());
		$("#mutation").html(park.ga.mutationCount.toString());
		$("#time").html(Math.floor(t1 - t0).toString());
		park.busy = false;
		$("#park ul li").removeClass("selected");
	},
	next: function (i) {
		var processInfo = $("#process").html();
		park.busy = true;
		var t0 = new Date(), t1;
		park.addScore(i);
		park.ga.next();
		park.draw();

		park.updateInfo(t0);
	},
	showHistory: function () {
		$("#bestHistory").html("").css("height", Math.floor(park.ga.bestHistory.length / 5 + 0.99) * 140 + 10 + "px").slideDown();
		for (var li, i = 0, l = park.ga.bestHistory.length, ul = $("#bestHistory")[0], canvas; i < l; i ++) {
			li = document.createElement("li");
			ul.appendChild(li);
			canvas = new drjs.Canvas({
					width: 128,
					height: 128
				}, li);
			canvas.show();
			park.drawOne(canvas, park.ga.bestHistory[i].gene);
			canvas.draw("string", [i], 2, 2, "#f00");
		}
		$("#showHistory").html("隐藏进化历史");
	},
	hideHistory: function () {
		$("#bestHistory").html("").slideUp("slow", function () {
			$("#showHistory").html("显示进化历史");
		});
	}
};

$(document).ready(function () {
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
		setTimeout(park.init, 1);
		park.busy = false;
		$(this).val("重新开始");
	});

	$("#xRate").change(function () {
		var v = parseFloat($(this).val()) || 0.7;
		park.ga.xRate = v;
		$(this).val(v);
	});

	$("#mutationRate").change(function () {
		var v = parseFloat($(this).val()) || 0.005;
		park.ga.mutationRate = v;
		$(this).val(v);
	});

	$("#showHistory").toggle(park.showHistory, park.hideHistory).click(function () {
		$(this).blur();
	});
});
