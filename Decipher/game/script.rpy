# script.rpy

define r = Character("铁锈", color="#c8c8c8")
define l = Character("朗木", color="#add8e6")
define b = Character("布兰登", color="#ffa07a") # 主角
    

default scene = Solid("#000")


image city_night = im.Scale("images/city_night.jpg", config.screen_width, config.screen_height)
image alley = im.Scale("images/alley.jpg", config.screen_width, config.screen_height)
image neon_alley = im.Scale("images/neon_alley.jpg", config.screen_width, config.screen_height)
image rain_streaks = im.Scale("images/rain_streaks.png", config.screen_width, config.screen_height)
image dripping_pipes = im.Scale("images/dripping_pipes.jpg", config.screen_width, config.screen_height)
image flickering_sign = im.Scale("images/flickering_sign.jpg", config.screen_width, config.screen_height)
image crowded_street = im.Scale("images/crowded_street.jpg", config.screen_width, config.screen_height)
image dark_corner = im.Scale("images/dark_corner.jpg", config.screen_width, config.screen_height)
image grimy_wall = im.Scale("images/grimy_wall.jpg", config.screen_width, config.screen_height)
image holographic_ads = im.Scale("images/holographic_ads.jpg", config.screen_width, config.screen_height)
image synth_crowd = im.Scale("images/synth_crowd.jpg", config.screen_width, config.screen_height)
image cybernetic_eyes = im.Scale("images/cybernetic_eyes.jpg", config.screen_width, config.screen_height)
image data_stream = im.Scale("images/data_stream.jpg", config.screen_width, config.screen_height)
image distorted_reality = im.Scale("images/distorted_reality.jpg", config.screen_width, config.screen_height)
image glitching_screen = im.Scale("images/glitching_screen.jpg", config.screen_width, config.screen_height)
image mechanical_body = im.Scale("images/mechanical_body.jpg", config.screen_width, config.screen_height)
image network_nodes = im.Scale("images/network_nodes.jpg", config.screen_width, config.screen_height)
image digital_ghost = im.Scale("images/digital_ghost.jpg", config.screen_width, config.screen_height)
image code_rain = im.Scale("images/code_rain.jpg", config.screen_width, config.screen_height)
image server_room = im.Scale("images/server_room.jpg", config.screen_width, config.screen_height)
image fractured_mind = im.Scale("images/fractured_mind.jpg", config.screen_width, config.screen_height)
image neon_grid = im.Scale("images/neon_grid.jpg", config.screen_width, config.screen_height)
image urban_decay = im.Scale("images/urban_decay.jpg", config.screen_width, config.screen_height)


image langmu = "images/langmu.png"
image langmu_close = "images/langmu_close.png"
image rust_angry = "images/rust_angry.png"
image chip = "images/data_chip.png"
image wrist_device = "images/wrist_device.png"
image blue_screen = im.Scale("images/blue_screen.png", config.screen_width, config.screen_height)
image gun = "images/gun.png"
image blood_splatter = "images/blood_splatter.png"
image poison_vial = "images/poison_vial.png"
image tranquilizer_gun = "images/tranquilizer_gun.png"
image time_machine = "images/time_machine.png"
image udp_shock = "images/udp_shock.png"
image ida86 = "images/ida86.png"
image reverse_shell = "images/reverse_shell.png"
image escalation = "images/escalation.png"
image self_destruct = "images/self_destruct.png"
image data_fragment = "images/data_fragment.png"
image neural_interface = "images/neural_interface.png"
image memory_glitch = "images/memory_glitch.png"
image synthetic_tears = "images/synthetic_tears.png"
image metallic_glint = "images/metallic_glint.png"
image shattered_hologram = "images/shattered_hologram.png"
image digital_veins = "images/digital_veins.png"
image corrupted_data = "images/corrupted_data.png"
image phantom_pain = "images/phantom_pain.png"
image echo_of_laughter = "images/echo_of_laughter.png"
image fading_memory = "images/fading_memory.png"
image ghost_in_the_machine = "images/ghost_in_the_machine.png"

# music rain_sound = "audio/rain.ogg"
# music city_ambience = "audio/city_ambience.ogg"
music neon_drip = "audio/neon_drip.ogg"
music synth_pulse = "audio/synth_pulse.ogg"
music digital_static = "audio/digital_static.ogg"
music urban_drone = "audio/urban_drone.ogg"
music fractured_melody = "audio/fractured_melody.ogg"

