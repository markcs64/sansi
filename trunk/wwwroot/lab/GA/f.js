/* f.js
 *
 *
 */

var g_lifeCount = 0,
	g_geneLength = 55,
	g_canvasTag = false;

var park = {
	ga: null,
	init: function () {
		park.ga = new GA({
			lifeCount: g_lifeCount,
			geneLength: g_geneLength * (g_canvasTag ? 25 : 10),
			xRate: parseFloat($("#xRate").val()) || 0.7,
			mutationRate: parseFloat($("#mutationRate").val()) || 0.005
		});
		var canvas;
		for (var i = 0; i < g_lifeCount; i ++) {
			if (g_canvasTag) {
				canvas = document.createElement("canvas");
				canvas.setAttribute("width", 128);
				canvas.setAttribute("height", 128);
				document.getElementById("cell-" + i).appendChild(canvas);
			} else {
				canvas = new drjs.Canvas({
						width: 128,
						height: 128
					}, "cell-" + i);
				canvas.show();
			}
			park.cells.push(canvas);
		}
		park.draw();
		park.updateInfo(0);
		park.hideHistory();
	},
	busy: true,
	cells: [],
	clear: function () {
		var i, ctx;
		if (g_canvasTag) {
			for (i = 0; i < g_lifeCount; i ++) {
				ctx = park.cells[i].getContext("2d");
				//ctx.globalAlpha = 1;
				ctx.fillStyle = "#fff";
				ctx.fillRect(0, 0, 128, 128);
			}
		} else {
			for (i = 0; i < g_lifeCount; i ++) {
				park.cells[i].clear();
			}
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
		for (i = 0; i < l; i += g_geneLength) {
			park.drawOneClip(canvas, gene.substr(i, g_geneLength));
		}
	},
	drawOneClip: function (canvas, geneClip) {
		var ctx,
			x0 = parseInt(geneClip.substr(0, 7), 2),
			y0 = parseInt(geneClip.substr(7, 7), 2),
			x1 = parseInt(geneClip.substr(14, 7), 2),
			y1 = parseInt(geneClip.substr(21, 7), 2),
			x2 = parseInt(geneClip.substr(28, 7), 2),
			y2 = parseInt(geneClip.substr(35, 7), 2),
			r = parseInt(geneClip.substr(42, 4), 2),
			g = parseInt(geneClip.substr(46, 4), 2),
			b = parseInt(geneClip.substr(50, 4), 2),
			s = parseInt(geneClip.substr(54, 1), 2) + 1;
		if (g_canvasTag) {
			ctx = canvas.getContext("2d");
			//ctx.globalAlpha = 0.5;
			//ctx.strokeStyle = "#" + r + g + b;
			ctx.fillStyle = "rgba(" + r * 17 + ", " + g * 17 + ", " + b * 17 + ", 0.5)";
			//ctx.lineWidth = s;
			ctx.beginPath();
			ctx.moveTo(x0, y0);
			ctx.lineTo(x1, y1);
			ctx.lineTo(x2, y2);
			ctx.closePath();
			ctx.fill();
		} else {
			canvas.draw("line", [[x0, y0], [x1, y1]], 0, 0, "#" + r.toString(16) + g.toString(16) + b.toString(16), 0, s);
		}
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
		$("#time").html((Math.floor(t1 - t0) / 1000).toString());
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
		for (var li, i = 0, l = park.ga.bestHistory.length, ul = $("#bestHistory")[0], canvas, span; i < l; i ++) {
			li = document.createElement("li");
			ul.appendChild(li);
			if (g_canvasTag) {
				canvas = document.createElement("canvas");
				canvas.setAttribute("width", 128);
				canvas.setAttribute("height", 128);
				li.appendChild(canvas);
				span = document.createElement("span");
				span.appendChild(document.createTextNode(i));
				li.appendChild(span);
			} else {
				canvas = new drjs.Canvas({
						width: 128,
						height: 128
					}, li);
				canvas.show();
				canvas.draw("string", [i], 2, 2, "#f00");
			}
			park.drawOne(canvas, park.ga.bestHistory[i].gene);
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
	g_lifeCount = $("#park ul li").length;
	var canvasTag = document.createElement("canvas");
	g_canvasTag = !!canvasTag.getContext;
	if (!g_canvasTag) {
		$("#tagNotSupport").html("您的浏览器不支持Canvas标签，请使用支持Canvas标签的浏览器（如Firefox 3、Chrome等）浏览本页以获得最佳体验！");
	}

	$("#reward").val(Math.ceil(Math.sqrt(g_lifeCount) - 1));

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
		$(this).val("重新开始").blur();
		$("#howToPlay").html("点击左边的方格以选择您觉得最理想的图形..");
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
