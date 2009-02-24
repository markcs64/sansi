// 上传图片相关js

WP_Album._upload_var = {
	isFolded: false
};

WP_Album._upload_fun = {
	scrollToAlbum: function (i) {
		//滚到指定的相册
		var o = $("albumArea"),
			t0 = o.scrollTop,
			t1 = Math.floor(i / 5) * 206,
			ds = t1 - o.scrollTop,
			step = ds / 10;

		var f = function () {
			ds = t1 - o.scrollTop;
			location.hash = "i=" + i + ",t0=" + t0 + ",t1=" + t1 + ",ds=" + ds;
			if (ds == 0) return;
			//step = ds > 0 ? Math.ceil(ds / 10) : Math.floor(ds / 3);
			if (Math.abs(ds) < Math.abs(step)) step = ds;
			o.scrollTop += step;
			setTimeout(f, 10);
		};

		f();
	},
	photoList: function () {
		//照片上传完毕后第一页的照片以供修改
		var photoLi = function (ob, i) {
			var html = "<div class=\"left\">"
				+ "<div class=\"photo\">"
				+ "<table align=\"center\" cellpadding=\"0\" cellspacing=\"0\">"
				+ "<tr><td class=\"tb-bd-7\"></td><td class=\"tb-bd-8\"></td><td class=\"tb-bd-9\"></td></tr>"
				+ "<tr><td class=\"tb-bd-4\"></td><td class=\"tb-bd-5\">"
				+ "<div class=\"photo-img\"><img src=\"" + ob.src + "\" /></div>"
				+ "</td><td class=\"tb-bd-6\"></td></tr>"
				+ "<tr><td class=\"tb-bd-1\"></td><td class=\"tb-bd-2\"></td><td class=\"tb-bd-3\"></td></tr>"
				+ "</table>"
				+ "</div>"
				+ "<input type=\"radio\" id=\"setCover-" + ob.id + "\" name=\"setCover\" value=\"" + ob.id + "\" /> "
				+ "<label for=\"setCover-" + ob.id + "\">设为封面</label>"
				+ "</div>";

			html += "<div class=\"right\">"
				+ "<p>图片标题：<input type=\"text\" id=\"photoTitle-" + ob.id + "\" name=\"photoTitle-" + ob.id + "\" value=\"" + ob.title + "\" /></p>"
				+ "<p><span class=\"abs\">图片内容：</span>　　　　　<textarea id=\"photoDesc-" + ob.id + "\">" + ob.desc + "</textarea></p>";
			if (i < g_photos.length - 1)
				html += "<p class=\"tright\"><a href=\"#\" onclick=\"return WP_Album._upload_fun.copyDown(" + i + ");\">向下复制内容</a></p>";
			html += "</div>";

			return html;
		};

		var html = "<ul>";
		for (var i = 0; g_photos[i]; i ++) {
			html += "<li>" + photoLi(g_photos[i], i) + "</li>";
		}
		html += "</ul>";

		$("photo-list").innerHTML = html;
		var td5 = $D.getElementsByClassName("photo-img");
		for (var j = 0; td5[j]; j ++) {
			if (td5[j].offsetWidth > 180) {
				$D.setStyle(td5[j], "width", "180px");
			}
		}
		if (g_photos.length < 10) {
			$D.setStyle("photo-list", "height", g_photos.length * 196 + "px");
		} else {
			$D.setStyle("photo-list", "height", 1960 + "px");
		}
	},
	copyDown: function (i) {
		//照片标题及描述向下复制
		if (g_photos[i + 1]) {
			$("photoTitle-" + g_photos[i + 1].id).value = $("photoTitle-" + g_photos[i].id).value;
			$("photoDesc-" + g_photos[i + 1].id).value = $("photoDesc-" + g_photos[i].id).value;
		}
		if (i % 10 == 9) {
			WP_GotoPage.items[0].gotoNextPage();
		}
		$("photoTitle-" + g_photos[i + 1].id).focus();
		return false;
	}
};

WP_Album.on("select", function () {
	//选中某个相册后的动作
	if (!WP_Album._upload_var.isFolded) {
		var anim_Album_fold = new YAHOO.util.Anim("albumArea", {
				height: {to: 206}
			},
			0.5);
		anim_Album_fold.animate();

		$D.setStyle("upload-step2", "background-position", "10px -263px");
		$D.setStyle("upload-step2-toInfo", "display", "inline");
		$D.removeClass("btn-selectPhoto", "bo_902btn_disabled");
	}
	setTimeout(function () {
		WP_Album._upload_fun.scrollToAlbum(WP_Album.curSelect.i);
	}, 1);

	$("upload-step2-albumName").innerHTML = WP_Album.curSelect.title;
});

var g_msgbox;
$E.onDOMReady(function () {
});