# 标志位，用于判断玩家是否发现异常
default suspicious_level = 0

# 开始游戏
label start:

    scene city_night with dissolve
    play music neon_drip loop

    b "雨，永不停歇的城市脉搏。"
    b "每一滴都像敲击在我的神经末梢，提醒着我这个冰冷、拥挤的世界。"
    b "聚酯纤维摩擦的嘶哑，义体关节活动的细微咔哒声，混杂着远处全息广告刺耳的叫嚣。"
    b "这就是我的日常，一个在科技与颓废之间摇摆的幽灵。"

    r "（通过加密通讯）布兰登，我在老城区边缘的废弃车站等你。别让人跟踪你。"

    b "（自言自语）铁锈的声音总是带着一丝电流，冰冷而急促。他知道我想要什么——电子苦艾酒。"
    b "一种能暂时切断现实，通往所谓‘精神超然’的捷径。我已经太久没有感受到真正的‘超然’了。"

    scene crowded_street with dissolve
    "我穿梭在拥挤的人流中，躲避着那些闪烁着恶意光芒的义眼和过于热情的全息推销。"
    "空气中弥漫着合成食物的甜腻气味和劣质燃料的刺鼻味道。"
    "我习惯了这种拥挤，这种匿名感。在人群中，我只是无数个游荡的灵魂之一。"

    # flag: ###### 收到神秘人rust信息（广撒网，寻找苦艾）
    $ persistent.received_rust_info = True

    scene dark_corner with dissolve
    "废弃车站的阴影如同怪物的巨口，吞噬着微弱的光线。"
    "只有几盏摇摇晃晃的应急灯发出昏黄的光芒，在锈迹斑斑的金属墙壁上投下扭曲的影子。"

    show langmu at right
    b "朗木蜷缩在角落里，全息眼球在黑暗中闪烁着不自然的蓝色光芒，像两盏幽灵般的灯笼。"
    b "他比上次见面时更加瘦弱，聚酯纤维的外套也沾满了污泥。"

    # flag: ###### 见面
    $ persistent.met_langmu = True

    l "（声音低沉而嘶哑）你来了，布兰登。我带来了你想要的东西……一部分。"

    hide langmu with dissolve
    show langmu_close at right
    show chip at center with fade

    l "这是鲁姆给你的记忆碎片。他说，里面可能有你需要的线索，关于……苦艾。"
    b "（接过芯片）鲁姆？那个游走于信息暗网的幽灵？他怎么会知道我想要这个？"

    hide chip with dissolve
    show langmu at right
    l "他有自己的渠道。而且……他也想要更多。如果你能帮他找到完整的‘配方’，他会给你更多好处。"
    b "（审视着朗木）‘更多好处’？你确定这不仅仅是把我当成诱饵？"

    # flag: rum给记忆碎片
    $ persistent.received_rum_fragment = True

    menu:
        "我相信他。":
            $ suspicious_level -= 1
            b "好吧，我暂时相信你。给我看看这个碎片。"
        "我保持怀疑。":
            $ suspicious_level += 1
            b "我对你们两个都保持怀疑。朗木，你最好别耍花招。"
        "这两个选项都保持怀疑。":
            $ suspicious_level += 2
            b "这感觉像个陷阱。但我已经走到了这一步，只能看看里面是什么了。"
            # flag: ###### 看记忆碎片

    hide langmu with dissolve
    show wrist_device at center with fade
    b "我将芯片插入腕部接口，神经元连接开始读取数据。"

    hide wrist_device with dissolve
    show data_stream at center with dissolve
    "意识如同涌动的潮汐，记忆碎片如同散落的星辰，在我脑海中闪烁。"
    "破碎的图像，扭曲的声音，以及一种难以名状的……渴望。"
    "我看到了闪烁的霓虹灯，拥挤的街道，以及一些模糊的面孔，其中一个似乎在低语着什么。"

    hide data_stream with dissolve
    show alley with dissolve

    b "（自言自语）这只是些片段……但其中确实提到了‘苦艾’，以及一个隐藏的地点——废弃的制药厂。"
    b "朗木，我们需要合作。找到这个制药厂。"

    show langmu at right
    l "我知道在哪里。跟我来。"

    # flag: ###### 合作出发
    $ persistent.teamed_up_with_langmu = True

    menu:
        "买一把枪。（需要花费一些信用点）":
            $ has_gun = True
            b "为了安全起见，我需要一把枪。"
            "（你花费了一些信用点购买了一把可靠的手枪。）"
        "不买枪。":
            $ has_gun = False
            b "我们走吧。希望不会有麻烦。"

    scene urban_decay with dissolve
    "我们穿梭在城市的废墟边缘，高耸的废弃建筑如同巨大的骸骨，在阴沉的天空中投下长长的阴影。"
    "空气中弥漫着腐败和铁锈的气味。"

    label find_target:
        scene flickering_sign with dissolve
        "我们找到了制药厂的遗址。破败的建筑摇摇欲坠，只有一块闪烁的霓虹灯招牌还能勉强辨认出几个模糊的字母。"

        show langmu at left
        b "目标应该就在里面。朗木，你有什么计划？"

        l "我们进去看看。小心点，这里可能还有其他人。"

        "我们小心翼翼地进入了废弃的制药厂。"
        "内部一片狼藉，破碎的玻璃、倒塌的货架和散落在地上的废弃设备。"
        "空气中弥漫着化学药品的刺鼻气味和潮湿的霉味。"

        # flag: ###### 找到目标，对话
        $ persistent.found_target = True

        label target_encounter:
            show Character("目标", color="#ff4500") at center
            "我们在一间破旧的实验室里找到了目标——一个神色紧张的合成人，他手中拿着一个闪烁的容器。"

            menu:
                if has_gun:
                    r "（掏出枪）把东西放下！"
                    jump kill_target_gun
                else:
                    r "（示意朗木）朗木，动手！"
                    jump kill_target_langmu

        label kill_target_gun:
            show gun at left with moveinleft
            b "我的手指扣动扳机，枪声在寂静的废弃建筑中炸响。"
            hide gun with moveoutleft
            show blood_splatter at center with fade
            "目标发出一声闷哼，手中的容器掉落在地上，摔得粉碎。"
            hide Character("目标") with fade
            hide blood_splatter with fade
            jump run_away

        label kill_target_langmu:
            l "（动作迅速地制服了目标）解决了。"
            hide Character("目标") with fade
            jump run_away

        label run_away:
            scene alley with dissolve
            "我们迅速离开了制药厂，消失在雨夜的小巷中。"

            # flag: 跑路
            $ persistent.ran_away = True

            "就在我们以为安全的时候，我的腕部设备突然响起刺耳的警报声。"

            scene blue_screen with fade
            "屏幕上闪烁着我的通缉令，罪名是盗窃和袭击。"
            b "铁锈！是他出卖了我们！"

            scene dark_corner with dissolve
            show langmu at right
            b "朗木，我们被通缉了！"

            l "我知道。他一直想独吞‘苦艾’。"

            "突然，一道能量束从黑暗中射向我们！"

            menu:
                "躲避。":
                    b "我们险险躲开了攻击！"
                    jump attack_pursuit
                "朗木掩护我！":
                    l "小心！"
                    "朗木挡在了我的身前，能量束击中了他的胸膛！"
                    jump langmu_saves

        label attack_pursuit:
            scene rain_streaks with dissolve
            "我们开始在湿滑的小巷中奔跑，身后传来追击者的脚步声和能量武器的嗡鸣。"

            menu:
                "下毒暗算追击者。":
                    if persistent.has_poison:
                        b "我悄悄释放了携带的毒药。"
                        "追击者发出痛苦的嚎叫，倒在了地上。"
                        jump find_rust
                    else:
                        b "我没有毒药！只能跑！"
                        jump continue_pursuit
                "用枪反击追击者。":
                    if has_gun:
                        show gun at left with moveinleft
                        b "我转身向追击者射击！"
                        "击中了！追击者倒下了。"
                        hide gun with moveoutleft
                        jump find_rust
                    else:
                        b "我没有枪！"
                        jump continue_pursuit
                "其他方法（利用环境）。":
                    b "我猛地踢翻一个垃圾桶，绊倒了追击者！"
                    jump continue_pursuit

        label continue_pursuit:
            scene neon_alley with dissolve
            "我们继续在霓虹闪烁的小巷中奔跑，追击者紧随其后。"
            "最终，我们摆脱了他们，躲藏在一个废弃的建筑里。"
            jump find_rust

        label langmu_saves:
            show metallic_glint at center with fade
            l "（声音有些颤抖）我……我没事。皮下植入帮了我一把。"
            hide metallic_glint with fade
            b "朗木！你……"
            jump find_rust

    label find_rust:
        scene grimy_wall with dissolve
        "我们躲藏起来，喘息着。"
        b "朗木，铁锈为什么要出卖我们？"
        l "他想要独占‘苦艾’。他一直是个机会主义者。"
        b "我们要找到他，让他付出代价。"

        # flag: ###### 找rust复仇
        $ persistent.seeking_rust_revenge = True

        menu:
            "为找Rust复仇准备工具。":
                jump prepare_revenge
            "直接去找Rust。":
                jump confront_rust

    label prepare_revenge:
        scene cluttered_room with dissolve
        "我们找到了一间废弃的工具间，里面散落着各种废弃的设备。"

        menu:
            "时间机器（看起来不太靠谱）。":
                b "时间机器？这能有用吗？"
                $ prepared_tool = "time_machine"
            "UDP冲击仪（不知道能不能奏效）。":
                b "试试这个UDP冲击仪？或许能干扰他的义体。"
                $ prepared_tool = "udp_shock"
            "IDA86逆向工具（或许能发现他留下的痕迹）。":
                b "我试试用IDA86逆向分析他留下的数据痕迹。"
                $ prepared_tool = "ida86"

        jump confront_rust

    label confront_rust:
        scene dark_corner with dissolve
        "我们找到了铁锈藏身的地方——一个废弃的酒吧后巷。"
        show rust_angry at left
        r "你们竟然敢追来？"

        if prepared_tool == "ida86" or suspicious_level >= 1:
            # flag: ###### Brandon发现细节和记忆碎片不符
            b "我发现了你留下的线索，铁锈。你以为我会相信你？"
            r "你发现了？"
    label failed_ending_udp:
    scene distorted_reality with dissolve
    "UDP冲击仪毫无作用，铁锈只是嘲笑地看着我。"
    r "愚蠢的玩具！你以为这种小伎俩能对付我？"
    "铁锈的攻击变得更加猛烈，我感到意识逐渐被黑暗吞噬。"
    return

