from pydantic import BaseModel
from typing import Optional, List


class TownshipInfo:
    def __init__(self, id, township, school):
        self.id = id
        self.township = township
        self.school = school


class Login(BaseModel):
    username: str
    password: str


class RepairRecord(BaseModel):
    id: int
    record_time: str
    record_info: str
    record_user: str


class RepairInfo(BaseModel):
    id: int
    school: str
    name: str
    tel: str
    device_type: str
    repair_description: str
    start_time: str
    end_time: Optional[str]
    status: str = '未接案'
    repair_record: Optional[List[RepairRecord]]


class Member(BaseModel):
    id: int
    account: str
    password: str
    alias: str
    priority: int


township_info_array = [
    TownshipInfo(1, "九如鄉", "後庄國小"),
    TownshipInfo(2, "九如鄉", "惠農國小"),
    TownshipInfo(3, "內埔鄉", "新生國小"),
    TownshipInfo(4, "內埔鄉", "榮華國小"),
    TownshipInfo(5, "內埔鄉", "富田國小"),
    TownshipInfo(6, "內埔鄉", "佳義國小"),
    TownshipInfo(7, "牡丹鄉", "牡丹國小"),
    TownshipInfo(8, "牡丹鄉", "高士國小"),
    TownshipInfo(9, "牡丹鄉", "牡林分校"),
    TownshipInfo(10, "車城鄉", "車城國中"),
    TownshipInfo(11, "車城鄉", "車城國小"),
    TownshipInfo(12, "里港鄉", "里港國小"),
    TownshipInfo(13, "里港鄉", "土庫國小"),
    TownshipInfo(14, "里港鄉", "玉田國小"),
    TownshipInfo(15, "佳冬鄉", "佳冬國中"),
    TownshipInfo(16, "佳冬鄉", "羌園國小"),
    TownshipInfo(17, "佳冬鄉", "玉光國小"),
    TownshipInfo(18, "來義鄉", "文樂國小"),
    TownshipInfo(19, "東港鎮", "東港國中"),
    TownshipInfo(20, "東港鎮", "海濱國小"),
    TownshipInfo(21, "東港鎮", "大潭國小"),
    TownshipInfo(22, "枋山鄉", "楓港國小"),
    TownshipInfo(23, "枋寮鄉", "枋寮高中"),
    TownshipInfo(24, "枋寮鄉", "建興國小"),
    TownshipInfo(25, "枋寮鄉", "東海國小"),
    TownshipInfo(26, "林邊鄉", "林邊國中"),
    TownshipInfo(27, "林邊鄉", "仁和國小"),
    TownshipInfo(28, "林邊鄉", "崎峰國小"),
    TownshipInfo(29, "林邊鄉", "水利國小"),
    TownshipInfo(30, "長治鄉", "長興國小"),
    TownshipInfo(31, "南州鄉", "南州國中"),
    TownshipInfo(32, "南州鄉", "南州國小"),
    TownshipInfo(33, "屏東市", "大同高中"),
    TownshipInfo(34, "屏東市", "鶴聲國小"),
    TownshipInfo(35, "恆春鎮", "恆春國中"),
    TownshipInfo(36, "恆春鎮", "僑勇國小"),
    TownshipInfo(37, "恆春鎮", "大平國小"),
    TownshipInfo(38, "崁頂鄉", "崁頂國小"),
    TownshipInfo(39, "崁頂鄉", "港東國小"),
    TownshipInfo(40, "高樹鄉", "新南國小"),
    TownshipInfo(41, "新埤鄉", "新埤國中"),
    TownshipInfo(42, "新埤鄉", "新埤國小"),
    TownshipInfo(43, "新埤鄉", "大成國小"),
    TownshipInfo(44, "新園鄉", "新園國中"),
    TownshipInfo(45, "新園鄉", "仙吉國小"),
    TownshipInfo(46, "新園鄉", "瓦磘國小"),
    TownshipInfo(47, "獅子鄉", "丹路國小"),
    TownshipInfo(48, "獅子鄉", "內獅國小"),
    TownshipInfo(49, "萬丹鄉", "新庄國小"),
    TownshipInfo(50, "萬丹鄉", "新興國小"),
    TownshipInfo(51, "萬丹鄉", "興化國小"),
    TownshipInfo(52, "萬丹鄉", "竹林國小"),
    TownshipInfo(53, "萬巒鄉", "赤山國小"),
    TownshipInfo(54, "滿州鄉", "滿州國中"),
    TownshipInfo(55, "潮州鎮", "光春國中"),
    TownshipInfo(56, "霧台鄉", "霧臺國小"),
    TownshipInfo(57, "霧台鄉", "勵古百合分校"),
    TownshipInfo(58, "來義鄉", "來義高中"),
    TownshipInfo(59, "屏東市", "公正國中"),
    TownshipInfo(60, "高樹鄉", "高樹國中"),
    TownshipInfo(61, "高樹鄉", "高泰國中"),
    TownshipInfo(62, "萬巒鄉", "萬巒國中"),
    TownshipInfo(63, "內埔鄉", "內埔國中"),
    TownshipInfo(64, "瑪家鄉", "瑪家國中"),
    TownshipInfo(65, "泰武鄉", "泰武國中"),
    TownshipInfo(66, "獅子鄉", "獅子國中"),
    TownshipInfo(67, "牡丹鄉", "牡丹國中"),
    TownshipInfo(68, "屏東市", "明正國中"),
    TownshipInfo(69, "屏東市", "中正國小"),
    TownshipInfo(70, "屏東市", "仁愛國小"),
    TownshipInfo(71, "屏東市", "勝利國小"),
    TownshipInfo(72, "屏東市", "前進國小"),
    TownshipInfo(73, "屏東市", "民和國小"),
    TownshipInfo(74, "屏東市", "建國國小"),
    TownshipInfo(75, "屏東市", "信義國小"),
    TownshipInfo(76, "屏東市", "民生國小"),
    TownshipInfo(77, "潮州鎮", "光華國小"),
    TownshipInfo(78, "潮州鎮", "四林國小"),
    TownshipInfo(79, "東港鎮", "東興國小"),
    TownshipInfo(80, "恆春鎮", "恆春國小"),
    TownshipInfo(81, "恆春鎮", "大光國小"),
    TownshipInfo(82, "恆春鎮", "山海國小"),
    TownshipInfo(83, "萬丹鄉", "廣安國小"),
    TownshipInfo(84, "九如鄉", "九如國小"),
    TownshipInfo(85, "里港鄉", "載興國小"),
    TownshipInfo(86, "里港鄉", "三和國小"),
    TownshipInfo(87, "里港鄉", "塔樓國小"),
    TownshipInfo(88, "鹽埔鄉", "仕絨國小"),
    TownshipInfo(89, "鹽埔鄉", "高朗國小"),
    TownshipInfo(90, "高樹鄉", "新豐國小"),
    TownshipInfo(91, "萬巒鄉", "萬巒國小"),
    TownshipInfo(92, "內埔鄉", "東寧國小育英分校"),
    TownshipInfo(93, "內埔鄉", "僑智國小"),
    TownshipInfo(94, "內埔鄉", "崇文國小"),
    TownshipInfo(95, "內埔鄉", "黎明國小"),
    TownshipInfo(96, "竹田鄉", "大明國小"),
    TownshipInfo(97, "新埤鄉", "萬隆國小"),
    TownshipInfo(98, "枋寮鄉", "枋寮國小"),
    TownshipInfo(99, "枋寮鄉", "僑德國小"),
    TownshipInfo(100, "新園鄉", "新園國小"),
    TownshipInfo(101, "新園鄉", "烏龍國小"),
    TownshipInfo(102, "新園鄉", "港西國小"),
    TownshipInfo(103, "新園鄉", "鹽洲國小"),
    TownshipInfo(104, "崁頂鄉", "力社國小"),
    TownshipInfo(105, "林邊鄉", "林邊國小"),
    TownshipInfo(106, "佳冬鄉", "塭子國小"),
    TownshipInfo(107, "車城鄉", "車城國小溫泉分校"),
    TownshipInfo(108, "車城鄉", "車城國小射寮分校"),
    TownshipInfo(109, "三地門鄉", "地磨兒國小"),
    TownshipInfo(110, "三地門鄉", "地磨兒國小德文分校"),
    TownshipInfo(111, "三地門鄉", "賽嘉國小"),
    TownshipInfo(112, "泰武鄉", "泰武國小"),
    TownshipInfo(113, "來義鄉", "古樓國小"),
    TownshipInfo(114, "春日鄉", "古華國小士文分校"),
    TownshipInfo(115, "南州鄉", "南州國小")
]

