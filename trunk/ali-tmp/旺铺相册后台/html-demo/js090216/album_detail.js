/* album detail */

function getSelectPhotos () {
	var selectedPhotos = [];
	$D.getElementsBy(function (o) {
			return o.checked;
		}, "input", "photoList", function (o) {
			selectedPhotos.push(o.value);
	});

	return selectedPhotos;
}

function delSelectPhotos () {
	var selectedPhotos = getSelectPhotos();
	if (selectedPhotos.length == 0) {
		alert("请先选择图片！");
	} else {
		if (confirm("您确定要删除选中的图片吗？")) {
			$("frmPhotoAction-action").value = "delete";
			$("frmPhotoAction-photos").value = selectedPhotos.join();
			$("frmPhotoAction").submit();
		}
	}
	return false;
}

function g_mvPhoto_albumListSelect () {
	var select = "";
	select += "<select style=\"width:18em;\" onchange=\"g_mvPhoto_targetChg(this)\">";

	for (var i = 0; i < g_albumList.length; i ++) {
		select += "<option value=\"" + g_albumList[i].id + "\""
			+ (g_albumList[i].id != g_album.id ? "" : " selected=\"selected\"")
			+ ">" + g_albumList[i].title + "</option>";
	}

	select += "</select>";

	return select;
}

var g_mvPhotoDialog,
	g_mvPhoto_albumList_html;
function moveSelectPhotos () {
	var selectedPhotos = getSelectPhotos();
	if (selectedPhotos.length == 0) {
		alert("请先选择图片！");
	} else {
		if (typeof(g_mvPhotoDialog) == "undefined")
			g_mvPhotoDialog = new MsgBox_oj();
		if (typeof(g_mvPhoto_albumList_html) == "undefined")
			g_mvPhoto_albumList_html = g_mvPhoto_albumListSelect();
		g_mvPhotoDialog.show(
			"移动相册",
			"<div style=\"font-weight:normal;\">相册目录：" + g_mvPhoto_albumList_html + "</div>",
			[
				{
					text: "确定",
					callback: function () {
						$("frmPhotoAction-action").value = "move";
						//$("frmPhotoAction-moveTo").value = "";
						$("frmPhotoAction-photos").value = selectedPhotos.join();
						$("frmPhotoAction").submit();
					}
				},
				{
					text: "取消"
				}
			]
		);
	}
	return false;
}

function g_mvPhoto_targetChg(o) {
	$("frmPhotoAction-moveTo").value = o.value;
}