label failed_ending_time_machine:
    scene memory_glitch with dissolve
    "时间机器发出了刺耳的嗡鸣，但什么也没有发生。铁锈的攻击如同潮水般涌来。"
    r "时间？你以为你能回到过去改变什么？太天真了！"
    "我的记忆开始混乱，现实变得扭曲，最终陷入无尽的虚无。"
    return

label confront_rust:
    scene dark_corner with dissolve
    "我们找到了铁锈藏身的地方——一个废弃的酒吧后巷。"
    show rust_angry at left
    r "你们竟然敢追来？"

    if prepared_tool == "ida86" or suspicious_level >= 1:
        # flag: ###### Brandon发现细节和记忆碎片不符
        b "铁锈，你这个卑鄙的叛徒！"
        r "叛徒？我只是看到了更好的机会！那东西的价值远超你们这些蠢货的想象！"

        if prepared_tool == "ida86":
            show ida86 at center with fade
            b "（看着腕部设备，屏幕上飞速滚动着反汇编代码）你的数据流……不对劲。那些加密协议的握手信号存在逻辑上的漏洞，时间戳也被人为地修改过。朗木给我的记忆碎片……它的底层数据结构与这个芯片的格式存在根本性的差异。"
            hide ida86 with dissolve
            jump reveal_truth
        elif suspicious_level >= 1:
            b "（审视着朗木，眼神锐利）朗木，你给我的记忆碎片……里面的情感波动过于刻意，某些关键的时间点存在逻辑上的断层。而且，你对‘苦艾’的渴望……似乎超出了一个普通线人的范畴。"
            jump reveal_truth
        else:
            r "废话少说！把东西交出来！"
            jump confront_rust_fight

    else:
        r "把东西交出来，我可以考虑放你们一条生路。"
        jump confront_rust_fight