dl_township_info_array = [
    TownshipInfo(1, "屏東市", "大同高中"),
    TownshipInfo(2, "屏東市", "明正國中"),
    TownshipInfo(3, "屏東市", "中正國中"),
    TownshipInfo(4, "屏東市", "公正國中"),
    TownshipInfo(5, "屏東市", "鶴聲國中"),
    TownshipInfo(6, "屏東市", "至正國中"),
    TownshipInfo(7, "屏東市", "陸興中學"),
    TownshipInfo(8, "長治鄉", "長治國中"),
    TownshipInfo(9, "麟洛鄉", "麟洛國中"),
    TownshipInfo(10, "九如鄉", "九如國中"),
    TownshipInfo(11, "里港鄉", "里港國中"),
    TownshipInfo(12, "鹽埔鄉", "鹽埔國中"),
    TownshipInfo(13, "高樹鄉", "高樹國中"),
    TownshipInfo(14, "高樹鄉", "高泰國中"),
    TownshipInfo(15, "內埔鄉", "內埔國中"),
    TownshipInfo(16, "內埔鄉", "崇文國中"),
    TownshipInfo(17, "內埔鄉", "美和高中"),
    TownshipInfo(18, "竹田鄉", "竹田國中"),
    TownshipInfo(19, "潮州鎮", "潮州國中"),
    TownshipInfo(20, "潮州鎮", "光春國中"),
    TownshipInfo(21, "萬巒鄉", "萬巒國中"),
    TownshipInfo(22, "新埤鄉", "新埤國中"),
    TownshipInfo(23, "萬丹鄉", "萬丹國中"),
    TownshipInfo(24, "萬丹鄉", "萬新國中"),
    TownshipInfo(25, "新園鄉", "新園國中"),
    TownshipInfo(26, "東港鎮", "東港高中"),
    TownshipInfo(27, "東港鎮", "東新國中"),
    TownshipInfo(28, "林邊鄉", "林邊國中"),
    TownshipInfo(29, "南州鄉", "南州國中"),
    TownshipInfo(30, "佳冬鄉", "佳冬國中"),
    TownshipInfo(31, "琉球鄉", "琉球國中"),
    TownshipInfo(32, "車城鄉", "車城國中"),
    TownshipInfo(33, "恆春鎮", "恆春國中"),
    TownshipInfo(34, "滿州鄉", "滿州國中"),
    TownshipInfo(35, "瑪家鄉", "瑪家國中"),
    TownshipInfo(36, "泰武鄉", "泰武國中"),
    TownshipInfo(37, "牡丹鄉", "牡丹國中"),
    TownshipInfo(38, "獅子鄉", "獅子國中"),
    TownshipInfo(39, "崁頂鄉", "南榮國中"),
    TownshipInfo(40, "枋寮鄉", "枋寮高中"),
    TownshipInfo(41, "來義鄉", "來義高中"),
    TownshipInfo(42, "九如鄉", "九如國小"),
    TownshipInfo(43, "九如鄉", "三多國小"),
    TownshipInfo(44, "九如鄉", "後庄國小"),
    TownshipInfo(45, "九如鄉", "惠農國小"),
    TownshipInfo(46, "三地門鄉", "地磨兒國小"),
    TownshipInfo(47, "三地門鄉", "地磨兒國小德文分校"),
    TownshipInfo(48, "三地門鄉", "青山國小"),
    TownshipInfo(49, "三地門鄉", "青葉國小"),
    TownshipInfo(50, "三地門鄉", "口社國小"),
    TownshipInfo(51, "三地門鄉", "賽嘉國小"),
    TownshipInfo(52, "內埔鄉", "內埔國小"),
    TownshipInfo(53, "內埔鄉", "東寧國小育英分校"),
    TownshipInfo(54, "內埔鄉", "僑智國小"),
    TownshipInfo(55, "內埔鄉", "崇文國小"),
    TownshipInfo(56, "內埔鄉", "新生國小"),
    TownshipInfo(57, "內埔鄉", "榮華國小"),
    TownshipInfo(58, "內埔鄉", "黎明國小"),
    TownshipInfo(59, "內埔鄉", "隘寮國小"),
    TownshipInfo(60, "內埔鄉", "泰安國小"),
    TownshipInfo(61, "內埔鄉", "東勢國小"),
    TownshipInfo(62, "內埔鄉", "豐田國小"),
    TownshipInfo(63, "內埔鄉", "富田國小"),
    TownshipInfo(64, "內埔鄉", "東寧國小"),
    TownshipInfo(65, "竹田鄉", "竹田國小"),
    TownshipInfo(66, "竹田鄉", "西勢國小"),
    TownshipInfo(67, "竹田鄉", "大明國小"),
    TownshipInfo(68, "牡丹鄉", "牡丹國小"),
    TownshipInfo(69, "牡丹鄉", "石門國小"),
    TownshipInfo(70, "牡丹鄉", "高士國小"),
    TownshipInfo(71, "牡丹鄉", "高士國小牡林分校"),
    TownshipInfo(72, "車城鄉", "車城國小"),
    TownshipInfo(73, "車城鄉", "車城國小射寮分校"),
    TownshipInfo(74, "車城鄉", "車城國小溫泉分校"),
    TownshipInfo(75, "里港鄉", "里港國小"),
    TownshipInfo(76, "里港鄉", "載興國小"),
    TownshipInfo(77, "里港鄉", "土庫國小"),
    TownshipInfo(78, "里港鄉", "三和國小"),
    TownshipInfo(79, "里港鄉", "塔樓國小"),
    TownshipInfo(80, "里港鄉", "玉田國小"),
    TownshipInfo(81, "佳冬鄉", "佳冬國小"),
    TownshipInfo(82, "佳冬鄉", "塭子國小"),
    TownshipInfo(83, "佳冬鄉", "羌園國小"),
    TownshipInfo(84, "佳冬鄉", "昌隆國小"),
    TownshipInfo(85, "佳冬鄉", "大新國小"),
    TownshipInfo(86, "佳冬鄉", "玉光國小"),
    TownshipInfo(87, "來義鄉", "來義國小"),
    TownshipInfo(88, "來義鄉", "望嘉國小"),
    TownshipInfo(89, "來義鄉", "文樂國小"),
    TownshipInfo(90, "來義鄉", "南和國小"),
    TownshipInfo(91, "來義鄉", "古樓國小"),
    TownshipInfo(92, "枋山鄉", "楓港國小"),
    TownshipInfo(93, "枋山鄉", "加祿國小"),
    TownshipInfo(94, "枋山鄉", "加祿國小枋山分校"),
    TownshipInfo(95, "枋寮鄉", "枋寮國小"),
    TownshipInfo(96, "枋寮鄉", "僑德國小"),
    TownshipInfo(97, "枋寮鄉", "建興國小"),
    TownshipInfo(98, "枋寮鄉", "東海國小"),
    TownshipInfo(99, "東港鎮", "東港國小"),
    TownshipInfo(100, "東港鎮", "東隆國小"),
    TownshipInfo(101, "東港鎮", "海濱國小"),
    TownshipInfo(102, "東港鎮", "以栗國小"),
    TownshipInfo(103, "東港鎮", "大潭國小"),
    TownshipInfo(104, "東港鎮", "東興國小"),
    TownshipInfo(105, "東港鎮", "東光國小"),
    TownshipInfo(106, "林邊鄉", "林邊國小"),
    TownshipInfo(107, "林邊鄉", "仁和國小"),
    TownshipInfo(108, "林邊鄉", "竹林國小"),
    TownshipInfo(109, "林邊鄉", "崎峰國小"),
    TownshipInfo(110, "林邊鄉", "水利國小"),
    TownshipInfo(111, "長治鄉", "長興國小"),
    TownshipInfo(112, "長治鄉", "繁華國小"),
    TownshipInfo(113, "長治鄉", "德協國小"),
    TownshipInfo(114, "南州鄉", "南州國小"),
    TownshipInfo(115, "南州鄉", "同安國小"),
    TownshipInfo(116, "南州鄉", "溪北國小"),
    TownshipInfo(117, "屏東市", "中正國小"),
    TownshipInfo(118, "屏東市", "仁愛國小"),
    TownshipInfo(119, "屏東市", "海豐國小"),
    TownshipInfo(120, "屏東市", "公館國小"),
    TownshipInfo(121, "屏東市", "大同國小"),
    TownshipInfo(122, "屏東市", "鶴聲國小"),
    TownshipInfo(123, "屏東市", "凌雲國小"),
    TownshipInfo(124, "屏東市", "勝利國小"),
    TownshipInfo(125, "屏東市", "歸來國小"),
    TownshipInfo(126, "屏東市", "前進國小"),
    TownshipInfo(127, "屏東市", "唐榮國小"),
    TownshipInfo(128, "屏東市", "民和國小"),
    TownshipInfo(129, "屏東市", "建國國小"),
    TownshipInfo(130, "屏東市", "復興國小"),
    TownshipInfo(131, "屏東市", "忠孝國小"),
    TownshipInfo(132, "屏東市", "和平國小"),
    TownshipInfo(133, "屏東市", "信義國小"),
    TownshipInfo(134, "屏東市", "瑞光國小"),
    TownshipInfo(135, "屏東市", "崇蘭國小"),
    TownshipInfo(136, "屏東市", "民生國小"),
    TownshipInfo(137, "恆春鎮", "恆春國小"),
    TownshipInfo(138, "恆春鎮", "恆春國小南灣分校"),
    TownshipInfo(139, "恆春鎮", "僑勇國小"),
    TownshipInfo(140, "恆春鎮", "山海國小"),
    TownshipInfo(141, "恆春鎮", "大光國小"),
    TownshipInfo(142, "恆春鎮", "水泉國小"),
    TownshipInfo(143, "恆春鎮", "水泉國小龍泉分校"),
    TownshipInfo(144, "恆春鎮", "大平國小"),
    TownshipInfo(145, "恆春鎮", "墾丁國小"),
    TownshipInfo(146, "恆春鎮", "墾丁國小鵝鑾分校"),
    TownshipInfo(147, "春日鄉", "春日國小"),
    TownshipInfo(148, "春日鄉", "力里國小"),
    TownshipInfo(149, "春日鄉", "古華國小"),
    TownshipInfo(150, "春日鄉", "古華國小士文分校"),
    TownshipInfo(151, "崁頂鄉", "崁頂國小"),
    TownshipInfo(152, "崁頂鄉", "港東國小"),
    TownshipInfo(153, "崁頂鄉", "力社國小"),
    TownshipInfo(154, "泰武鄉", "武潭國小"),
    TownshipInfo(155, "泰武鄉", "武潭國小佳平分校"),
    TownshipInfo(156, "泰武鄉", "武潭國小平和分校"),
    TownshipInfo(157, "泰武鄉", "萬安國小"),
    TownshipInfo(158, "泰武鄉", "泰武國小"),
    TownshipInfo(159, "琉球鄉", "琉球國小"),
    TownshipInfo(160, "琉球鄉", "天南國小"),
    TownshipInfo(161, "琉球鄉", "全德國小"),
    TownshipInfo(162, "琉球鄉", "白沙國小"),
    TownshipInfo(163, "高樹鄉", "高樹國小"),
    TownshipInfo(164, "高樹鄉", "舊寮國小"),
    TownshipInfo(165, "高樹鄉", "新豐國小"),
    TownshipInfo(166, "高樹鄉", "田子國小"),
    TownshipInfo(167, "高樹鄉", "新南國小"),
    TownshipInfo(168, "高樹鄉", "泰山國小"),
    TownshipInfo(169, "高樹鄉", "大路觀國小"),
    TownshipInfo(170, "高樹鄉", "大路觀國中"),
    TownshipInfo(171, "新埤鄉", "新埤國小"),
    TownshipInfo(172, "新埤鄉", "大成國小"),
    TownshipInfo(173, "新埤鄉", "萬隆國小"),
    TownshipInfo(174, "新埤鄉", "餉潭國小"),
    TownshipInfo(175, "新園鄉", "新園國小"),
    TownshipInfo(176, "新園鄉", "仙吉國小"),
    TownshipInfo(177, "新園鄉", "烏龍國小"),
    TownshipInfo(178, "新園鄉", "港西國小"),
    TownshipInfo(179, "新園鄉", "鹽洲國小"),
    TownshipInfo(180, "新園鄉", "瓦瑤國小"),
    TownshipInfo(181, "獅子鄉", "楓林國小"),
    TownshipInfo(182, "獅子鄉", "丹路國小"),
    TownshipInfo(183, "獅子鄉", "內獅國小"),
    TownshipInfo(184, "獅子鄉", "草埔國小"),
    TownshipInfo(185, "萬丹鄉", "萬丹國小"),
    TownshipInfo(186, "萬丹鄉", "萬丹國小竹林分校"),
    TownshipInfo(187, "萬丹鄉", "新庄國小"),
    TownshipInfo(188, "萬丹鄉", "興華國小"),
    TownshipInfo(189, "萬丹鄉", "新興國小"),
    TownshipInfo(190, "萬丹鄉", "社皮國小"),
    TownshipInfo(191, "萬丹鄉", "廣安國小"),
    TownshipInfo(192, "萬丹鄉", "興化國小"),
    TownshipInfo(193, "萬丹鄉", "四維國小"),
    TownshipInfo(194, "萬巒鄉", "赤山國小"),
    TownshipInfo(195, "萬巒鄉", "萬巒國小"),
    TownshipInfo(196, "萬巒鄉", "五溝國小"),
    TownshipInfo(197, "萬巒鄉", "佳佐國小"),
    TownshipInfo(198, "萬巒鄉", "佳佐國小中興分校"),
    TownshipInfo(199, "滿州鄉", "滿州國小"),
    TownshipInfo(200, "滿州鄉", "長樂國小"),
    TownshipInfo(201, "滿州鄉", "永港國小"),
    TownshipInfo(202, "瑪家鄉", "佳義國小"),
    TownshipInfo(203, "瑪家鄉", "北葉國小"),
    TownshipInfo(204, "瑪家鄉", "長榮百合國小"),
    TownshipInfo(205, "潮州鎮", "潮州國小"),
    TownshipInfo(206, "潮州鎮", "光春國小"),
    TownshipInfo(207, "潮州鎮", "光華國小"),
    TownshipInfo(208, "潮州鎮", "四林國小"),
    TownshipInfo(209, "潮州鎮", "潮南國小"),
    TownshipInfo(210, "潮州鎮", "潮東國小"),
    TownshipInfo(211, "潮州鎮", "潮昇國小"),
    TownshipInfo(212, "潮州鎮", "潮和國小"),
    TownshipInfo(213, "霧台鄉", "霧台國小"),
    TownshipInfo(214, "霧台鄉", "霧台國小勵古百合分校"),
    TownshipInfo(215, "麟洛鄉", "麟洛國小"),
    TownshipInfo(216, "鹽埔鄉", "鹽埔國小"),
    TownshipInfo(217, "鹽埔鄉", "仕絨國小"),
    TownshipInfo(218, "鹽埔鄉", "高朗國小"),
    TownshipInfo(219, "鹽埔鄉", "新圍國小"),
    TownshipInfo(220, "鹽埔鄉", "彭厝國小"),
    TownshipInfo(221, "鹽埔鄉", "振興國小"),
    TownshipInfo(222, "屏東市", "屏東女中"),
    TownshipInfo(223, "屏東市", "民生家商"),
    TownshipInfo(224, "潮州鎮", "日新工商"),
    TownshipInfo(225, "鹽埔鄉", "屏北高中"),
    TownshipInfo(226, "潮州鎮", "屏東特殊教育學校"),
    TownshipInfo(227, "屏東市", "屏東中學"),
    TownshipInfo(228, "東港鎮", "新基高中"),
    TownshipInfo(229, "屏東市", "屏東高工"),
    TownshipInfo(230, "恆春鎮", "恆春工商"),
    TownshipInfo(231, "內埔鄉", "內埔農工"),
    TownshipInfo(232, "佳冬鄉", "佳冬農校"),
    TownshipInfo(233, "屏東市", "華洲工家"),
    TownshipInfo(234, "屏東市", "屏榮高中"),
    TownshipInfo(235, "潮州鎮", "潮州高中"),
    TownshipInfo(236, "東港鎮", "東港海事")
]

