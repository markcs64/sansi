// ActionScript file
package {
	public class CNMap {
		public var prov:Object = {
			zj: "浙江",
			s1x: "山西",
			hlj: "黑龙江",
			tw: "台湾",
			gd: "广东",
			fj: "福建",
			jx: "江西",
			hun: "湖南",
			gz: "贵州",
			gx: "广西",
			gs: "甘肃",
			js: "江苏",
			sh: "上海",
			hain: "海南",
			hub: "湖北",
			nx: "宁夏",
			s3x: "陕西",
			jl: "吉林",
			hen: "河南",
			cq: "重庆",
			yn: "云南",
			sc: "四川",
			xz: "西藏",
			qh: "青海",
			xj: "新疆",
			tj: "天津",
			nmg: "内蒙古",
			bj: "北京",
			sd: "山东",
			heb: "河北",
			ln: "辽宁",
			ah: "安徽",
			hk: "香港",
			om: "澳门"
		};
		
		public var hot:Object = {
			zj: 10,	//浙江
			s1x: 5,	//山西
			hlj: 5,	//黑龙江
			tw: 5,	//台湾
			gd: 10,	//广东
			fj: 8,	//福建
			jx: 5,	//江西
			hun: 5,	//湖南
			gz: 5,	//贵州
			gx: 5,	//广西
			gs: 2,	//甘肃
			js: 9,	//江苏
			sh: 10,	//上海
			hain: 5,	//海南
			hub: 5,	//湖北
			nx: 5,	//宁夏
			s3x: 5,	//陕西
			jl: 5,	//吉林
			hen: 5,	//河南
			cq: 5,	//重庆
			yn: 5,	//云南
			sc: 5,	//四川
			xz: 0,	//西藏
			qh: 0,	//青海
			xj: 0,	//新疆
			tj: 5,	//天津
			nmg: 1,	//内蒙古
			bj: 9,	//北京
			sd: 7,	//山东
			heb: 5,	//河北
			ln: 6,	//辽宁
			ah: 5,	//安徽
			hk: 5,	//香港
			om: 5	//澳门
		};
		
		public var provCity:Object = {
			"北京": "北京",
			"上海": "上海",
			"天津": "天津",
			"重庆": "重庆",
			"河北": "石家庄市|邯郸市|邢台市|保定市|张家口市|承德市|廊坊市|唐山市|秦皇岛市|沧州市|衡水市",
			"山西": "太原市|大同市|阳泉市|长治市|晋城市|朔州市|吕梁市|忻州市|晋中市|临汾市|运城市",
			"辽宁": "沈阳市|大连市|鞍山市|抚顺市|本溪市|丹东市|锦州市|营口市|阜新市|辽阳市|盘锦市|铁岭市|朝阳市|葫芦岛市",
			"吉林": "长春市|吉林市|四平市|辽源市|通化市|白山市|松原市|白城市|延边市",
			"黑龙江": "哈尔滨市|齐齐哈尔市|牡丹江市|佳木斯市|大庆市|绥化市|鹤岗市|鸡西市|黑河市|双鸭山市|伊春市|七台河市|大兴安岭市",
			"江苏": "<font color='#0000ff'>南京市</font>|镇江市|苏州市|南通市|扬州市|盐城市|徐州市|连云港市|常州市|无锡市|宿迁市|泰州市|淮安市",
			"浙江": "杭州市|宁波市|温州市|嘉兴市|湖州市|绍兴市|金华市|衢州市|舟山市|台州市|丽水市",
			"安徽": "合肥市|芜湖市|蚌埠市|马鞍山市|淮北市|铜陵市|安庆市|黄山市|滁州市|宿州市|池州市|淮南市|巢湖市|阜阳市|六安市|宣城市|亳州市",
			"福建": "福州市|厦门市|莆田市|三明市|泉州市|漳州市|南平市|龙岩市|宁德市",
			"江西": "南昌市市|景德镇市|九江市|鹰潭市|萍乡市|新馀市|赣州市|吉安市|宜春市|抚州市|上饶市",
			"山东": "济南市|青岛市|淄博市|枣庄市|东营市|烟台市|潍坊市|济宁市|泰安市|威海市|日照市|莱芜市|临沂市|德州市|聊城市|滨州市|菏泽市",
			"河南": "郑州市|开封市|洛阳市|平顶山市|安阳市|鹤壁市|新乡市|焦作市|濮阳市|许昌市|漯河市|三门峡市|南阳市|商丘市|信阳市|周口市|驻马店市|济源市",
			"湖北": "武汉市|宜昌市|荆州市|襄樊市|黄石市|荆门市|黄冈市|十堰市|恩施市|潜江市|天门市|仙桃市|随州市|咸宁市|孝感市|鄂州市",
			"湖南": "长沙市|常德市|株洲市|湘潭市|衡阳市|岳阳市|邵阳市|益阳市|娄底市|怀化市|郴州市|永州市|湘西市|张家界市",
			"广东": "广州市|深圳市|珠海市|汕头市|东莞市|中山市|佛山市|韶关市|江门市|湛江市|茂名市|肇庆市|惠州市|梅州市|汕尾市|河源市|阳江市|清远市|潮州市|揭阳市|云浮市",
			"甘肃": "兰州市|嘉峪关市|金昌市|白银市|天水市|酒泉市|张掖市|武威市|定西市|陇南市|平凉市|庆阳市|临夏市|甘南市",
			"陕西": "西安市|宝鸡市|咸阳市|铜川市|渭南市|延安市|榆林市|汉中市|安康市|商洛市",
			"内蒙古": "呼和浩特市|包头市|乌海市|集宁市|通辽市|赤峰市|呼伦贝尔盟|阿拉善盟|哲里木盟|兴安盟|乌兰察布盟|锡林郭勒盟|巴彦淖尔盟|伊克昭盟",
			"广西": "南宁市|柳州市|桂林市|梧州市|北海市|防城港市|钦州市|贵港市|玉林市|南宁市|柳州市|贺州市|百色市|河池市",
			"四川": "成都市|绵阳市|德阳市|自贡市|攀枝花市|广元市|内江市|乐山市|南充市|宜宾市|广安市|达川市|雅安市|眉山市|甘孜市|凉山市|泸州市",
			"贵州": "贵阳市|六盘水市|遵义市|安顺市|铜仁市|黔西南市|毕节市|黔东南市|黔南市",
			"云南": "昆明市|大理市|曲靖市|玉溪市|昭通市|楚雄市|红河市|文山市|思茅市|西双版纳市|保山市|德宏市|丽江市|怒江市|迪庆市|临沧市",
			"西藏": "拉萨市|日喀则市|山南市|林芝市|昌都市|阿里市|那曲市",
			"海南": "海口市|三亚市",
			"宁夏": "银川市|石嘴山市|吴忠市|固原市",
			"青海": "西宁市|海东市|海南市|海北市|黄南市|玉树市|果洛市|海西市",
			"新疆": "乌鲁木齐市|石河子市|克拉玛依市|伊犁市|巴音郭勒市|昌吉市|克孜勒苏柯尔克孜市|博尔塔拉市|吐鲁番市|哈密市|喀什市|和田市|阿克苏市",
			"香港": "香港",
			"澳门": "澳门",
			"台湾": "台北市|高雄市|台中市|台南市|屏东市|南投市|云林市|新竹市|彰化市|苗栗市|嘉义市|花莲市|桃园市|宜兰市|基隆市|台东市|金门市|马祖市|澎湖市",
			"美国": "美国",
			"加拿大": "加拿大",
			"新加坡": "新加坡",
			"韩国": "韩国",
			"日本": "日本",
			"东南亚": "东南亚",
			"南美洲": "南美洲",
			"澳大利亚": "澳大利亚",
			"欧洲": "欧洲",
			"非洲": "非洲",
			"亚洲": "亚洲",
			"其它": "其它"
		};
		
		public var citiesMaxLen:Object = {
			
		};
		
		public function CNMap() {
		}
	}
}