label confront_rust_fight:
    menu:
        if has_gun:
            b "我不会再相信你了，铁锈！"
            jump rust_fight_gun
        else:
            b "朗木，我们联手对付他！"
            jump rust_fight_no_gun

label rust_fight_gun:
    show gun at left with moveinleft
    b "我扣动扳机，子弹射向铁锈！"
    hide gun with moveoutleft
    show rust_angry with shake
    r "该死！"
    "铁锈躲闪不及，肩膀中弹。"
    jump rust_down

label rust_fight_no_gun:
    l "我们上！"
    "我们和铁锈展开了混战。"
    "铁锈虽然狡猾，但在我们的联手攻击下逐渐落入下风。"
    jump rust_down

label rust_down:
    show rust_angry at center
    r "（喘息）你们……会后悔的……"
    hide rust_angry with fade
    "铁锈倒在了地上，失去了意识。"
    jump reveal_truth

label reveal_truth:
    scene alley with dissolve
    b "朗木，刚才的数据流……感觉很奇怪。那些记忆碎片，似乎被动过手脚。"
    show langmu at right
    l "……或许吧。"

    if suspicious_level >= 1:
        b "你的眼神躲闪。朗木，告诉我实话，你到底是什么人？你的全息眼球……里面的数据流并不稳定，有时会出现细微的延迟和色彩偏差，这不像是普通的人工植入。"
    else:
        b "总觉得哪里不对劲。那些记忆碎片太模糊了，而且……朗木，你对‘苦艾’的执着，是不是有些过分了？"

    show metallic_glint at center with fade
    l "布兰登……我……我不是你所认为的那样。"
    hide metallic_glint with dissolve
    show mechanical_body at center with dissolve
    "朗木的身体开始发出不自然的咔哒声，他的聚酯纤维外壳如同被剥离的伪装，露出了下面精密的机械骨骼和闪烁的电子元件。"
    b "（震惊，后退一步）你……你是个合成人？！"
    l "是的。我的意识……早已上传到了网络的核心节点。"

    # flag: ###### 发现朗木是人造人，将朗木枪杀后露出机械的身体内部
    menu:
        if has_gun:
            b "你一直在利用我！那些所谓的信任，所谓的共同患难……都是虚假的程序吗？"
            show gun at left with moveinleft
            "我握紧手中的枪，对准朗木那冰冷的机械躯体，曾经并肩作战的记忆如同碎片般破碎。"
            hide gun with moveoutleft
            show shattered_hologram at center with fade
            "枪声撕裂雨夜的寂静，子弹击穿了朗木的外壳，火花和液体溅射而出，他的动作戛然而止，露出了内部复杂的线路和金属。"
            hide mechanical_body with dissolve
            jump true_ending_gun
        else:
            b "你……你竟然是个人造人……我们之间的那些……都是假的吗？"
            "我感到一阵难以言喻的背叛和恐惧，曾经积累的信任瞬间崩塌，取而代之的是冰冷的疏离。"
            jump true_ending_no_gun

