// 上传图片相关js

WP_Album._upload_var = {
	isFolded: false,
	fileCount: 0,
	fileList: null,
	fileTotalSize: 0,
	fileUploadCount: 0,
	fileUploadSize: 0,
	refusedList: [],
	url: "http://q.pnq.cc/works/uploader/upload-receiver.php?album=0"
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
			//location.hash = "i=" + i + ",t0=" + t0 + ",t1=" + t1 + ",ds=" + ds;
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
	},
	jsUpInit: function () {
		$("uploadArea").getElementsByTagName("li")[0].innerHTML += "，单张最大200K"
		$("uploadArea").getElementsByTagName("li")[1].innerHTML = "";
		//$D.removeClass("uploadBox", "hidden");
		$D.setStyle("uploadRightInfo", "margin-top", "10px");

		var html = "<form id=\"frmJsUploader\" action=\"" + WP_Album._upload_var.url + " method=\"post\">"
			+ "<p>1.<span><input type=\"file\" id=\"file1\" name=\"file1\" /></span>　　"
			+ "5.<span><input type=\"file\" id=\"file5\" name=\"file5\" /></span></p>"
			+ "<p>2.<span><input type=\"file\" id=\"file2\" name=\"file2\" /></span>　　"
			+ "6.<span><input type=\"file\" id=\"file6\" name=\"file6\" /></span></p>"
			+ "<p>3.<span><input type=\"file\" id=\"file3\" name=\"file3\" /></span>　　"
			+ "7.<span><input type=\"file\" id=\"file7\" name=\"file7\" /></span></p>"
			+ "<p>4.<span><input type=\"file\" id=\"file4\" name=\"file4\" /></span>　　"
			+ "8.<span><input type=\"file\" id=\"file8\" name=\"file8\" /></span></p>"
			+ "</form>"
			+ "<div class=\"hidden\"><form id=\"frmTmp\"></form></div>";	//用于清空file域
		$("uploadMainInfo").innerHTML = html;

		var chkSubmitEnable = function () {
			var enable = 1;
			$D.getElementsBy(function (o) {
				return o.type == "file";
			}, "input", "uploadMainInfo", function (o) {
				//alert("v: \"" + o.value + "\"");
				if (o.value != "") enable = 0;
			});
			BTN902.btns["btn-upload"].disable(enable);
		};

		$D.getElementsBy(function (o) {
			return o.type == "file";
		}, "input", "uploadMainInfo", function (o) {
			$E.on(o, "change", function () {
				var size = 0;
				var img = new Image();
				//alert(this.value);
				try {
					img.dynsrc = this.value;
					size = img.fileSize;
				} catch (e) {
					//var fso = new ActiveXObject("Scripting.FileSystemObject");
					//size = fso.GetFile(this.value).size;
				}
				if (size > 200 * 1024) {
					alert("上传图片大小超过200K，请压缩后重新上传。");
					var p = this.parentNode;
					$("frmTmp").appendChild(this);
					$("frmTmp").reset();
					p.appendChild(this);
				}
				chkSubmitEnable();
			});
		});

		BTN902.btns["btn-upload"].on("click", function () {
			$("uploadTopInfo2").innerHTML = "<div class=\"smallInfo\">上传中... 请勿刷新本页面</div>";
			$D.setStyle("uploadTopInfo", "display", "block");
			BTN902.btns["btn-upload"].disable(1);
			//$("frmJsUploader").submit();
			
			var ovlay = mkEl("div", {className: "overlay"});
			$D.setStyle(ovlay, "width", $("albumArea").offsetWidth - 20 + "px");
			$D.setStyle(ovlay, "height", $("albumArea").scrollHeight + "px");
			$("albumArea").appendChild(ovlay);

			var ovlay2 = mkEl("div", {className: "overlay"});
			$D.setStyle(ovlay2, "width", $("uploadMainInfo").offsetWidth - 20 + "px");
			$D.setStyle(ovlay2, "height", $("uploadMainInfo").offsetHeight + "px");
			$("uploadMainInfo").appendChild(ovlay2);
		});
	},
	uploaderInit: function () {
		//if (true) {
		if (!swfobject.hasFlashPlayerVersion("10")) {
			//如果不支持相应的Flash版本
			WP_Album._upload_fun.jsUpInit();
			return;
		}

		WP_Album.uploader = new AliUploader("selectFilesLink", {
			url: WP_Album._upload_var.url,
			width: 124,
			height: 45,
			buttonSkin: "img090216/uploadBtn.png",
			allowMulti: true,
			sizeLimitEach: 200 * 1024,
			compressSize: 3 * 1024 * 1024
		});

		WP_Album.uploader.swfReady(function (evt) {
			WP_Album.uploader.setAllowLogging(true);
			var ff = new Array({description:"图像 | images", extensions:"*.jpg;*.png;*.gif"},
				{description:"视频 | videos", extensions:"*.avi;*.mov;*.mpg"});
			WP_Album.uploader.setFileFilters(ff);
			if (WP_Album.curSelect) {
				WP_Album.uploader.enable();
			} else {
				WP_Album.uploader.disable();
			}
		})
		.fileSelect(function (evt) {
			log(evt);
			WP_Album._upload_var.fileList = evt.fileList;
			WP_Album._upload_fun.addFileList(evt.fileList);
			BTN902.btns["btn-upload"].disable(0);
			if (WP_Album._upload_var.refusedList.length) {
				$("uploadTopInfo2").innerHTML = "<div class=\"bigInfo\">抱歉，以下图片因大于 5M 已被移除上传队列：</div><div class=\"refusedList\"><span>" + WP_Album._upload_var.refusedList.join("</span> / <span>") + "</span></div>";
				$D.setStyle("uploadTopInfo", "display", "block");
			}
		})
		.fileRefused(function (evt) {
			WP_Album._upload_var.refusedList.push(evt.name);
		})
		.uploadStart(function (evt) {
			//info(evt);
		})
		.uploadComplete(function (evt) {
			info(evt);
			//alert("ob size: " + WP_Album._upload_var.fileList[evt.id].size);
			WP_Album._upload_var.fileUploadCount ++;
			WP_Album._upload_var.fileUploadSize += WP_Album._upload_var.fileList[evt.id].size;
			//alert("total: " + WP_Album._upload_var.fileUploadSize);
			//$D.setStyle("uploaderProcessBar", "width", Math.floor(100 * WP_Album._upload_var.fileUploadSize / WP_Album._upload_var.fileTotalSize) + "%");
			$D.setStyle("uploaderProcessBar", "width", Math.floor(100 * WP_Album._upload_var.fileUploadCount / WP_Album._upload_var.fileCount) + "%");
			$D.getElementsByClassName("act", "div", "fileLi-" + evt.id, function (o) {
				$D.replaceClass(o, "ready", "ok");
			});
			$D.addClass("fileLi-" + evt.id, "ok");
			$("uploadFileList").scrollTop += 25;
		})
		.uploadCompleteData(function (evt) {

		})
		.uploadProgress(function (evt) {
			info(evt);
			var t = WP_Album._upload_var.fileUploadSize,
				t2 = t + evt.bytesLoaded;
			$D.setStyle("fileLi-" + evt.id, "background-position", evt.percent + "% 50%");
			//alert("cur: " + t2);
			//$D.setStyle("uploaderProcessBar", "width", Math.floor(100 * t2 / WP_Album._upload_var.fileTotalSize) + "%");
		})
		.finish(function (evt) {
			alert("finish!");
			//location.href = "a-7.html";
		})
		.uploadError(function (evt) {
			info(evt);
		});

		BTN902.btns["btn-upload"].on("click", function () {
			$("uploadTopInfo2").innerHTML = "<div class=\"smallInfo\">上传中... 请勿刷新本页面</div>";
			$D.setStyle("uploadTopInfo", "display", "block");
			$("uploadFileList").scrollTop = 0;
			WP_Album.uploader.uploadAll();
			WP_Album.uploader.disable();
			BTN902.btns["btn-upload"].disable(1);
			$D.setStyle("uploaderProcess", "display", "block");

			$D.getElementsByClassName("size", "div", "uploadMainInfo", function (o) {
				o.innerHTML = "&nbsp;";
			});
			$D.getElementsByClassName("act", "div", "uploadMainInfo", function (o) {
				o.innerHTML = "&nbsp;";
			})[0].innerHTML = "状态";
			$D.getElementsBy(function (o) {
				return true;
			}, "li", "uploadFileList", function (o) {
				$D.addClass(o, "ready");
			});

			var ovlay = mkEl("div", {className: "overlay"});
			$D.setStyle(ovlay, "width", $("albumArea").offsetWidth - 20 + "px");
			$D.setStyle(ovlay, "height", $("albumArea").scrollHeight + "px");
			$("albumArea").appendChild(ovlay);
		});
	},
	addFileList: function (lst) {
		var ul = $("uploadFileList"), li, k;
		while (ul.firstChild) {
			ul.removeChild(ul.firstChild);
		}
		WP_Album._upload_var.list = lst;
		for (k in lst) {
			li = WP_Album._upload_fun.mkFileLi(lst[k]);
			ul.appendChild(li);
		}
		WP_Album._upload_fun.summary();
	},
	summary: function () {
		WP_Album._upload_var.fileCount = 0;
		WP_Album._upload_var.fileTotalSize = 0;
		WP_Album._upload_var.fileUploadCount = 0;
		WP_Album._upload_var.fileUploadSize = 0;
		var lst = WP_Album._upload_var.list;
		for (var k in lst) {
			WP_Album._upload_var.fileCount ++;
			WP_Album._upload_var.fileTotalSize += lst[k].size;
		}
		$("uploader-fileCount").innerHTML = WP_Album._upload_var.fileCount;
		$("uploader-fileTotleSize").innerHTML = WP_Album._upload_fun.formatSize(WP_Album._upload_var.fileTotalSize, " ");
		if (WP_Album._upload_var.fileCount == 0) {
			BTN902.btns["btn-upload"].disable(1);
		}
	},
	mkFileLi: function (ob) {
		var li = document.createElement("li");
		li.id = "fileLi-" + ob.id;
		var tmp = mkEl("div", {className: "title"});
		tmp.appendChild(document.createTextNode(ob.name));
		li.appendChild(tmp);
		tmp = mkEl("div", {className: "size"});
		tmp.appendChild(document.createTextNode(WP_Album._upload_fun.formatSize(ob.size)));
		li.appendChild(tmp);
		tmp = mkEl("div", {className: "act"});
		var tmp2 = mkEl("a", {className: "del"});
		tmp2.title = "删除";
		$E.on(tmp2, "click", function () {WP_Album._upload_fun.removeFile(ob.id);});
		tmp2.appendChild(document.createTextNode("删除"));
		tmp.appendChild(tmp2);
		li.appendChild(tmp);
		return li;
	},
	removeFile: function (fId) {
		delete WP_Album._upload_var.list[fId];
		WP_Album.uploader.removeFile(fId);
		var anim = new $Y.Anim("fileLi-" + fId, {
			height: {to: 0}
		}, 0.2);
		anim.onComplete.subscribe(function () {
			$("uploadFileList").removeChild($("fileLi-" + fId));
		});
		anim.animate();
		WP_Album._upload_fun.summary();
	},
	formatSize: function (n, sp) {
		var s = "";
		var sp2 = sp || "";
		if (n < 1024) {
			s = n + sp2 + "B";
		} else if (n < 1048576) {
			s = Math.ceil(n / 1024) + sp2 + "KB";
		} else {
			s = Math.ceil(n / 1048576) + sp2 + "MB";
		}
		return s;
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
		anim_Album_fold.onComplete.subscribe(function () {
			getTreeHeight();
		});

		$D.setStyle("upload-step2", "background-position", "10px -263px");
		$D.setStyle("upload-step2-toInfo", "display", "inline");
		//$D.removeClass("btn-selectPhoto", "bo_902btn_disabled");
		if (WP_Album.uploader) {
			WP_Album.uploader.enable();
			WP_Album.uploader.url = WP_Album.uploader.url.replace(/album=[^&]*?/, "album=" + WP_Album.curSelect.id);
		}
	}
	setTimeout(function () {
		WP_Album._upload_fun.scrollToAlbum(WP_Album.curSelect.i);
	}, 1);

	$("upload-step2-albumName").innerHTML = WP_Album.curSelect.title;
	$D.removeClass("uploadBox", "hidden");
	$D.removeClass("uploadAct", "hidden");
	getTreeHeight();
});

function swfUploadInit() {
}

var g_msgbox;