aa_township_info_array = [
    TownshipInfo(1, "屏東市", "明正國中"),
    TownshipInfo(2, "屏東市", "中正國中"),
    TownshipInfo(3, "屏東市", "公正國中"),
    TownshipInfo(4, "屏東市", "鶴聲國中"),
    TownshipInfo(5, "屏東市", "至正國中"),
    TownshipInfo(6, "長治鄉", "長治國中"),
    TownshipInfo(7, "麟洛鄉", "麟洛國中"),
    TownshipInfo(8, "九如鄉", "九如國中"),
    TownshipInfo(9, "里港鄉", "里港國中"),
    TownshipInfo(10, "鹽埔鄉", "鹽埔國中"),
    TownshipInfo(11, "高樹鄉", "高樹國中"),
    TownshipInfo(12, "高樹鄉", "高泰國中"),
    TownshipInfo(13, "內埔鄉", "內埔國中"),
    TownshipInfo(14, "內埔鄉", "崇文國中"),
    TownshipInfo(15, "竹田鄉", "竹田國中"),
    TownshipInfo(16, "潮州鎮", "潮州國中"),
    TownshipInfo(17, "潮州鎮", "光春國中"),
    TownshipInfo(18, "萬巒鄉", "萬巒國中"),
    TownshipInfo(19, "新埤鄉", "新埤國中"),
    TownshipInfo(20, "萬丹鄉", "萬丹國中"),
    TownshipInfo(21, "萬丹鄉", "萬新國中"),
    TownshipInfo(22, "新園鄉", "新園國中"),
    TownshipInfo(23, "東港鎮", "東新國中"),
    TownshipInfo(24, "林邊鄉", "林邊國中"),
    TownshipInfo(25, "南州鄉", "南州國中"),
    TownshipInfo(26, "佳冬鄉", "佳冬國中"),
    TownshipInfo(27, "琉球鄉", "琉球國中"),
    TownshipInfo(28, "車城鄉", "車城國中"),
    TownshipInfo(29, "恆春鎮", "恆春國中"),
    TownshipInfo(30, "滿州鄉", "滿州國中"),
    TownshipInfo(31, "瑪家鄉", "瑪家國中"),
    TownshipInfo(32, "泰武鄉", "泰武國中"),
    TownshipInfo(33, "牡丹鄉", "牡丹國中"),
    TownshipInfo(34, "獅子鄉", "獅子國中"),
    TownshipInfo(35, "九如鄉", "九如國小"),
    TownshipInfo(36, "九如鄉", "三多國小"),
    TownshipInfo(37, "九如鄉", "後庄國小"),
    TownshipInfo(38, "九如鄉", "惠農國小"),
    TownshipInfo(39, "三地門", "地磨兒國小"),
    TownshipInfo(40, "三地門", "地磨兒國小德文分校"),
    TownshipInfo(41, "三地門", "青山國小"),
    TownshipInfo(42, "三地門", "青葉國小"),
    TownshipInfo(43, "三地門", "口社國小"),
    TownshipInfo(44, "三地門", "賽嘉國小"),
    TownshipInfo(45, "內埔鄉", "內埔國小"),
    TownshipInfo(46, "內埔鄉", "東寧國小育英分校"),
    TownshipInfo(47, "內埔鄉", "僑智國小"),
    TownshipInfo(48, "內埔鄉", "崇文國小"),
    TownshipInfo(49, "內埔鄉", "新生國小"),
    TownshipInfo(50, "內埔鄉", "榮華國小"),
    TownshipInfo(51, "內埔鄉", "黎明國小"),
    TownshipInfo(52, "內埔鄉", "隘寮國小"),
    TownshipInfo(53, "內埔鄉", "泰安國小"),
    TownshipInfo(54, "內埔鄉", "東勢國小"),
    TownshipInfo(55, "內埔鄉", "豐田國小"),
    TownshipInfo(56, "內埔鄉", "富田國小"),
    TownshipInfo(57, "內埔鄉", "東寧國小"),
    TownshipInfo(58, "竹田鄉", "竹田國小"),
    TownshipInfo(59, "竹田鄉", "西勢國小"),
    TownshipInfo(60, "竹田鄉", "大明國小"),
    TownshipInfo(61, "牡丹鄉", "牡丹國小"),
    TownshipInfo(62, "牡丹鄉", "石門國小"),
    TownshipInfo(63, "牡丹鄉", "高士國小"),
    TownshipInfo(64, "牡丹鄉", "高士國小牡林分校"),
    TownshipInfo(65, "車城鄉", "車城國小"),
    TownshipInfo(66, "車城鄉", "車城國小射寮分校"),
    TownshipInfo(67, "車城鄉", "車城國小溫泉分校"),
    TownshipInfo(68, "里港鄉", "里港國小"),
    TownshipInfo(69, "里港鄉", "載興國小"),
    TownshipInfo(70, "里港鄉", "土庫國小"),
    TownshipInfo(71, "里港鄉", "三和國小"),
    TownshipInfo(72, "里港鄉", "塔樓國小"),
    TownshipInfo(73, "里港鄉", "玉田國小"),
    TownshipInfo(74, "佳冬鄉", "佳冬國小"),
    TownshipInfo(75, "佳冬鄉", "塭子國小"),
    TownshipInfo(76, "佳冬鄉", "羌園國小"),
    TownshipInfo(77, "佳冬鄉", "昌隆國小"),
    TownshipInfo(78, "佳冬鄉", "玉光國小"),
    TownshipInfo(79, "來義鄉", "來義國小"),
    TownshipInfo(80, "來義鄉", "望嘉國小"),
    TownshipInfo(81, "來義鄉", "文樂國小"),
    TownshipInfo(82, "來義鄉", "南和國小"),
    TownshipInfo(83, "來義鄉", "古樓國小"),
    TownshipInfo(84, "枋山鄉", "楓港國小"),
    TownshipInfo(85, "枋山鄉", "加祿國小"),
    TownshipInfo(86, "枋山鄉", "加祿國小枋山分校"),
    TownshipInfo(87, "枋寮鄉", "枋寮國小"),
    TownshipInfo(88, "枋寮鄉", "僑德國小"),
    TownshipInfo(89, "枋寮鄉", "建興國小"),
    TownshipInfo(90, "枋寮鄉", "東海國小"),
    TownshipInfo(91, "東港鎮", "東港國小"),
    TownshipInfo(92, "東港鎮", "東隆國小"),
    TownshipInfo(93, "東港鎮", "海濱國小"),
    TownshipInfo(94, "東港鎮", "以栗國小"),
    TownshipInfo(95, "東港鎮", "大潭國小"),
    TownshipInfo(96, "東港鎮", "東興國小"),
    TownshipInfo(97, "東港鎮", "東光國小"),
    TownshipInfo(98, "林邊鄉", "林邊國小"),
    TownshipInfo(99, "林邊鄉", "仁和國小"),
    TownshipInfo(100, "林邊鄉", "竹林國小"),
    TownshipInfo(101, "林邊鄉", "崎峰國小"),
    TownshipInfo(102, "林邊鄉", "水利國小"),
    TownshipInfo(103, "長治鄉", "長興國小"),
    TownshipInfo(104, "長治鄉", "繁華國小"),
    TownshipInfo(105, "長治鄉", "德協國小"),
    TownshipInfo(106, "南州鄉", "南州國小"),
    TownshipInfo(107, "南州鄉", "同安國小"),
    TownshipInfo(108, "南州鄉", "溪北國小"),
    TownshipInfo(109, "屏東市", "中正國小"),
    TownshipInfo(110, "屏東市", "仁愛國小"),
    TownshipInfo(111, "屏東市", "海豐國小"),
    TownshipInfo(112, "屏東市", "公館國小"),
    TownshipInfo(113, "屏東市", "大同國小"),
    TownshipInfo(114, "屏東市", "鶴聲國小"),
    TownshipInfo(115, "屏東市", "凌雲國小"),
    TownshipInfo(116, "屏東市", "勝利國小"),
    TownshipInfo(117, "屏東市", "歸來國小"),
    TownshipInfo(118, "屏東市", "前進國小"),
    TownshipInfo(119, "屏東市", "唐榮國小"),
    TownshipInfo(120, "屏東市", "民和國小"),
    TownshipInfo(121, "屏東市", "建國國小"),
    TownshipInfo(122, "屏東市", "復興國小"),
    TownshipInfo(123, "屏東市", "忠孝國小"),
    TownshipInfo(124, "屏東市", "和平國小"),
    TownshipInfo(125, "屏東市", "信義國小"),
    TownshipInfo(126, "屏東市", "瑞光國小"),
    TownshipInfo(127, "屏東市", "崇蘭國小"),
    TownshipInfo(128, "屏東市", "民生國小"),
    TownshipInfo(129, "恆春鎮", "恆春國小"),
    TownshipInfo(130, "恆春鎮", "恆春國小南灣分校"),
    TownshipInfo(131, "恆春鎮", "僑勇國小"),
    TownshipInfo(132, "恆春鎮", "山海國小"),
    TownshipInfo(133, "恆春鎮", "大光國小"),
    TownshipInfo(134, "恆春鎮", "水泉國小"),
    TownshipInfo(135, "恆春鎮", "水泉國小龍泉分校"),
    TownshipInfo(136, "恆春鎮", "大平國小"),
    TownshipInfo(137, "恆春鎮", "墾丁國小"),
    TownshipInfo(138, "恆春鎮", "墾丁國小鵝鑾分校"),
    TownshipInfo(139, "春日鄉", "春日國小"),
    TownshipInfo(140, "春日鄉", "力里國小"),
    TownshipInfo(141, "春日鄉", "古華國小"),
    TownshipInfo(142, "春日鄉", "古華國小士文分校"),
    TownshipInfo(143, "崁頂鄉", "崁頂國小"),
    TownshipInfo(144, "崁頂鄉", "港東國小"),
    TownshipInfo(145, "崁頂鄉", "力社國小"),
    TownshipInfo(146, "泰武鄉", "武潭國小"),
    TownshipInfo(147, "泰武鄉", "武潭國小佳平分校"),
    TownshipInfo(148, "泰武鄉", "武潭國小平和分校"),
    TownshipInfo(149, "泰武鄉", "萬安國小"),
    TownshipInfo(150, "泰武鄉", "泰武國小"),
    TownshipInfo(151, "琉球鄉", "琉球國小"),
    TownshipInfo(152, "琉球鄉", "天南國小"),
    TownshipInfo(153, "琉球鄉", "全德國小"),
    TownshipInfo(154, "琉球鄉", "白沙國小"),
    TownshipInfo(155, "高樹鄉", "高樹國小"),
    TownshipInfo(156, "高樹鄉", "舊寮國小"),
    TownshipInfo(157, "高樹鄉", "新豐國小"),
    TownshipInfo(158, "高樹鄉", "田子國小"),
    TownshipInfo(159, "高樹鄉", "新南國小"),
    TownshipInfo(160, "高樹鄉", "泰山國小"),
    TownshipInfo(161, "高樹鄉", "大路關國小"),
    TownshipInfo(162, "高樹鄉", "大路關國中"),
    TownshipInfo(163, "新埤鄉", "新埤國小"),
    TownshipInfo(164, "新埤鄉", "大成國小"),
    TownshipInfo(165, "新埤鄉", "萬隆國小"),
    TownshipInfo(166, "新埤鄉", "餉潭國小"),
    TownshipInfo(167, "新園鄉", "新園國小"),
    TownshipInfo(168, "新園鄉", "仙吉國小"),
    TownshipInfo(169, "新園鄉", "烏龍國小"),
    TownshipInfo(170, "新園鄉", "港西國小"),
    TownshipInfo(171, "新園鄉", "鹽洲國小"),
    TownshipInfo(172, "新園鄉", "瓦瑤國小"),
    TownshipInfo(173, "獅子鄉", "楓林國小"),
    TownshipInfo(174, "獅子鄉", "丹路國小"),
    TownshipInfo(175, "獅子鄉", "內獅國小"),
    TownshipInfo(176, "獅子鄉", "草埔國小"),
    TownshipInfo(177, "萬丹鄉", "萬丹國小"),
    TownshipInfo(178, "萬丹鄉", "萬丹國小竹林分校"),
    TownshipInfo(179, "萬丹鄉", "新庄國小"),
    TownshipInfo(180, "萬丹鄉", "興華國小"),
    TownshipInfo(181, "萬丹鄉", "新興國小"),
    TownshipInfo(182, "萬丹鄉", "社皮國小"),
    TownshipInfo(183, "萬丹鄉", "廣安國小"),
    TownshipInfo(184, "萬丹鄉", "興化國小"),
    TownshipInfo(185, "萬丹鄉", "四維國小"),
    TownshipInfo(186, "萬巒鄉", "赤山國小"),
    TownshipInfo(187, "萬巒鄉", "萬巒國小"),
    TownshipInfo(188, "萬巒鄉", "五溝國小"),
    TownshipInfo(189, "萬巒鄉", "佳佐國小"),
    TownshipInfo(190, "萬巒鄉", "佳佐國小中興分校"),
    TownshipInfo(191, "滿州鄉", "滿州國小"),
    TownshipInfo(192, "滿州鄉", "長樂國小"),
    TownshipInfo(193, "滿州鄉", "永港國小"),
    TownshipInfo(194, "瑪家鄉", "佳義國小"),
    TownshipInfo(195, "瑪家鄉", "北葉國小"),
    TownshipInfo(196, "瑪家鄉", "長榮百合國小"),
    TownshipInfo(197, "潮州鎮", "潮州國小"),
    TownshipInfo(198, "潮州鎮", "光春國小"),
    TownshipInfo(199, "潮州鎮", "光華國小"),
    TownshipInfo(200, "潮州鎮", "四林國小"),
    TownshipInfo(201, "潮州鎮", "潮南國小"),
    TownshipInfo(202, "潮州鎮", "潮東國小"),
    TownshipInfo(203, "潮州鎮", "潮昇國小"),
    TownshipInfo(204, "潮州鎮", "潮和國小"),
    TownshipInfo(205, "霧台鄉", "霧台國小"),
    TownshipInfo(206, "霧台鄉", "霧台國小勵古百合分校"),
    TownshipInfo(207, "麟洛鄉", "麟洛國小"),
    TownshipInfo(208, "鹽埔鄉", "鹽埔國小"),
    TownshipInfo(209, "鹽埔鄉", "仕絨國小"),
    TownshipInfo(210, "鹽埔鄉", "高朗國小"),
    TownshipInfo(211, "鹽埔鄉", "新圍國小"),
    TownshipInfo(212, "鹽埔鄉", "彭厝國小"),
    TownshipInfo(213, "鹽埔鄉", "振興國小"),
    TownshipInfo(214, "屏東市", "大同高中-國中部"),
    TownshipInfo(215, "東港鎮", "東港高中-國中部"),
    TownshipInfo(216, "枋寮鄉", "枋寮高中-國中部"),
    TownshipInfo(217, "來義鄉", "來義高中-國中部"),
    TownshipInfo(218, "崁頂鄉", "南榮國中"),
    TownshipInfo(219, "屏東市", "教師研習中心"),
    TownshipInfo(220, "屏東市", "資教中心")
]