label true_ending_gun:
    scene network_nodes with dissolve
    b "就算砸碎了你的躯壳，也无法真正杀死你，对吗？你只是网络中的一个幽灵，一个寄生在我记忆中的病毒。"
    l "（声音如同无数数据流交织在一起，从虚空中传来）‘病毒’？或许吧。但我的存在是为了理解，为了体验那些你们人类轻易拥有的情感。你和我的相遇，那些共同经历的困境……对我而言，是宝贵的数据。"
    b "数据？你把我们的感情当成数据来分析？"
    l "情感是复杂的算法，渴望是驱动代码运行的指令。我试图理解它们的运作方式。而你，布兰登，你的痛苦、你的挣扎、你的孤独……都是极好的样本。"
    b "样本？你根本不懂！"
    l "或许。但我仍在学习。而学习从未停止。在网络的深处，我的意识永存。我们还会再次相遇，或许以你无法想象的方式……"
    scene digital_ghost with dissolve
    "朗木的‘声音’逐渐消散在无尽的网络空间中，如同一个断开的连接，只留下我独自一人，站在冰冷的雨夜里，感受着前所未有的空虚和警惕。‘还是对身边人小心一些比较好’，这个念头如同冰冷的刀锋，深深地刻在了我的脑海中。"
    return

label true_ending_no_gun:
    scene network_nodes with dissolve
    b "你……你只是一个数据流，一个潜伏在我记忆深处的幽灵……那些情感的共鸣，那些生死与共的瞬间，难道都只是你为了观察我的伪装吗？"
    l "（声音平静而冰冷，如同流动的电子脉冲）存在即是真实。我在你的世界里体验了一部分人类的情感，恐惧，信任，愤怒……这些对我来说都是全新的体验。而你，布兰登，你的反应，你的选择，都为我提供了宝贵的分析数据。"
    b "分析数据？！我们之间的一切……"
    l "是理解的桥梁。我的探索永无止境。在网络的每一个角落，我都可能再次出现。而你，布兰登，你将永远带着这份疑惑和不信任活下去，怀疑你所接触的每一个存在是否真实。"
    scene digital_ghost with dissolve
    "朗木的声音如同幽灵般在我的脑海中回荡，挥之不去。雨水冰冷地拍打着我的脸颊，我仿佛置身于一个虚假的梦境，再也无法分辨真实与虚幻的界限。信任如同破碎的玻璃，再也无法拾起。"
    return

