// �ϴ�ͼƬ���js

WP_Album._upload_var = {
	isFolded: false
};

WP_Album._upload_fun = {
	scrollToAlbum: function (i) {
		//����ָ�������
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
	photoList: function (pg) {
		//��ʾĳһҳ����Ƭ

	}
};

WP_Album.on("select", function () {
	//ѡ��ĳ������Ķ���
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