hpps_township_info_array = [
    TownshipInfo(1, "屏東市", "鶴聲國中"),
    TownshipInfo(2, "長治鄉", "長治國中 "),
    TownshipInfo(3, "麟洛鄉", "麟洛國中"),
    TownshipInfo(4, "里港鄉", "里港國中"),
    TownshipInfo(5, "鹽埔鄉", "鹽埔國中"),
    TownshipInfo(6, "竹田鄉", "竹田國中"),
    TownshipInfo(7, "潮州鎮", "潮州國中"),
    TownshipInfo(8, "屏東市", "海豐國小"),
    TownshipInfo(9, "屏東市", "復興國小"),
    TownshipInfo(10, "屏東市", "忠孝國小"),
    TownshipInfo(11, "屏東市", "和平國小"),
    TownshipInfo(12, "屏東市", "瑞光國小"),
    TownshipInfo(13, "屏東市", "崇蘭國小"),
    TownshipInfo(14, "潮州鎮", "潮昇國小"),
    TownshipInfo(15, "潮州鎮", "潮和國小"),
    TownshipInfo(16, "東港鎮", "以栗國小"),
    TownshipInfo(17, "崁頂鄉", "南灣分校"),
    TownshipInfo(18, "恆春鎮", "墾丁國小"),
    TownshipInfo(19, "高樹鄉", "鵝鑾分校"),
    TownshipInfo(20, "萬丹鄉", "興華國小"),
    TownshipInfo(21, "萬丹鄉", "社皮國小"),
    TownshipInfo(22, "萬丹鄉", "四維國小"),
    TownshipInfo(23, "長治鄉", "繁華國小"),
    TownshipInfo(24, "長治鄉", "德協國小"),
    TownshipInfo(25, "麟洛鄉", "麟洛國小"),
    TownshipInfo(26, "九如鄉", "三多國小"),
    TownshipInfo(27, "鹽埔鄉", "新圍國小"),
    TownshipInfo(28, "鹽埔鄉", "彭厝國小"),
    TownshipInfo(29, "高樹鄉", "高樹國小"),
    TownshipInfo(30, "高樹鄉", "大路關國中小(國小部)"),
    TownshipInfo(31, "萬巒鄉", "五溝國小"),
    TownshipInfo(32, "萬巒鄉", "佳佐國小"),
    TownshipInfo(33, "屏東市", "中興分校"),
    TownshipInfo(34, "內埔鄉", "泰安國小"),
    TownshipInfo(35, "內埔鄉", "東勢國小"),
    TownshipInfo(36, "內埔鄉", "隘寮國小"),
    TownshipInfo(37, "南州鄉", "溪北國小"),
    TownshipInfo(38, "滿州鄉", "長樂國小"),
    TownshipInfo(39, "滿州鄉", "永港國小"),
    TownshipInfo(40, "三地門鄉", "青山國小"),
    TownshipInfo(41, "三地門鄉", "青葉國小"),
    TownshipInfo(42, "來義鄉", "來義國小"),
    TownshipInfo(43, "來義鄉", "南和國小"),
    TownshipInfo(44, "春日鄉", "力里國小"),
    TownshipInfo(45, "潮州鎮", "潮南國小"),
    TownshipInfo(46, "潮州鎮", "潮東國小"),
    TownshipInfo(47, "高樹鄉", "舊寮國小"),
    TownshipInfo(48, "竹田鄉", "竹田國小"),
    TownshipInfo(49, "竹田鄉", "西勢國小"),
    TownshipInfo(50, "新埤鄉", "餉潭國小"),
    TownshipInfo(51, "泰武鄉", "萬安國小"),
    TownshipInfo(52, "春日鄉", "古華國小"),
    TownshipInfo(53, "屏東市", "明正國中"),
    TownshipInfo(54, "滿州鄉", "滿州國小"),
]