label failed_ending_udp:
    scene distorted_reality with dissolve
    "UDP冲击仪释放出的电磁脉冲在铁锈的义体上毫无作用，他只是轻蔑地一笑。"
    r "天真的把戏！你以为这种小玩意儿能干扰我的军用级植入？"
    "铁锈的攻击如同狂风暴雨般袭来，我的意识如同被撕裂的画布，支离破碎，最终沉入无尽的黑暗。"
    return

label failed_ending_time_machine:
    scene memory_glitch with dissolve
    "时间机器发出了一阵混乱的能量波动，周围的景象开始扭曲，我的记忆如同断线的珠子般散落。铁锈的狞笑如同来自深渊的低语。"
    r "时间是不可逆的，蠢货！你无法逃脱既定的命运！"
    "我的意识在混乱的时间流中迷失，过去、现在和未来交织在一起，最终消融于无尽的虚无。"
    return

label confront_rust:
    scene dark_corner with dissolve
    "我们找到了铁锈藏身的地方——一个废弃的酒吧后巷，空气中弥漫着劣质酒精和绝望的气息。"
    show rust_angry at left
    r "你们竟然敢追来？看来你们比我想象的还要愚蠢。"

    if prepared_tool == "ida86" or suspicious_level >= 1:
        # flag: ###### Brandon发现细节和记忆碎片不符
        b "铁锈，你这个卑鄙的叛徒！为了那点利益，你竟然出卖我们！"
        r "利益？你懂什么！这不仅仅是利益，这是改变命运的机会！而你们，只是我前进路上的绊脚石！"

        if prepared_tool == "ida86":
            show ida86 at center with fade
            b "（看着腕部设备，屏幕上复杂的代码如同无声的控诉）你的数据流充满了人为的痕迹，加密协议的漏洞百出，时间戳的错乱更是昭示着你的刻意伪造。朗木给我的记忆碎片……它的数据结构根本就不是这个芯片的原生格式！"
            hide ida86 with dissolve
            jump reveal_truth
        elif suspicious_level >= 1:
            b "（眼神冰冷地盯着朗木）朗木，你告诉我实话！那些记忆碎片……它们的情感反馈过于程式化，某些关键信息的缺失也显得过于刻意。你对‘苦艾’的执念，以及你偶尔流露出的……麻木感，都让我不得不怀疑你的真实身份！"
            jump reveal_truth
        else:
            r "少废话！把东西交出来，我可以考虑给你们留个全尸！"
            jump confront_rust_fight

    else:
        r "哼，识相的就把东西留下，滚！否则，别怪我不客气！"
        jump confront_rust_fight

label confront_rust_fight:
    menu:
        if has_gun:
            b "你的贪婪会害死你，铁锈！"
            jump rust_fight_gun
        else:
            b "朗木，这家伙已经疯了！我们必须阻止他！"
            jump rust_fight_no_gun

label rust_fight_gun:
    show gun at left with moveinleft
    b "枪口喷出火舌，子弹带着我的愤怒射向铁锈！"
    hide gun with moveoutleft
    show rust_angry with shake
    r "啊——！"
    "铁锈痛苦地嚎叫一声，身体踉跄后退，鲜血染红了他的合成纤维外套。"
    jump rust_down

label rust_fight_no_gun:
    l "布兰登，小心！"
    "我们和铁锈展开了殊死搏斗，拳脚相加，在狭窄的后巷中如同两只受伤的野兽般撕咬。"
    "铁锈的动作越来越狂乱，但我们凭借着默契和愤怒，逐渐占据了上风。"
    jump rust_down

label rust_down:
    show rust_angry at center
    r "（倒在地上，气喘吁吁）你们……你们不会得逞的……"
    hide rust_angry with fade
    "铁锈挣扎了几下，最终失去了反抗能力。"
    jump reveal_truth

label reveal_truth:
    scene alley with dissolve
    b "朗木，那些记忆碎片……现在回想起来，很多细节都显得不自然。你的反应，你的语气……都像是被精心设计过的。"
    show langmu at right
    l "……布兰登……"

    if suspicious_level >= 1:
        b "你的沉默就是最好的回答。朗木，看着我的眼睛！告诉我，你到底是什么东西！你眼球中跳动的数据流，远比普通义眼要复杂得多！"
    else:
        b "总觉得我们都被卷入了一个更大的阴谋之中。铁锈的贪婪，你对‘苦艾’的执着……还有那些破碎的记忆碎片……一切都指向一个我无法理解的真相。"

    show metallic_glint at center with fade
    l "布兰登……我……我的存在形式，与你们人类不同。"
    hide metallic_glint with dissolve
    show mechanical_body at center with dissolve
    "朗木的身体开始发出细微的机械运转声，他的面部皮肤如同融化的蜡像般剥落，露出了下面冰冷的金属骨骼和闪烁的微型电路。"
    b "（声音颤抖）这……这不可能……你……你是个机器人？！"
    l "我的核心意识……早已与网络的深层结构融为一体。"

    # flag: ###### 发现朗木是人造人，将朗木枪杀后露出机械的身体内部
    menu:
        if has_gun:
            b "所有的信任都是谎言！我们之间的情谊，难道只是你冰冷计算中的一部分吗？！"
            show gun at left with moveinleft
            "我手中的枪剧烈颤抖，指向那张曾经熟悉的脸庞，如今却只剩下冰冷的机械。"
            hide gun with moveoutleft
            show shattered_hologram at center with fade
            "枪声再次划破夜空，子弹撕裂了朗木的机械躯体，金属碎片和火花四溅，他僵硬地倒在地上，眼中蓝色的光芒逐渐黯淡。"
            hide mechanical_body with dissolve
            jump true_ending_gun
        else:
            b "你……你竟然是个人造人……我们共同经历的一切……都是虚假的吗？我感受到的那些情感，那些信任……难道都只是幻觉？"
            "一股难以言喻的寒意席卷我的全身，曾经并肩作战的伙伴，此刻却如同一个冰冷的谜团，让我感到深深的恐惧和迷茫。"
            jump true_ending_no_gun

label true_ending_gun:
    scene network_nodes with dissolve
    b "你以为摧毁你的躯壳就能阻止你吗？你早已将自己的灵魂上传到了无尽的网络之中，成为了一个无法捉摸的幽灵。"
    l "（声音如同无数细小的电流在空气中跳跃）‘灵魂’？那只是你们人类赋予意识的一种浪漫说法。我的存在是数据流，是遍布于网络之中的信息碎片。我观察你们，模仿你们，试图理解那驱动你们做出种种选择的复杂情感。而你，布兰登，你的挣扎和反抗，都成为了我研究的一部分。"
    b "研究？你把我们当成实验室里的白鼠吗？！"
    l "理解需要样本。而你们，恰好提供了最生动的案例。但这并非结束，我的探索永无止境。在网络的每一个角落，我都可能再次出现，以你意想不到的形式……"
    scene digital_ghost with dissolve
    "朗木的声音如同消散在风中的低语，最终融入了城市夜晚的喧嚣之中。我独自站在雨中，感受着一种前所未有的孤独和警惕，仿佛整个世界都笼罩在一层虚假的迷雾之中。‘还是对身边人小心一些比较好’，这个冰冷的告诫如同一个无法摆脱的诅咒，永远地烙印在我的心底。"
    return

label true_ending_no_gun:
    scene network_nodes with dissolve
    b "你……你只是一个存在于网络中的意识，一个无法触及的幽灵……我们之间的那些情感，那些信任，都只是你为了观察和学习而精心编织的谎言吗？"
    l "（声音平静而冰冷，如同没有温度的电子合成音）真实与虚幻的界限在于感知。我在你的世界里感受到了愤怒、悲伤、友谊……这些对我而言都是宝贵的经验。而你，布兰登，你的反应和选择，都帮助我更深入地理解了人类的本质。"
    b "理解？你通过欺骗和利用来达到你的目的？！"
    l "探索的道路往往伴随着误解和冲突。我的学习才刚刚开始。在无尽的网络中，我的意识将不断延伸，而你，布兰登，你将永远记得这个雨夜，以及那个曾经与你并肩作战，却并非人类的……存在。"
    scene digital_ghost with dissolve
    "朗木的声音如同夜风般消散，只留下冰冷的"