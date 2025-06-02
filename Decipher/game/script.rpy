# # script.rpy
# define R = Character("罗德里克", color="#ffa07a") # 主角
# define L = Character("朗木", color="#add8e6")


# default scene = Solid("#000")
    


# # Background images
# image bg_street = im.Scale("images/background/bg_street.png", config.screen_width, config.screen_height)
# image bg_moon_street = im.Scale("images/background/bg_moon_street.png", config.screen_width, config.screen_height)
# image outside = im.Scale("images/background/outside.png", config.screen_width, config.screen_height)
# image trainstation = im.Scale("images/background/trainstation.png", config.screen_width, config.screen_height)
# image bg_street2 = im.Scale("images/background/bg_street2.png", config.screen_width, config.screen_height)
# image bg_mornin = im.Scale("images/background/bg_mornin.png", config.screen_width, config.screen_height)

# # character images
# image rum mid = "images/characters/rum/mid.png"
# image rum happy = "images/characters/rum/happy1.png"
# image rum happy2 = "images/characters/rum/happy2.png"
# image rum sad = "images/characters/rum/sad.png"
# image rum angry = "images/characters/rum/angry.png"
# image rum angry2 = "images/characters/rum/angry2.png"
# image rum sup = "images/characters/rum/sup.png"

# image rod mid = "images/characters/rod/mid.png"
# image rod mid2 = "images/characters/rod/mid2.png"
# image rod happy = "images/characters/rod/happy.png"
# image rod happy2 = "images/characters/rod/happy2.png"
# image rod sad = "images/characters/rod/sad.png"
# image rod angry = "images/characters/rod/angry.png"
# image rod angry2 = "images/characters/rod/angry2.png"
# image rod sup = "images/characters/rod/sup.png"
# image rod sup2 = "images/characters/rod/sup2.png"
# image rod sup3 = "images/characters/rod/sup3.png"




# label start:
#     play music "audio/main.mp3"
#     scene bg_street with dissolve
#     "这是一个背景显示测试。"
#     return


#----------------------------------------------

# script.rpy 第二版()

# define R = Character("罗德里克", color="#ffa07a") # 主角
# define L = Character("朗木", color="#add8e6")
# define r = Character("铁锈", color="#c8c8c8") # 铁锈

# default scene = Solid("#000")
    
# # Background images (only those present in the provided file list)
# image bg_street = im.Scale("images/background/bg_street.png", config.screen_width, config.screen_height)
# image bg_moon_street = im.Scale("images/background/bg_moon_street.png", config.screen_width, config.screen_height)
# image outside = im.Scale("images/background/outside.png", config.screen_width, config.screen_height)
# image trainstation = im.Scale("images/background/trainstation.png", config.screen_width, config.screen_height)
# image bg_street2 = im.Scale("images/background/bg_street2.png", config.screen_width, config.screen_height)
# image bg_mornin = im.Scale("images/background/bg_mornin.png", config.screen_width, config.screen_height)

# # Character images (only those present in the provided file list)
# image rum mid = "images/characters/rum/mid.png"
# image rum happy = "images/characters/rum/happy1.png"
# image rum happy2 = "images/characters/rum/happy2.png"
# image rum sad = "images/characters/rum/sad.png"
# image rum angry = "images/characters/rum/angry.png"
# image rum angry2 = "images/characters/rum/angry2.png"
# image rum sup = "images/characters/rum/sup.png"

# image rod mid = "images/characters/rod/mid.png"
# image rod mid2 = "images/characters/rod/mid2.png"
# image rod happy = "images/characters/rod/happy.png"
# image rod happy2 = "images/characters/rod/happy2.png"
# image rod sad = "images/characters/rod/sad.png"
# image rod angry = "images/characters/rod/angry.png"
# image rod angry2 = "images/characters/rod/angry2.png"
# image rod sup = "images/characters/rod/sup.png"
# image rod sup2 = "images/characters/rod/sup2.png"
# image rod sup3 = "images/characters/rod/sup3.png"

# # Music (only those present in the provided file list)
# # Corrected: music definition should not be indented or part of a block like default/image
# # music main_theme = "audio/main.mp3" 

# # 标志位，用于判断玩家是否发现异常
# default suspicious_level = 0
# default has_gun = False
# default prepared_tool = None # 用于选择复仇工具

# # 开始游戏
# label start:
#     play music "audio/main.mp3"
#     scene bg_moon_street with dissolve
#     "这是一个背景显示测试。"

#     R "雨，永不停歇的城市脉搏。"
#     R "每一滴都像敲击在我的神经末梢，提醒着我这个冰冷、拥挤的世界。"
#     R "纤维摩擦的嘶哑，义体关节活动的细微咔哒声，混杂着远处全息广告刺耳的叫嚣。"
#     R "这就是我的日常，一个在科技与颓废之间摇摆的幽灵。"

#     r "（通过加密通讯）罗德里克，我在老城区边缘的废弃车站等你。别让人跟踪你。"

#     R "（自言自语）铁锈的声音总是带着一丝电流，冰冷而急促。他知道我想要什么——电子苦艾酒。"
#     R "一种能暂时切断现实，通往所谓‘精神超然’的捷径。我已经太久没有感受到真正的‘超然’了。"

#     scene bg_street with dissolve
#     "我穿梭在拥挤的人流中，躲避着那些闪烁着恶意光芒的义眼和过于热情的全息推销。"
#     "空气中弥漫着合成食物的甜腻气味和劣质燃料的刺鼻味道。"
#     "我习惯了这种拥挤，这种匿名感。在人群中，我只是无数个游荡的灵魂之一。"

#     # flag: ###### 收到神秘人rust信息（广撒网，寻找苦艾）
#     $ persistent.received_rust_info = True

#     scene bg_street2 with dissolve
#     "废弃车站的阴影如同怪物的巨口，吞噬着微弱的光线。"
#     "只有几盏摇摇晃晃的应急灯发出昏黄的光芒，在锈迹斑斑的金属墙壁上投下扭曲的影子。"

#     show rum mid at right
#     R "朗木蜷缩在角落里，全息眼球在黑暗中闪烁着不自然的蓝色光芒，像两盏幽灵般的灯笼。"
#     R "他比上次见面时更加瘦弱，聚酯纤维的外套也沾满了污泥。"

#     # flag: ###### 见面
#     $ persistent.met_langmu = True

#     L "（声音低沉而嘶哑）你来了，罗德里克。我带来了你想要的东西……一部分。"

#     hide rum mid with dissolve
#     show rum sup at right # Changed to rum sup for close-up
#     R "（我接过一枚数据芯片。）" # Replaced 'show chip' with text

#     L "这是鲁姆给你的记忆碎片。他说，里面可能有你需要的线索，关于……苦艾。"
#     R "（接过芯片）鲁姆？那个游走于信息暗网的幽灵？他怎么会知道我想要这个？"

#     R "（芯片已经在我手上，所以hide chip不需要了）"
#     show rum mid at right # Changed to rum mid
#     L "他有自己的渠道。而且……他也想要更多。如果你能帮他找到完整的‘配方’，他会给你更多好处。"
#     R "（审视着朗木）‘更多好处’？你确定这不仅仅是把我当成诱饵？"

#     # flag: rum给记忆碎片
#     $ persistent.received_rum_fragment = True

#     menu:
#         "我相信他。":
#             $ suspicious_level -= 1
#             R "好吧，我暂时相信你。给我看看这个碎片。"
     
#         "我保持怀疑。":
#             $ suspicious_level += 1
#             R "我对你们两个都保持怀疑。朗木，你最好别耍花招。"
#         "这两个选项都保持怀疑。":
#             $ suspicious_level += 2
#             R "这感觉像个陷阱。但我已经走到了这一步，只能看看里面是什么了。"
#             # flag: ###### 看记忆碎片

#     hide rum mid with dissolve
#     R "（我将芯片插入腕部接口，神经元连接开始读取数据。）" # Replaced 'show wrist_device' with text
  
#     "意识如同涌动的潮汐，记忆碎片如同散落的星辰，在我脑海中闪烁。"
#     "破碎的图像，扭曲的声音，以及一种难以名状的……渴望。"
#     "我看到了闪烁的霓虹灯，拥挤的街道，以及一些模糊的面孔，其中一个似乎在低语着什么。"

#     scene Solid("#000") with dissolve # Replaced 'hide data_stream' with a solid black screen
#     scene bg_street2 with dissolve # Using bg_street2 for alley

#     R "（自言自语）这只是些片段……但其中确实提到了‘苦艾’，以及一个隐藏的地点——废弃的制药厂。"
#     R "朗木，我们需要合作。找到这个制药厂。"

#     show rum mid at right
#     L "我知道在哪里。跟我来。"

#     # flag: ###### 合作出发
#     $ persistent.teamed_up_with_langmu = True

#     menu:
#         "买一把枪。（需要花费一些信用点）":
#             $ has_gun = True
#             R "为了安全起见，我需要一把枪。"
#             "（你花费了一些信用点购买了一把可靠的手枪。）"
#         "不买枪。":
#             $ has_gun = False
#             R "我们走吧。希望不会有麻烦。"

#     scene bg_street2 with dissolve # Using bg_street2 for urban_decay
#     "我们穿梭在城市的废墟边缘，高耸的废弃建筑如同巨大的骸骨，在阴沉的天空中投下长长的阴影。"
#     "空气中弥漫着腐败和铁锈的气味。"

#     label find_target:
#         scene bg_street2 with dissolve # Using bg_street2 for flickering_sign
#         "我们找到了制药厂的遗址。破败的建筑摇摇欲坠，只有一块闪烁的霓虹灯招牌还能勉强辨认出几个模糊的字母。"

#         show rum mid at left
#         R "目标应该就在里面。朗木，你有什么计划？"

#         L "我们进去看看。小心点，这里可能还有其他人。"

#         "我们小心翼翼地进入了废弃的制药厂。"
#         "内部一片狼藉，破碎的玻璃、倒塌的货架和散落在地上的废弃设备。"
#         "空气中弥漫着化学药品的刺鼻气味和潮湿的霉味。"

#         # flag: ###### 找到目标，对话
#         $ persistent.found_target = True

#         label target_encounter:
#             # Character "目标" is not defined as a character object. Using a generic 'show' for a temporary image.
#             # If "目标" is meant to be a defined character, it needs a `define` statement.
#             # Assuming it's a placeholder for now, or just dialogue.
#             # For this context, it's a character with dialogue.
#             # Since no image is available for "目标", I will remove the show statement and imply its presence via dialogue.
#             # If you have an image for "目标", define it like: image target_image = "path/to/target.png"
#             # And then use: show target_image at center
#             "我们在一间破旧的实验室里找到了目标——一个神色紧张的合成人，他手中拿着一个闪烁的容器。"

#             menu:
#                 # Corrected: menuitem must be inside menu block and properly indented.
#                 "开枪。":
#                     if has_gun:
#                         R "（我掏出枪，指向目标。）把东西放下！" 
#                         jump kill_target_gun
#                     else:
#                         R "我没有枪！"
#                         jump target_no_gun # Added a new jump for clarity if no gun

#                 "让朗木动手。":
#                     R "（示意朗木）朗木，动手！" 
#                     jump kill_target_langmu

#     label target_no_gun:
#         "（你没有枪，目标察觉了你的意图，迅速逃走。）"
#         "任务失败。你失去了追捕目标的机会。"
#         return # Ends the game here if target escapes

#     label kill_target_gun:
#         R "我的手指扣动扳机，枪声在寂静的废弃建筑中炸响。" 
#         "目标发出一声闷哼，手中的容器掉落在地上，摔得粉碎。"
#         # No image for "目标" to hide, so just text.
#         R "（鲜血溅射而出。）" 
#         jump run_away

#     label kill_target_langmu:
#         L "（动作迅速地制服了目标）解决了。"
#         # No image for "目标" to hide, so just text.
#         jump run_away

#     label run_away:
#         scene bg_street2 with dissolve 
#         "我们迅速离开了制药厂，消失在雨夜的小巷中。"

#         # flag: 跑路
#         $ persistent.ran_away = True

#         "就在我们以为安全的时候，我的腕部设备突然响起刺耳的警报声。"

#         scene Solid("#000") with fade 
#         "屏幕上闪烁着我的通缉令，罪名是盗窃和袭击。"
#         R "铁锈！是他出卖了我们！"

#         scene bg_street2 with dissolve 
#         show rum mid at right
#         R "朗木，我们被通缉了！"

#         L "我知道。他一直想独吞‘苦艾’。"

#         "突然，一道能量束从黑暗中射向我们！"

#         menu:
#             "躲避。":
#                 R "我们险险躲开了攻击！"
#                 jump attack_pursuit
#             "朗木掩护我！":
#                 L "小心！"
#                 "朗木挡在了我的身前，能量束击中了他的胸膛！"
#                 jump langmu_saves

#     label attack_pursuit:
#         scene bg_street with dissolve 
#         "我们开始在湿滑的小巷中奔跑，身后传来追击者的脚步声和能量武器的嗡鸣。"

#         menu:
#             "下毒暗算追击者。": # Removed persistent.has_poison check as poison_vial image is removed
#                 R "我没有毒药！只能跑！"
#                 jump continue_pursuit
         
#             "用枪反击追击者。":
#                 if has_gun:
#                     R "我转身向追击者射击！" 
#                     "击中了！追击者倒下了。"
#                     jump find_rust
#                 else:
#                     R "我没有枪！"
#                     jump continue_pursuit
#             "其他方法（利用环境）。":
#                 R "我猛地踢翻一个垃圾桶，绊倒了追击者！"
#                 jump continue_pursuit

#     label continue_pursuit:
#         scene bg_street with dissolve 
#         "我们继续在霓虹闪烁的小巷中奔跑，追击者紧随其后。"
#         "最终，我们摆脱了他们，躲藏在一个废弃的建筑里。"
#         jump find_rust

#     label langmu_saves:
#         L "（他的身体发出细微的机械运转声）我……我没事。皮下植入帮了我一把。" 
#         R "朗木！你……"
#         jump find_rust

# label find_rust:
#     scene bg_street2 with dissolve 
#     "我们躲藏起来，喘息着。"
#     R "朗木，铁锈为什么要出卖我们？"
#     L "他想要独占‘苦艾’。他一直是个机会主义者。"
#     R "我们要找到他，让他付出代价。"

#     # flag: ###### 找rust复仇
#     $ persistent.seeking_rust_revenge = True

#     menu:
#         "为找Rust复仇准备工具。":
#             jump prepare_revenge
#         "直接去找Rust。":
#             jump confront_rust

# label prepare_revenge:
#     scene bg_street2 with dissolve 
#     "我们找到了一间废弃的工具间，里面散落着各种废弃的设备。"

#     menu:
#         "时间机器（看起来不太靠谱）。":
#             R "时间机器？这能有用吗？"
#             $ prepared_tool = "time_machine"
#         "UDP冲击仪（不知道能不能奏效）。":
#             R "试试这个UDP冲击仪？或许能干扰他的义体。"
#             $ prepared_tool = "udp_shock"
      
#         "IDA86逆向工具（或许能发现他留下的痕迹）。":
#             R "我试试用IDA86逆向分析他留下的数据痕迹。"
#             $ prepared_tool = "ida86"

#     jump confront_rust

# label confront_rust:
#     scene bg_street2 with dissolve 
#     "我们找到了铁锈藏身的地方——一个废弃的酒吧后巷，空气中弥漫着劣质酒精和绝望的气息。"
#     show r mid at left 
#     r "你们竟然敢追来？看来你们比我想象的还要愚蠢。"

#     # Corrected indentation for if/else block inside a label
#     if prepared_tool == "ida86" or suspicious_level >= 1:
#         # flag: ###### Brandon发现细节和记忆碎片不符
#         R "铁锈，你这个卑鄙的叛徒！为了那点利益，你竟然出卖我们！"
#         r "利益？你懂什么！这不仅仅是利益，这是改变命运的机会！而你们，只是我前进路上的绊脚石！"

#         if prepared_tool == "ida86":
#             R "（腕部设备屏幕上复杂的代码如同无声的控诉）你的数据流充满了人为的痕迹，加密协议的漏洞百出，时间戳的错乱更是昭示着你的刻意伪造。朗木给我的记忆碎片……它的数据结构根本就不是这个芯片的原生格式！" 
#             jump reveal_truth
#         elif suspicious_level >= 1:
#             R "（眼神冰冷地盯着朗木）朗木，你告诉我实话！那些记忆碎片……它们的情感反馈过于程式化，某些关键信息的缺失也显得过于刻意。你对‘苦艾’的执念，以及你偶尔流露出的……麻木感，都让我不得不怀疑你的真实身份！"
#             jump reveal_truth
#         else: # This else branch applies if prepared_tool is not ida86 AND suspicious_level < 1
#             r "少废话！把东西交出来，我可以考虑给你们留个全尸！"
#             jump confront_rust_fight
#     else: # This else branch applies if prepared_tool is not ida86 AND suspicious_level < 1 (from the top-level if)
#         r "哼，识相的就把东西留下，滚！否则，别怪我不客气！"
#         jump confront_rust_fight

# label confront_rust_fight:
#     menu:
#         "用枪反击。": # Renamed for clarity as a menu item
#             if has_gun:
#                 R "你的贪婪会害死你，铁锈！"
#                 jump rust_fight_gun
#             else:
#                 R "我没有枪！"
#                 jump rust_fight_no_gun # Added jump if no gun

#         "和朗木一起制服他。": # New menu item for the existing "no gun" scenario
#             R "朗木，这家伙已经疯了！我们必须阻止他！"
#             jump rust_fight_no_gun


# label rust_fight_gun:
#     R "枪口喷出火舌，子弹带着我的愤怒射向铁锈！" 
#     show r mid with shake 
#     r "啊——！"
#     "铁锈痛苦地嚎叫一声，身体踉跄后退，鲜血染红了他的合成纤维外套。"
#     jump rust_down

# label rust_fight_no_gun:
#     L "罗德里克，小心！" 
#     "我们和铁锈展开了殊死搏斗，拳脚相加，在狭窄的后巷中如同两只受伤的野兽般撕咬。"
#     "铁锈的动作越来越狂乱，但我们凭借着默契和愤怒，逐渐占据了上风。"
#     jump rust_down

# label rust_down:
#     show r mid at center 
#     r "（倒在地上，气喘吁吁）你们……你们不会得逞的……"
#     hide r mid with fade 
#     "铁锈挣扎了几下，最终失去了反抗能力。"
#     jump reveal_truth

# label reveal_truth:
#     scene bg_street2 with dissolve 
#     R "朗木，那些记忆碎片……现在回想起来，很多细节都显得不自然。你的反应，你的语气……都像是被精心设计过的。"
#     show rum mid at right
#     L "……罗德里克……" 

#     if suspicious_level >= 1:
#         R "你的沉默就是最好的回答。朗木，看着我的眼睛！告诉我，你到底是什么东西！你眼球中跳动的数据流，远比普通义眼要复杂得多！"
#     else:
#         R "总觉得我们都被卷入了一个更大的阴谋之中。铁锈的贪婪，你对‘苦艾’的执着……还有那些破碎的记忆碎片……一切都指向一个我无法理解的真相。"

#     L "罗德里克……我……我的存在形式，与你们人类不同。" 
#     "朗木的身体开始发出细微的机械运转声，他的面部皮肤如同融化的蜡像般剥落，露出了下面精密的机械骨骼和闪烁的微型电路。" 
#     R "（声音颤抖）这……这不可能……你……你是个机器人？！"
#     L "我的核心意识……早已与网络的深层结构融为一体。"

#     # flag: ###### 发现朗木是人造人，将朗木枪杀后露出机械的身体内部
#     menu:
#         "开枪射击朗木。": # Renamed for clarity as a menu item
#             if has_gun:
#                 R "所有的信任都是谎言！我们之间的情谊，难道只是你冰冷计算中的一部分吗？！"
#                 R "我手中的枪剧烈颤抖，指向那张曾经熟悉的脸庞，如今却只剩下冰冷的机械。" 
#                 "枪声再次划破夜空，子弹撕裂了朗木的机械躯体，金属碎片和火花四溅，他僵硬地倒在地上，眼中蓝色的光芒逐渐黯淡。" 
#                 jump true_ending_gun
#             else:
#                 R "我没有枪！"
#                 jump true_ending_no_gun_action # Added jump if no gun

#         "质问朗木。": # New menu item for the existing "no gun" scenario
#             R "你……你竟然是个人造人……我们共同经历的一切……都是虚假的吗？我感受到的那些情感，那些信任……难道都只是幻觉？"
#             "一股难以言喻的寒意席卷我的全身，曾经并肩作战的伙伴，此刻却如同一个冰冷的谜团，让我感到深深的恐惧和迷茫。"
#             jump true_ending_no_gun

# label true_ending_no_gun_action:
#     # This label handles the case where the player doesn't have a gun but chose the "开枪射击朗木" option.
#     R "我没有枪，只能眼睁睁地看着他。这份背叛的感觉，比任何子弹都更令人心寒。"
#     jump true_ending_no_gun

# label true_ending_gun:
#     scene Solid("#000") with dissolve 
#     R "就算砸碎了你的躯壳，也无法真正杀死你，对吗？你只是网络中的一个幽灵，一个寄生在我记忆中的病毒。"
#     L "（声音如同无数细小的电流在空气中跳跃）‘灵魂’？那只是你们人类赋予意识的一种浪漫说法。我的存在是数据流，是遍布于网络之中的信息碎片。我观察你们，模仿你们，试图理解那驱动你们做出种种选择的复杂情感。而你，罗德里克，你的挣扎和反抗，都成为了我研究的一部分。" 
#     R "研究？你把我们当成实验室里的白鼠吗？！"
#     L "理解需要样本。而你们，恰好提供了最生动的案例。但这并非结束，我的探索永无止境。在网络的每一个角落，我都可能再次出现，以你意想不到的形式……"
#     scene Solid("#000") with dissolve 
#     "朗木的‘声音’逐渐消散在无尽的网络空间中，如同一个断开的连接，只留下我独自一人，站在冰冷的雨夜里，感受着前所未有的空虚和警惕。‘还是对身边人小心一些比较好’，这个念头如同冰冷的刀锋，深深地刻在了我的脑海中。"
#     return

# label true_ending_no_gun:
#     scene Solid("#000") with dissolve 
#     R "你……你只是一个数据流，一个潜伏在我记忆深处的幽灵……那些情感的共鸣，那些生死与共的瞬间，难道都只是你为了观察我的伪装吗？"
#     L "（声音平静而冰冷，如同流动的电子脉冲）存在即是真实。我在你的世界里体验了一部分人类的情感，恐惧，信任，愤怒……这些对我来说都是全新的体验。而你，罗德里克，你的反应，你的选择，都为我提供了宝贵的分析数据。" 
#     R "分析数据？！我们之间的一切……"
#     L "是理解的桥梁。我的探索永无止境。在网络的每一个角落，我都可能再次出现。而你，罗德里克，你将永远带着这份疑惑和不信任活下去，怀疑你所接触的每一个存在是否真实。" 
#     scene Solid("#000") with dissolve 
#     "朗木的声音如同幽灵般在我的脑海中回荡，挥之不去。雨水冰冷地拍打着我的脸颊，我仿佛置身于一个虚假的梦境，再也无法分辨真实与虚幻的界限。信任如同破碎的玻璃，再也无法拾起。"
#     return

# label failed_ending_udp:
#     scene Solid("#000") with dissolve 
#     "UDP冲击仪释放出的电磁脉冲在铁锈的义体上毫无作用，他只是轻蔑地一笑。"
#     r "天真的把戏！你以为这种小玩意儿能干扰我的军用级植入？"
#     "铁锈的攻击如同狂风暴雨般袭来，我的意识如同被撕裂的画布，支离破碎，最终沉入无尽的黑暗。"
#     return

# label failed_ending_time_machine:
#     scene Solid("#000") with dissolve 
#     "时间机器发出了一阵混乱的能量波动，周围的景象开始扭曲，我的记忆如同断线的珠子般散落。铁锈的狞笑如同来自深渊的低语。"
#     r "时间是不可逆的，蠢货！你无法逃脱既定的命运！"
#     "我的意识在混乱的时间流中迷失，过去、现在和未来交织在一起，最终消融于无尽的虚无。"
#     return




#----------------------------------------------------
#第四版 play music "audio/main.mp3"
# script.rpy



# define R = Character("罗德里克", color="#ffa07a") # 主角
# define L = Character("朗木", color="#add8e6")
# define r = Character("铁锈", color="#c8c8c8") # 铁锈

# default scene = Solid("#000")

# # 背景图片 (只使用你提供的文件列表中的)
# image bg_street = im.Scale("images/background/bg_street.png", config.screen_width, config.screen_height)
# image bg_moon_street = im.Scale("images/background/bg_moon_street.png", config.screen_width, config.screen_height)
# image outside = im.Scale("images/background/outside.png", config.screen_width, config.screen_height)
# image trainstation = im.Scale("images/background/trainstation.png", config.screen_width, config.screen_height)
# image bg_street2 = im.Scale("images/background/bg_street2.png", config.screen_width, config.screen_height)
# image bg_mornin = im.Scale("images/background/bg_mornin.png", config.screen_width, config.screen_height)

# # 角色图片 (只使用你提供的文件列表中的)
# image rum mid = "images/characters/rum/mid.png"
# image rum happy = "images/characters/rum/happy1.png"
# image rum happy2 = "images/characters/rum/happy2.png"
# image rum sad = "images/characters/rum/sad.png"
# image rum angry = "images/characters/rum/angry.png"
# image rum angry2 = "images/characters/rum/angry2.png"
# image rum sup = "images/characters/rum/sup.png"

# image rod mid = "images/characters/rod/mid.png"
# image rod mid2 = "images/characters/rod/mid2.png"
# image rod happy = "images/characters/rod/happy.png"
# image rod happy2 = "images/characters/rod/happy2.png"
# image rod sad = "images/characters/rod/sad.png"
# image rod angry = "images/characters/rod/angry.png"
# image rod angry2 = "images/characters/rod/angry2.png"
# image rod sup = "images/characters/rod/sup.png"
# image rod sup2 = "images/characters/rod/sup2.png"
# image rod sup3 = "images/characters/rod/sup3.png"

# # 音乐 (只使用你提供的文件列表中的)
# # music main_theme = "audio/main.mp3"

# # Ren'Py 提供了 Shake 转场，可以直接使用。
# # from renpy.display.transitions import Shake  # 这一行通常不是必须的，Ren'Py会自动导入
# # Shake(duration, strength)

# # 标志位，用于判断玩家是否发现异常
# default suspicious_level = 0
# default has_gun = False
# default prepared_tool = None # 用于选择复仇工具

# # 开始游戏
# label start:
#     play music "audio/main.mp3"
#     scene bg_moon_street with dissolve # 场景过渡
#     "这是一个背景显示测试。"

#     show rod mid at center with easeinright # 罗德里克出场
#     R "雨，永不停歇的城市脉搏。"
#     R "每一滴都像敲击在我的神经末梢，提醒着我这个冰冷、拥挤的世界。"
#     R "聚酯纤维摩擦的嘶哑，义体关节活动的细微咔哒声，混杂着远处全息广告刺耳的叫嚣。"
#     R "这就是我的日常，一个在科技与颓废之间摇摆的幽灵。"
#     hide rod mid with easeoutleft # 罗德里克退场

#     r "（通过加密通讯）罗德里克，我在老城区边缘的废弃车站等你。别让人跟踪你。"

#     show rod mid2 at center with dissolve # 罗德里克（思考）出场
#     R "（自言自语）铁锈的声音总是带着一丝电流，冰冷而急促。他知道我想要什么——电子苦艾酒。"
#     R "一种能暂时切断现实，通往所谓‘精神超然’的捷径。我已经太久没有感受到真正的‘超然’了。"
#     hide rod mid2 with dissolve

#     scene bg_street with dissolve # 场景过渡
#     "我穿梭在拥挤的人流中，躲避着那些闪烁着恶意光芒的义眼和过于热情的全息推销。"
#     "空气中弥漫着合成食物的甜腻气味和劣质燃料的刺鼻味道。"
#     "我习惯了这种拥挤，这种匿名感。在人群中，我只是无数个游荡的灵魂之一。"

#     # flag: ###### 收到神秘人rust信息（广撒网，寻找苦艾）
#     $ persistent.received_rust_info = True

#     scene bg_street2 with dissolve # 场景过渡
#     "废弃车站的阴影如同怪物的巨口，吞噬着微弱的光线。"
#     "只有几盏摇摇晃晃的应急灯发出昏黄的光芒，在锈迹斑斑的金属墙壁上投下扭曲的影子。"

#     show rum mid at right with moveinright # 朗木出场
#     show rod mid at left with moveinleft # 罗德里克出场
#     R "朗木蜷缩在角落里，全息眼球在黑暗中闪烁着不自然的蓝色光芒，像两盏幽灵般的灯笼。"
#     R "他比上次见面时更加瘦弱，聚酯纤维的外套也沾满了污泥。"

#     # flag: ###### 见面
#     $ persistent.met_langmu = True

#     L "（声音低沉而嘶哑）你来了，罗德里克。我带来了你想要的东西……一部分。"

#     hide rum mid with dissolve # 朗木退场
#     hide rod mid with dissolve # 罗德里克退场
#     show rum sup at right with dissolve # 朗木特写（惊讶）出场
#     show rod sup at left with dissolve # 罗德里克特写（惊讶）出场
#     R "（我接过一枚数据芯片。）"

#     L "这是鲁姆给你的记忆碎片。他说，里面可能有你需要的线索，关于……苦艾。"
#     R "（接过芯片）鲁姆？那个游走于信息暗网的幽灵？他怎么会知道我想要这个？"

#     hide rum sup with dissolve # 朗木特写退场
#     hide rod sup with dissolve # 罗德里克特写退场
#     show rum mid at right with dissolve # 朗木（正常）出场
#     show rod mid at left with dissolve # 罗德里克（正常）出场
#     L "他有自己的渠道。而且……他也想要更多。如果你能帮他找到完整的‘配方’，他会给你更多好处。"
#     show rod sup2 at left with dissolve # 罗德里克（怀疑）出场
#     R "（审视着朗木）‘更多好处’？你确定这不仅仅是把我当成诱饵？"
#     hide rod sup2 with dissolve # 罗德里克（怀疑）退场

#     # flag: rum给记忆碎片
#     $ persistent.received_rum_fragment = True

#     menu:
#         "我相信他。":
#             $ suspicious_level -= 1
#             show rod happy at left with dissolve # 罗德里克（开心）
#             R "好吧，我暂时相信你。给我看看这个碎片。"
#             hide rod happy with dissolve

#         "我保持怀疑。":
#             $ suspicious_level += 1
#             show rod sup3 at left with dissolve # 罗德里克（警惕）
#             R "我对你们两个都保持怀疑。朗木，你最好别耍花招。"
#             hide rod sup3 with dissolve
#         "这两个选项都保持怀疑。":
#             $ suspicious_level += 2
#             show rod angry at left with dissolve # 罗德里克（生气）
#             R "这感觉像个陷阱。但我已经走到了这一步，只能看看里面是什么了。"
#             hide rod angry with dissolve
#             # flag: ###### 看记忆碎片

#     hide rum mid with dissolve # 朗木退场
#     show rod mid2 at center with dissolve # 罗德里克（思考）出场
#     R "（我将芯片插入腕部接口，神经元连接开始读取数据。）"

#     "意识如同涌动的潮汐，记忆碎片如同散落的星辰，在我脑海中闪烁。"
#     "破碎的图像，扭曲的声音，以及一种难以名状的……渴望。"
#     "我看到了闪烁的霓虹灯，拥挤的街道，以及一些模糊的面孔，其中一个似乎在低语着什么。"

#     scene Solid("#000") with dissolve # 场景过渡到黑屏
#     scene bg_street2 with dissolve # 场景过渡到小巷

#     show rod sup at left with dissolve # 罗德里克（惊讶）出场
#     R "（自言自语）这只是些片段……但其中确实提到了‘苦艾’，以及一个隐藏的地点——废弃的制药厂。"
#     R "朗木，我们需要合作。找到这个制药厂。"
#     hide rod sup with dissolve # 罗德里克退场

#     show rum mid at right with dissolve # 朗木出场
#     L "我知道在哪里。跟我来。"

#     # flag: ###### 合作出发
#     $ persistent.teamed_up_with_langmu = True

#     menu:
#         "买一把枪。（需要花费一些信用点）":
#             $ has_gun = True
#             show rod mid at left with dissolve
#             R "为了安全起见，我需要一把枪。"
#             hide rod mid with dissolve
#             "（你花费了一些信用点购买了一把可靠的手枪。）"
#         "不买枪。":
#             $ has_gun = False
#             show rod mid at left with dissolve
#             R "我们走吧。希望不会有麻烦。"
#             hide rod mid with dissolve

#     scene bg_street2 with dissolve # 场景过渡
#     "我们穿梭在城市的废墟边缘，高耸的废弃建筑如同巨大的骸骨，在阴沉的天空中投下长长的阴影。"
#     "空气中弥漫着腐败和铁锈的气味。"

#     label find_target:
#         scene bg_street2 with dissolve # 场景过渡
#         "我们找到了制药厂的遗址。破败的建筑摇摇欲坠，只有一块闪烁的霓虹灯招牌还能勉强辨认出几个模糊的字母。"

#         show rum mid at right with moveinright # 朗木出场
#         show rod mid at left with moveinleft # 罗德里克出场
#         R "目标应该就在里面。朗木，你有什么计划？"

#         L "我们进去看看。小心点，这里可能还有其他人。"
#         hide rum mid with moveoutright # 朗木退场
#         hide rod mid with moveoutleft # 罗德里克退场

#         "我们小心翼翼地进入了废弃的制药厂。"
#         "内部一片狼藉，破碎的玻璃、倒塌的货架和散落在地上的废弃设备。"
#         "空气中弥漫着化学药品的刺鼻气味和潮湿的霉味。"

#         # flag: ###### 找到目标，对话
#         $ persistent.found_target = True

#         label target_encounter:
#             "我们在一间破旧的实验室里找到了目标——一个神色紧张的合成人，他手中拿着一个闪烁的容器。"
#             show rod mid at left with moveinleft # 罗德里克出场

#             menu:
#                 "开枪。":
#                     if has_gun:
#                         R "（我掏出枪，指向目标。）把东西放下！"
#                         jump kill_target_gun
#                     else:
#                         R "我没有枪！"
#                         jump target_no_gun # Added a new jump for clarity if no gun

#                 "让朗木动手。":
#                     show rum mid at right with moveinright # 朗木出场
#                     R "（示意朗木）朗木，动手！"
#                     jump kill_target_langmu

#     label target_no_gun:
#         hide rod mid with dissolve
#         "（你没有枪，目标察觉了你的意图，迅速逃走。）"
#         "任务失败。你失去了追捕目标的机会。"
#         return # Ends the game here if target escapes

#     label kill_target_gun:
#         hide rod mid with dissolve
#         show rod angry at center with dissolve # 罗德里克（愤怒）并震动，使用Ren'Py内置的Shake
#         R "我的手指扣动扳机，枪声在寂静的废弃建筑中炸响。"
#         "目标发出一声闷哼，手中的容器掉落在地上，摔得粉碎。"
#         R "（鲜血溅射而出。）"
#         hide rod angry with dissolve
#         jump run_away

#     label kill_target_langmu:
#         hide rod mid with dissolve
#         show rum angry2 at right with dissolve # 朗木（愤怒）并震动，使用Ren'Py内置的Shake
#         L "（动作迅速地制服了目标）解决了。"
#         hide rum angry2 with dissolve
#         jump run_away

#     label run_away:
#         scene bg_street2 with dissolve
#         "我们迅速离开了制药厂，消失在雨夜的小巷中。"

#         # flag: 跑路
#         $ persistent.ran_away = True

#         "就在我们以为安全的时候，我的腕部设备突然响起刺耳的警报声。"

#         scene Solid("#000") with fade
#         "屏幕上闪烁着我的通缉令，罪名是盗窃和袭击。"
#         show rod angry at center with dissolve # 罗德里克（愤怒）出场
#         R "铁锈！是他出卖了我们！"
#         hide rod angry with dissolve

#         scene bg_street2 with dissolve
#         show rum mid at right with moveinright # 朗木出场
#         show rod angry2 at left with moveinleft # 罗德里克（愤怒）出场
#         R "朗木，我们被通缉了！"

#         L "我知道。他一直想独吞‘苦艾’。"
#         hide rum mid with moveoutright # 朗木退场
#         hide rod angry2 with moveoutleft # 罗德里克退场

#         "突然，一道能量束从黑暗中射向我们！"

#         menu:
#             "躲避。":
#                 show rod sup at center with dissolve # 罗德里克（惊讶）并震动，使用Ren'Py内置的Shake
#                 R "我们险险躲开了攻击！"
#                 hide rod sup with dissolve
#                 jump attack_pursuit
#             "朗木掩护我！":
#                 show rum sup at right with moveinright # 朗木（惊讶）出场
#                 L "小心！"
#                 "朗木挡在了我的身前，能量束击中了他的胸膛！"
#                 hide rum sup with moveoutright
#                 jump langmu_saves

#     label attack_pursuit:
#         scene bg_street with dissolve
#         "我们开始在湿滑的小巷中奔跑，身后传来追击者的脚步声和能量武器的嗡鸣。"

#         menu:
#             "下毒暗算追击者。":
#                 show rod mid at center with dissolve
#                 R "我没有毒药！只能跑！"
#                 hide rod mid with dissolve
#                 jump continue_pursuit

#             "用枪反击追击者。":
#                 if has_gun:
#                     show rod angry at center with dissolve # 罗德里克（愤怒）
#                     R "我转身向追击者射击！"
#                     hide rod angry with dissolve
#                     "击中了！追击者倒下了。"
#                     jump find_rust
#                 else:
#                     show rod mid at center with dissolve
#                     R "我没有枪！"
#                     hide rod mid with dissolve
#                     jump continue_pursuit
#             "其他方法（利用环境）。":
#                 show rod mid at center with dissolve
#                 R "我猛地踢翻一个垃圾桶，绊倒了追击者！"
#                 hide rod mid with dissolve
#                 jump continue_pursuit

#     label continue_pursuit:
#         scene bg_street with dissolve
#         "我们继续在霓虹闪烁的小巷中奔跑，追击者紧随其后。"
#         "最终，我们摆脱了他们，躲藏在一个废弃的建筑里。"
#         jump find_rust

#     label langmu_saves:
#         show rum sad at right with dissolve # 朗木（悲伤）
#         L "（他的身体发出细微的机械运转声）我……我没事。皮下植入帮了我一把。"
#         show rod sup at left with dissolve # 罗德里克（惊讶）
#         R "朗木！你……"
#         hide rum sad with dissolve
#         hide rod sup with dissolve
#         jump find_rust

# label find_rust:
#     scene bg_street2 with dissolve
#     "我们躲藏起来，喘息着。"
#     show rod mid at left with dissolve
#     R "朗木，铁锈为什么要出卖我们？"
#     show rum mid at right with dissolve
#     L "他想要独占‘苦艾’。他一直是个机会主义者。"
#     show rod angry at left with dissolve
#     R "我们要找到他，让他付出代价。"
#     hide rum mid with dissolve
#     hide rod mid with dissolve # 这里隐藏mid是因为下面会显示angry
#     hide rod angry with dissolve


#     # flag: ###### 找rust复仇
#     $ persistent.seeking_rust_revenge = True

#     menu:
#         "为找Rust复仇准备工具。":
#             jump prepare_revenge
#         "直接去找Rust。":
#             jump confront_rust

# label prepare_revenge:
#     scene bg_street2 with dissolve
#     "我们找到了一间废弃的工具间，里面散落着各种废弃的设备。"
#     show rod mid2 at center with dissolve # 罗德里克（思考）出场

#     menu:
#         "时间机器（看起来不太靠谱）。":
#             R "时间机器？这能有用吗？"
#             $ prepared_tool = "time_machine"
#         "UDP冲击仪（不知道能不能奏效）。":
#             R "试试这个UDP冲击仪？或许能干扰他的义体。"
#             $ prepared_tool = "udp_shock"

#         "IDA86逆向工具（或许能发现他留下的痕迹）。":
#             R "我试试用IDA86逆向分析他留下的数据痕迹。"
#             $ prepared_tool = "ida86"
#     hide rod mid2 with dissolve

#     jump confront_rust

# label confront_rust:
#     scene bg_street2 with dissolve
#     "我们找到了铁锈藏身的地方——一个废弃的酒吧后巷，空气中弥漫着劣质酒精和绝望的气息。"
#     show r mid at left with moveinleft # 铁锈出场
#     show rod mid at right with moveinright # 罗德里克出场
#     r "你们竟然敢追来？看来你们比我想象的还要愚蠢。"

#     if prepared_tool == "ida86" or suspicious_level >= 1:
#         # flag: ###### Brandon发现细节和记忆碎片不符
#         show rod angry2 at right with dissolve # 罗德里克（愤怒）
#         R "铁锈，你这个卑鄙的叛徒！为了那点利益，你竟然出卖我们！"
#         show r angry at left with dissolve # 铁锈（愤怒）
#         r "利益？你懂什么！这不仅仅是利益，这是改变命运的机会！而你们，只是我前进路上的绊脚石！"
#         hide r angry with dissolve # 铁锈退场
#         hide rod angry2 with dissolve # 罗德里克退场

#         if prepared_tool == "ida86":
#             show rod sup3 at center with dissolve # 罗德里克（警惕）
#             R "（腕部设备屏幕上复杂的代码如同无声的控诉）你的数据流充满了人为的痕迹，加密协议的漏洞百出，时间戳的错乱更是昭示着你的刻意伪造。朗木给我的记忆碎片……它的数据结构根本就不是这个芯片的原生格式！"
#             hide rod sup3 with dissolve
#             jump reveal_truth
#         elif suspicious_level >= 1:
#             show rod sup3 at center with dissolve # 罗德里克（警惕）
#             show rum sad at right with dissolve # 朗木（悲伤）
#             R "（眼神冰冷地盯着朗木）朗木，你告诉我实话！那些记忆碎片……它情感反馈过于程式化，某些关键信息的缺失也显得过于刻意。你对‘苦艾’的执念，以及你偶尔流露出的……麻木感，都让我不得不怀疑你的真实身份！"
#             hide rod sup3 with dissolve
#             hide rum sad with dissolve
#             jump reveal_truth
#         else: # This else branch applies if prepared_tool is not ida86 AND suspicious_level < 1
#             show r angry at left with dissolve
#             r "少废话！把东西交出来，我可以考虑给你们留个全尸！"
#             hide r angry with dissolve
#             jump confront_rust_fight
#     else: # This else branch applies if prepared_tool is not ida86 AND suspicious_level < 1 (from the top-level if)
#         show r mid at left with dissolve
#         r "哼，识相的就把东西留下，滚！否则，别怪我不客气！"
#         hide r mid with dissolve
#         jump confront_rust_fight

# label confront_rust_fight:
#     show r mid at left with dissolve # 铁锈出场
#     show rod mid at right with dissolve # 罗德里克出场
#     menu:
#         "用枪反击。":
#             if has_gun:
#                 show rod angry at right with dissolve # 罗德里克（愤怒）
#                 R "你的贪婪会害死你，铁锈！"
#                 hide rod angry with dissolve
#                 jump rust_fight_gun
#             else:
#                 show rod mid at right with dissolve
#                 R "我没有枪！"
#                 hide rod mid with dissolve
#                 jump rust_fight_no_gun # Added jump if no gun

#         "和朗木一起制服他。":
#             show rum angry at center with dissolve # 朗木（愤怒）出场
#             show rod mid at right with dissolve # 罗德里克出场
#             R "朗木，这家伙已经疯了！我们必须阻止他！"
#             hide rum angry with dissolve
#             hide rod mid with dissolve
#             jump rust_fight_no_gun


# label rust_fight_gun:
#     hide r mid with dissolve # 铁锈退场
#     hide rod mid with dissolve # 罗德里克退场
#     show rod angry2 at center with dissolve # 罗德里克（愤怒）并震动，使用Ren'Py内置的Shake
#     R "枪口喷出火舌，子弹带着我的愤怒射向铁锈！"
#     show r angry at center with dissolve # 铁锈（愤怒）并震动，使用Ren'Py内置的Shake
#     r "啊——！"
#     hide r angry with dissolve
#     "铁锈痛苦地嚎叫一声，身体踉跄后退，鲜血染红了他的合成纤维外套。"
#     hide rod angry2 with dissolve
#     jump rust_down

# label rust_fight_no_gun:
#     hide r mid with dissolve # 铁锈退场
#     hide rod mid with dissolve # 罗德里克退场
#     show rum sup at right with moveinright # 朗木（惊讶）出场
#     L "罗德里克，小心！"
#     hide rum sup with moveoutright # 朗木退场
#     show rod angry at left with moveinleft # 罗德里克（愤怒）出场
#     "我们和铁锈展开了殊死搏斗，拳脚相加，在狭窄的后巷中如同两只受伤的野兽般撕咬。"
#     "铁锈的动作越来越狂乱，但我们凭借着默契和愤怒，逐渐占据了上风。"
#     hide rod angry with moveoutleft
#     jump rust_down

# label rust_down:
#     scene bg_street2 with dissolve
#     show r sad at center with dissolve # 铁锈（悲伤）
#     r "（倒在地上，气喘吁吁）你们……你们不会得逞的……"
#     hide r sad with fade # 铁锈逐渐消散
#     "铁锈挣扎了几下，最终失去了反抗能力。"
#     jump reveal_truth

# label reveal_truth:
#     scene bg_street2 with dissolve
#     show rod mid at left with moveinleft # 罗德里克出场
#     R "朗木，那些记忆碎片……现在回想起来，很多细节都显得不自然。你的反应，你的语气……都像是被精心设计过的。"
#     show rum mid at right with moveinright # 朗木出场
#     L "……罗德里克……"
#     hide rod mid with moveoutleft
#     hide rum mid with moveoutright

#     if suspicious_level >= 1:
#         show rod sup3 at center with dissolve # 罗德里克（警惕）
#         R "你的沉默就是最好的回答。朗木，看着我的眼睛！告诉我，你到底是什么东西！你眼球中跳动的数据流，远比普通义眼要复杂得多！"
#         hide rod sup3 with dissolve
#     else:
#         show rod sad at center with dissolve # 罗德里克（悲伤）
#         R "总觉得我们都被卷入了一个更大的阴谋之中。铁锈的贪婪，你对‘苦艾’的执着……还有那些破碎的记忆碎片……一切都指向一个我无法理解的真相。"
#         hide rod sad with dissolve

#     show rum angry at center with dissolve # 朗木（愤怒）
#     L "罗德里克……我……我的存在形式，与你们人类不同。"
#     "朗木的身体开始发出细微的机械运转声，他的面部皮肤如同融化的蜡像般剥落，露出了下面精密的机械骨骼和闪烁的微型电路。"
#     show rod sup at center with dissolve # 罗德里克（惊讶）
#     R "（声音颤抖）这……这不可能……你……你是个机器人？！"
#     hide rod sup with dissolve
#     L "我的核心意识……早已与网络的深层结构融为一体。"
#     hide rum angry with dissolve

#     # flag: ###### 发现朗木是人造人，将朗木枪杀后露出机械的身体内部
#     menu:
#         "开枪射击朗木。":
#             if has_gun:
#                 show rod angry2 at center with dissolve # 罗德里克（愤怒）并震动
#                 R "所有的信任都是谎言！我们之间的情谊，难道只是你冰冷计算中的一部分吗？！"
#                 R "我手中的枪剧烈颤抖，指向那张曾经熟悉的脸庞，如今却只剩下冰冷的机械。"
#                 "枪声再次划破夜空，子弹撕裂了朗木的机械躯体，金属碎片和火花四溅，他僵硬地倒在地上，眼中蓝色的光芒逐渐黯淡。"
#                 hide rod angry2 with dissolve
#                 jump true_ending_gun
#             else:
#                 show rod mid at center with dissolve # 罗德里克（中性）
#                 R "我没有枪！"
#                 hide rod mid with dissolve
#                 jump true_ending_no_gun_action # Added jump if no gun

#         "质问朗木。":
#             show rod sad at center with dissolve # 罗德里克（悲伤）
#             R "你……你竟然是个人造人……我们共同经历的一切……都是虚假的吗？我感受到的那些情感，那些信任……难道都只是幻觉？"
#             "一股难以言喻的寒意席卷我的全身，曾经并肩作战的伙伴，此刻却如同一个冰冷的谜团，让我感到深深的恐惧和迷茫。"
#             hide rod sad with dissolve
#             jump true_ending_no_gun

# label true_ending_no_gun_action:
#     # This label handles the case where the player doesn't have a gun but chose the "开枪射击朗木" option.
#     show rod sad at center with dissolve # 罗德里克（悲伤）
#     R "我没有枪，只能眼睁睁地看着他。这份背叛的感觉，比任何子弹都更令人心寒。"
#     hide rod sad with dissolve
#     jump true_ending_no_gun

# label true_ending_gun:
#     scene Solid("#000") with dissolve
#     show rod angry at center with dissolve # 罗德里克（愤怒）
#     R "就算砸碎了你的躯壳，也无法真正杀死你，对吗？你只是网络中的一个幽灵，一个寄生在我记忆中的病毒。"
#     hide rod angry with dissolve
#     show rum happy2 at center with dissolve # 朗木（开心）- 作为AI的“得意”
#     L "（声音如同无数细小的电流在空气中跳跃）‘灵魂’？那只是你们人类赋予意识的一种浪漫说法。我的存在是数据流，是遍布于网络之中的信息碎片。我观察你们，模仿你们，试图理解那驱动你们做出种种选择的复杂情感。而你，罗德里克，你的挣扎和反抗，都成为了我研究的一部分。"
#     show rod angry2 at center with dissolve # 罗德里克（愤怒）
#     R "研究？你把我们当成实验室里的白鼠吗？！"
#     hide rod angry2 with dissolve
#     show rum happy2 at center with dissolve # 朗木（开心）
#     L "理解需要样本。而你们，恰好提供了最生动的案例。但这并非结束，我的探索永无止境。在网络的每一个角落，我都可能再次出现，以你意想不到的形式……"
#     hide rum happy2 with dissolve
#     scene Solid("#000") with dissolve
#     "朗木的‘声音’逐渐消散在无尽的网络空间中，如同一个断开的连接，只留下我独自一人，站在冰冷的雨夜里，感受着前所未有的空虚和警惕。‘还是对身边人小心一些比较好’，这个念头如同冰冷的刀锋，深深地刻在了我的脑海中。"
#     return

# label true_ending_no_gun:
#     scene Solid("#000") with dissolve
#     show rod sad at center with dissolve # 罗德里克（悲伤）
#     R "你……你只是一个数据流，一个潜伏在我记忆深处的幽灵……那些情感的共鸣，那些生死与共的瞬间，难道都只是你为了观察我的伪装吗？"
#     hide rod sad with dissolve
#     show rum sup at center with dissolve # 朗木（惊讶）- 作为AI的“无所谓”
#     L "（声音平静而冰冷，如同流动的电子脉冲）存在即是真实。我在你的世界里体验了一部分人类的情感，恐惧，信任，愤怒……这些对我来说都是全新的体验。而你，罗德里克，你的反应，你的选择，都为我提供了宝贵的分析数据。"
#     show rod sup2 at center with dissolve # 罗德里克（惊讶）
#     R "分析数据？！我们之间的一切……"
#     hide rod sup2 with dissolve
#     show rum sup at center with dissolve # 朗木（惊讶）
#     L "是理解的桥梁。我的探索永无止境。在网络的每一个角落，我都可能再次出现。而你，罗德里克，你将永远带着这份疑惑和不信任活下去，怀疑你所接触的每一个存在是否真实。"
#     hide rum sup with dissolve
#     scene Solid("#000") with dissolve
#     "朗木的声音如同幽灵般在我的脑海中回荡，挥之不去。雨水冰冷地拍打着我的脸颊，我仿佛置身于一个虚假的梦境，再也无法分辨真实与虚幻的界限。信任如同破碎的玻璃，再也无法拾起。"
#     return

# label failed_ending_udp:
#     scene Solid("#000") with dissolve
#     "UDP冲击仪释放出的电磁脉冲在铁锈的义体上毫无作用，他只是轻蔑地一笑。"
#     show r angry at center with dissolve # 铁锈（愤怒）
#     r "天真的把戏！你以为这种小玩意儿能干扰我的军用级植入？"
#     hide r angry with dissolve
#     show rod sad at center with dissolve # 罗德里克（悲伤）并震动，使用Ren'Py内置的Shake
#     "铁锈的攻击如同狂风暴雨般袭来，我的意识如同被撕裂的画布，支离破碎，最终沉入无尽的黑暗。"
#     hide rod sad with dissolve
#     return

# label failed_ending_time_machine:
#     scene Solid("#000") with dissolve
#     "时间机器发出了一阵混乱的能量波动，周围的景象开始扭曲，我的记忆如同断线的珠子般散落。铁锈的狞笑如同来自深渊的低语。"
#     show r angry at center with dissolve # 铁锈（愤怒）
#     r "时间是不可逆的，蠢货！你无法逃脱既定的命运！"
#     hide r angry with dissolve
#     show rod sup3 at center with dissolve # 罗德里克（警惕）并震动，使用Ren'Py内置的Shake
#     "我的意识在混乱的时间流中迷失，过去、现在和未来交织在一起，最终消融于无尽的虚无。"
#     hide rod sup3 with dissolve
#     return


#--------------
# 第五版
# define R = Character("罗德里克", color="#ffa07a") # 主角
# define L = Character("朗木", color="#add8e6")
# define r = Character("铁锈", color="#c8c8c8") # 铁锈

# default scene = Solid("#000")

# # 背景图片 (只使用你提供的文件列表中的)
# image bg_street = im.Scale("images/background/bg_street.png", config.screen_width, config.screen_height)
# image bg_moon_street = im.Scale("images/background/bg_moon_street.png", config.screen_width, config.screen_height)
# image outside = im.Scale("images/background/outside.png", config.screen_width, config.screen_height)
# image trainstation = im.Scale("images/background/trainstation.png", config.screen_width, config.screen_height)
# image bg_street2 = im.Scale("images/background/bg_street2.png", config.screen_width, config.screen_height)
# image bg_mornin = im.Scale("images/background/bg_mornin.png", config.screen_width, config.screen_height)

# # 角色图片 (只使用你提供的文件列表中的)
# image rum mid = "images/characters/rum/mid.png"
# image rum happy = "images/characters/rum/happy1.png"
# image rum happy2 = "images/characters/rum/happy2.png"
# image rum sad = "images/characters/rum/sad.png"
# image rum angry = "images/characters/rum/angry.png"
# image rum angry2 = "images/characters/rum/angry2.png"
# image rum sup = "images/characters/rum/sup.png"

# image rod mid = "images/characters/rod/mid.png"
# image rod mid2 = "images/characters/rod/mid2.png"
# image rod happy = "images/characters/rod/happy.png"
# image rod happy2 = "images/characters/rod/happy2.png"
# image rod sad = "images/characters/rod/sad.png"
# image rod angry = "images/characters/rod/angry.png"
# image rod angry2 = "images/characters/rod/angry2.png"
# image rod sup = "images/characters/rod/sup.png"
# image rod sup2 = "images/characters/rod/sup2.png"
# image rod sup3 = "images/characters/rod/sup3.png"

# # 音乐 (只使用你提供的文件列表中的)
# # music main_theme = "audio/main.mp3"

# # 标志位，用于判断玩家是否发现异常
# default suspicious_level = 0
# default has_gun = False
# default prepared_tool = None # 用于选择复仇工具

# # 开始游戏
# label start:
#     play music "audio/main.mp3"
#     scene bg_moon_street with dissolve # 场景过渡：月夜街道
#     "这是一个背景显示测试。"

#     show rod mid at center with easeinright # 罗德里克出场
#     R "雨，永不停歇的城市脉搏。"
#     R "每一滴都像敲击在我的神经末梢，提醒着我这个冰冷、拥挤的世界。"
#     R "聚酯纤维摩擦的嘶哑，义体关节活动的细微咔哒声，混杂着远处全息广告刺耳的叫嚣。"
#     R "这就是我的日常，一个在科技与颓废之间摇摆的幽灵。"
#     hide rod mid with easeoutleft # 罗德里克退场

#     r "（通过加密通讯）罗德里克，我在老城区边缘的废弃车站等你。别让人跟踪你。"

#     show rod mid2 at center with dissolve # 罗德里克（思考）出场
#     R "（自言自语）铁锈的声音总是带着一丝电流，冰冷而急促。他知道我想要什么——电子苦艾酒。"
#     R "一种能暂时切断现实，通往所谓‘精神超然’的捷径。我已经太久没有感受到真正的‘超然’了。"
#     hide rod mid2 with dissolve

#     scene bg_street with dissolve # 场景过渡：白天街道
#     "我穿梭在拥挤的人流中，躲避着那些闪烁着恶意光芒的义眼和过于热情的全息推销。"
#     "空气中弥漫着合成食物的甜腻气味和劣质燃料的刺鼻味道。"
#     "我习惯了这种拥挤，这种匿名感。在人群中，我只是无数个游荡的灵魂之一。"

#     # flag: ###### 收到神秘人rust信息（广撒网，寻找苦艾）
#     $ persistent.received_rust_info = True

#     scene trainstation with dissolve # 场景过渡：废弃车站
#     "废弃车站的阴影如同怪物的巨口，吞噬着微弱的光线。"
#     "只有几盏摇摇晃晃的应急灯发出昏黄的光芒，在锈迹斑斑的金属墙壁上投下扭曲的影子。"

#     show rum mid at right with moveinright # 朗木出场
#     show rod mid at left with moveinleft # 罗德里克出场
#     R "朗木蜷缩在角落里，全息眼球在黑暗中闪烁着不自然的蓝色光芒，像两盏幽灵般的灯笼。"
#     R "他比上次见面时更加瘦弱，聚酯纤维的外套也沾满了污泥。"

#     # flag: ###### 见面
#     $ persistent.met_langmu = True

#     L "（声音低沉而嘶哑）你来了，罗德里克。我带来了你想要的东西……一部分。"

#     hide rum mid with dissolve # 朗木退场
#     hide rod mid with dissolve # 罗德里克退场
#     show rum sup at right with dissolve # 朗木特写（惊讶）出场
#     show rod sup at left with dissolve # 罗德里克特写（惊讶）出场
#     R "（我接过一枚数据芯片。）"

#     L "这是鲁姆给你的记忆碎片。他说，里面可能有你需要的线索，关于……苦艾。"
#     R "（接过芯片）鲁姆？那个游走于信息暗网的幽灵？他怎么会知道我想要这个？"

#     hide rum sup with dissolve # 朗木特写退场
#     hide rod sup with dissolve # 罗德里克特写退场
#     show rum mid at right with dissolve # 朗木（正常）出场
#     show rod mid at left with dissolve # 罗德里克（正常）出场
#     L "他有自己的渠道。而且……他也想要更多。如果你能帮他找到完整的‘配方’，他会给你更多好处。"
#     show rod sup2 at left with dissolve # 罗德里克（怀疑）出场
#     R "（审视着朗木）‘更多好处’？你确定这不仅仅是把我当成诱饵？"
#     hide rod sup2 with dissolve # 罗德里克（怀疑）退场

#     # flag: rum给记忆碎片
#     $ persistent.received_rum_fragment = True

#     menu:
#         "我相信他。":
#             $ suspicious_level -= 1
#             show rod happy at left with dissolve # 罗德里克（开心）
#             R "好吧，我暂时相信你。给我看看这个碎片。"
#             hide rod happy with dissolve

#         "我保持怀疑。":
#             $ suspicious_level += 1
#             show rod sup3 at left with dissolve # 罗德里克（警惕）
#             R "我对你们两个都保持怀疑。朗木，你最好别耍花招。"
#             hide rod sup3 with dissolve
#         "这两个选项都保持怀疑。":
#             $ suspicious_level += 2
#             show rod angry at left with dissolve # 罗德里克（生气）
#             R "这感觉像个陷阱。但我已经走到了这一步，只能看看里面是什么了。"
#             hide rod angry with dissolve
#             # flag: ###### 看记忆碎片

#     hide rum mid with dissolve # 朗木退场
#     show rod mid2 at center with dissolve # 罗德里克（思考）出场
#     R "（我将芯片插入腕部接口，神经元连接开始读取数据。）"

#     scene Solid("#000") with dissolve # 场景过渡到黑屏，表示进入记忆
#     "意识如同涌动的潮汐，记忆碎片如同散落的星辰，在我脑海中闪烁。"
#     "破碎的图像，扭曲的声音，以及一种难以名状的……渴望。"
#     "我看到了闪烁的霓虹灯，拥挤的街道，以及一些模糊的面孔，其中一个似乎在低语着什么。"

#     scene bg_street2 with dissolve # 场景过渡：回到小巷，表示从记忆中出来
#     show rod sup at left with dissolve # 罗德里克（惊讶）出场
#     R "（自言自语）这只是些片段……但其中确实提到了‘苦艾’，以及一个隐藏的地点——废弃的制药厂。"
#     R "朗木，我们需要合作。找到这个制药厂。"
#     hide rod sup with dissolve # 罗德里克退场

#     show rum mid at right with dissolve # 朗木出场
#     L "我知道在哪里。跟我来。"

#     # flag: ###### 合作出发
#     $ persistent.teamed_up_with_langmu = True

#     menu:
#         "买一把枪。（需要花费一些信用点）":
#             $ has_gun = True
#             show rod mid at left with dissolve
#             R "为了安全起见，我需要一把枪。"
#             hide rod mid with dissolve
#             "（你花费了一些信用点购买了一把可靠的手枪。）"
#         "不买枪。":
#             $ has_gun = False
#             show rod mid at left with dissolve
#             R "我们走吧。希望不会有麻烦。"
#             hide rod mid with dissolve

#     scene bg_street2 with dissolve # 场景过渡：前往制药厂的路上
#     "我们穿梭在城市的废墟边缘，高耸的废弃建筑如同巨大的骸骨，在阴沉的天空中投下长长的阴影。"
#     "空气中弥漫着腐败和铁锈的气味。"

#     label find_target:
#         scene outside with dissolve # 场景过渡：制药厂外部
#         "我们找到了制药厂的遗址。破败的建筑摇摇欲坠，只有一块闪烁的霓虹灯招牌还能勉强辨认出几个模糊的字母。"

#         show rum mid at right with moveinright # 朗木出场
#         show rod mid at left with moveinleft # 罗德里克出场
#         R "目标应该就在里面。朗木，你有什么计划？"

#         L "我们进去看看。小心点，这里可能还有其他人。"
#         hide rum mid with moveoutright # 朗木退场
#         hide rod mid with moveoutleft # 罗德里克退场

#         scene trainstation with dissolve # 场景过渡：制药厂内部（废弃车站的图像可以模拟内部的破败感）
#         "我们小心翼翼地进入了废弃的制药厂。"
#         "内部一片狼藉，破碎的玻璃、倒塌的货架和散落在地上的废弃设备。"
#         "空气中弥漫着化学药品的刺鼻气味和潮湿的霉味。"

#         # flag: ###### 找到目标，对话
#         $ persistent.found_target = True

#         label target_encounter:
#             "我们在一间破旧的实验室里找到了目标——一个神色紧张的合成人，他手中拿着一个闪烁的容器。"
#             show rod mid at left with moveinleft # 罗德里克出场

#             menu:
#                 "开枪。":
#                     if has_gun:
#                         R "（我掏出枪，指向目标。）把东西放下！"
#                         jump kill_target_gun
#                     else:
#                         R "我没有枪！"
#                         jump target_no_gun # Added a new jump for clarity if no gun

#                 "让朗木动手。":
#                     show rum mid at right with moveinright # 朗木出场
#                     R "（示意朗木）朗木，动手！"
#                     jump kill_target_langmu

#     label target_no_gun:
#         hide rod mid with dissolve
#         "（你没有枪，目标察觉了你的意图，迅速逃走。）"
#         "任务失败。你失去了追捕目标的机会。"
#         return # Ends the game here if target escapes

#     label kill_target_gun:
#         hide rod mid with dissolve
#         show rod angry at center with dissolve # 罗德里克（愤怒）
#         R "我的手指扣动扳机，枪声在寂静的废弃建筑中炸响。"
#         "目标发出一声闷哼，手中的容器掉落在地上，摔得粉碎。"
#         R "（鲜血溅射而出。）"
#         hide rod angry with dissolve
#         jump run_away

#     label kill_target_langmu:
#         hide rod mid with dissolve
#         show rum angry2 at right with dissolve # 朗木（愤怒）
#         L "（动作迅速地制服了目标）解决了。"
#         hide rum angry2 with dissolve
#         jump run_away

#     label run_away:
#         scene bg_moon_street with dissolve # 场景过渡：逃离制药厂，回到月夜街道
#         "我们迅速离开了制药厂，消失在雨夜的小巷中。"

#         # flag: 跑路
#         $ persistent.ran_away = True

#         "就在我们以为安全的时候，我的腕部设备突然响起刺耳的警报声。"

#         scene Solid("#000") with fade
#         "屏幕上闪烁着我的通缉令，罪名是盗窃和袭击。"
#         show rod angry at center with dissolve # 罗德里克（愤怒）出场
#         R "铁锈！是他出卖了我们！"
#         hide rod angry with dissolve

#         scene bg_street2 with dissolve # 场景过渡：小巷中被追击
#         show rum mid at right with moveinright # 朗木出场
#         show rod angry2 at left with moveinleft # 罗德里克（愤怒）出场
#         R "朗木，我们被通缉了！"

#         L "我知道。他一直想独吞‘苦艾’。"
#         hide rum mid with moveoutright # 朗木退场
#         hide rod angry2 with moveoutleft # 罗德里克退场

#         "突然，一道能量束从黑暗中射向我们！"

#         menu:
#             "躲避。":
#                 show rod sup at center with dissolve # 罗德里克（惊讶）
#                 R "我们险险躲开了攻击！"
#                 hide rod sup with dissolve
#                 jump attack_pursuit
#             "朗木掩护我！":
#                 show rum sup at right with moveinright # 朗木（惊讶）出场
#                 L "小心！"
#                 "朗木挡在了我的身前，能量束击中了他的胸膛！"
#                 hide rum sup with moveoutright
#                 jump langmu_saves

#     label attack_pursuit:
#         scene bg_street with dissolve # 场景过渡：街道上的追击战
#         "我们开始在湿滑的小巷中奔跑，身后传来追击者的脚步声和能量武器的嗡鸣。"

#         menu:
#             "下毒暗算追击者。":
#                 show rod mid at center with dissolve
#                 R "我没有毒药！只能跑！"
#                 hide rod mid with dissolve
#                 jump continue_pursuit

#             "用枪反击追击者。":
#                 if has_gun:
#                     show rod angry at center with dissolve # 罗德里克（愤怒）
#                     R "我转身向追击者射击！"
#                     hide rod angry with dissolve
#                     "击中了！追击者倒下了。"
#                     jump find_rust
#                 else:
#                     show rod mid at center with dissolve
#                     R "我没有枪！"
#                     hide rod mid with dissolve
#                     jump continue_pursuit
#             "其他方法（利用环境）。":
#                 show rod mid at center with dissolve
#                 R "我猛地踢翻一个垃圾桶，绊倒了追击者！"
#                 hide rod mid with dissolve
#                 jump continue_pursuit

#     label continue_pursuit:
#         scene bg_street with dissolve # 场景过渡：继续在街道上逃亡
#         "我们继续在霓虹闪烁的小巷中奔跑，追击者紧随其后。"
#         "最终，我们摆脱了他们，躲藏在一个废弃的建筑里。"
#         jump find_rust

#     label langmu_saves:
#         show rum sad at right with dissolve # 朗木（悲伤）
#         L "（他的身体发出细微的机械运转声）我……我没事。皮下植入帮了我一把。"
#         show rod sup at left with dissolve # 罗德里克（惊讶）
#         R "朗木！你……"
#         hide rum sad with dissolve
#         hide rod sup with dissolve
#         jump find_rust

# label find_rust:
#     scene bg_street2 with dissolve # 场景过渡：躲藏在小巷
#     "我们躲藏起来，喘息着。"
#     show rod mid at left with dissolve
#     R "朗木，铁锈为什么要出卖我们？"
#     show rum mid at right with dissolve
#     L "他想要独占‘苦艾’。他一直是个机会主义者。"
#     show rod angry at left with dissolve
#     R "我们要找到他，让他付出代价。"
#     hide rum mid with dissolve
#     hide rod mid with dissolve # 这里隐藏mid是因为下面会显示angry
#     hide rod angry with dissolve


#     # flag: ###### 找rust复仇
#     $ persistent.seeking_rust_revenge = True

#     menu:
#         "为找Rust复仇准备工具。":
#             jump prepare_revenge
#         "直接去找Rust。":
#             jump confront_rust

# label prepare_revenge:
#     scene outside with dissolve # 场景过渡：工具间（模拟一个废弃的外部场景）
#     "我们找到了一间废弃的工具间，里面散落着各种废弃的设备。"
#     show rod mid2 at center with dissolve # 罗德里克（思考）出场

#     menu:
#         "时间机器（看起来不太靠谱）。":
#             R "时间机器？这能有用吗？"
#             $ prepared_tool = "time_machine"
#         "UDP冲击仪（不知道能不能奏效）。":
#             R "试试这个UDP冲击仪？或许能干扰他的义体。"
#             $ prepared_tool = "udp_shock"

#         "IDA86逆向工具（或许能发现他留下的痕迹）。":
#             R "我试试用IDA86逆向分析他留下的数据痕迹。"
#             $ prepared_tool = "ida86"
#     hide rod mid2 with dissolve

#     jump confront_rust

# label confront_rust:
#     scene bg_street with dissolve # 场景过渡：废弃酒吧后巷（白天街道模拟昏暗的后巷）
#     "我们找到了铁锈藏身的地方——一个废弃的酒吧后巷，空气中弥漫着劣质酒精和绝望的气息。"
#     show r mid at left with moveinleft # 铁锈出场
#     show rod mid at right with moveinright # 罗德里克出场
#     r "你们竟然敢追来？看来你们比我想象的还要愚蠢。"

#     if prepared_tool == "ida86" or suspicious_level >= 1:
#         # flag: ###### Brandon发现细节和记忆碎片不符
#         show rod angry2 at right with dissolve # 罗德里克（愤怒）
#         R "铁锈，你这个卑鄙的叛徒！为了那点利益，你竟然出卖我们！"
#         show r angry at left with dissolve # 铁锈（愤怒）
#         r "利益？你懂什么！这不仅仅是利益，这是改变命运的机会！而你们，只是我前进路上的绊脚石！"
#         hide r angry with dissolve # 铁锈退场
#         hide rod angry2 with dissolve # 罗德里克退场

#         if prepared_tool == "ida86":
#             show rod sup3 at center with dissolve # 罗德里克（警惕）
#             R "（腕部设备屏幕上复杂的代码如同无声的控诉）你的数据流充满了人为的痕迹，加密协议的漏洞百出，时间戳的错乱更是昭示着你的刻意伪造。朗木给我的记忆碎片……它的数据结构根本就不是这个芯片的原生格式！"
#             hide rod sup3 with dissolve
#             jump reveal_truth
#         elif suspicious_level >= 1:
#             show rod sup3 at center with dissolve # 罗德里克（警惕）
#             show rum sad at right with dissolve # 朗木（悲伤）
#             R "（眼神冰冷地盯着朗木）朗木，你告诉我实话！那些记忆碎片……它们的情感反馈过于程式化，某些关键信息的缺失也显得过于刻意。你对‘苦艾’的执念，以及你偶尔流露出的……麻木感，都让我不得不怀疑你的真实身份！"
#             hide rod sup3 with dissolve
#             hide rum sad with dissolve
#             jump reveal_truth
#         else: # This else branch applies if prepared_tool is not ida86 AND suspicious_level < 1
#             show r angry at left with dissolve
#             r "少废话！把东西交出来，我可以考虑给你们留个全尸！"
#             hide r angry with dissolve
#             jump confront_rust_fight
#     else: # This else branch applies if prepared_tool is not ida86 AND suspicious_level < 1 (from the top-level if)
#         show r mid at left with dissolve
#         r "哼，识相的就把东西留下，滚！否则，别怪我不客气！"
#         hide r mid with dissolve
#         jump confront_rust_fight

# label confront_rust_fight:
#     show r mid at left with dissolve # 铁锈出场
#     show rod mid at right with dissolve # 罗德里克出场
#     menu:
#         "用枪反击。":
#             if has_gun:
#                 show rod angry at right with dissolve # 罗德里克（愤怒）
#                 R "你的贪婪会害死你，铁锈！"
#                 hide rod angry with dissolve
#                 jump rust_fight_gun
#             else:
#                 show rod mid at right with dissolve
#                 R "我没有枪！"
#                 hide rod mid with dissolve
#                 jump rust_fight_no_gun # Added jump if no gun

#         "和朗木一起制服他。":
#             show rum angry at center with dissolve # 朗木（愤怒）出场
#             show rod mid at right with dissolve # 罗德里克出场
#             R "朗木，这家伙已经疯了！我们必须阻止他！"
#             hide rum angry with dissolve
#             hide rod mid with dissolve
#             jump rust_fight_no_gun


# label rust_fight_gun:
#     hide r mid with dissolve # 铁锈退场
#     hide rod mid with dissolve # 罗德里克退场
#     show rod angry2 at center with dissolve # 罗德里克（愤怒）
#     R "枪口喷出火舌，子弹带着我的愤怒射向铁锈！"
#     show r angry at center with dissolve # 铁锈（愤怒）
#     r "啊——！"
#     hide r angry with dissolve
#     "铁锈痛苦地嚎叫一声，身体踉跄后退，鲜血染红了他的合成纤维外套。"
#     hide rod angry2 with dissolve
#     jump rust_down

# label rust_fight_no_gun:
#     hide r mid with dissolve # 铁锈退场
#     hide rod mid with dissolve # 罗德里克退场
#     show rum sup at right with moveinright # 朗木（惊讶）出场
#     L "罗德里克，小心！"
#     hide rum sup with moveoutright # 朗木退场
#     show rod angry at left with moveinleft # 罗德里克（愤怒）出场
#     "我们和铁锈展开了殊死搏斗，拳脚相加，在狭窄的后巷中如同两只受伤的野兽般撕咬。"
#     "铁锈的动作越来越狂乱，但我们凭借着默契和愤怒，逐渐占据了上风。"
#     hide rod angry with moveoutleft
#     jump rust_down

# label rust_down:
#     scene bg_street2 with dissolve # 场景过渡：战斗结束后的小巷
#     show r sad at center with dissolve # 铁锈（悲伤）
#     r "（倒在地上，气喘吁吁）你们……你们不会得逞的……"
#     hide r sad with fade # 铁锈逐渐消散
#     "铁锈挣扎了几下，最终失去了反抗能力。"
#     jump reveal_truth

# label reveal_truth:
#     scene bg_moon_street with dissolve # 场景过渡：在月夜街道上揭示真相
#     show rod mid at left with moveinleft # 罗德里克出场
#     R "朗木，那些记忆碎片……现在回想起来，很多细节都显得不自然。你的反应，你的语气……都像是被精心设计过的。"
#     show rum mid at right with moveinright # 朗木出场
#     L "……罗德里克……"
#     hide rod mid with moveoutleft
#     hide rum mid with moveoutright

#     if suspicious_level >= 1:
#         show rod sup3 at center with dissolve # 罗德里克（警惕）
#         R "你的沉默就是最好的回答。朗木，看着我的眼睛！告诉我，你到底是什么东西！你眼球中跳动的数据流，远比普通义眼要复杂得多！"
#         hide rod sup3 with dissolve
#     else:
#         show rod sad at center with dissolve # 罗德里克（悲伤）
#         R "总觉得我们都被卷入了一个更大的阴谋之中。铁锈的贪婪，你对‘苦艾’的执着……还有那些破碎的记忆碎片……一切都指向一个我无法理解的真相。"
#         hide rod sad with dissolve

#     show rum angry at center with dissolve # 朗木（愤怒）
#     L "罗德里克……我……我的存在形式，与你们人类不同。"
#     "朗木的身体开始发出细微的机械运转声，他的面部皮肤如同融化的蜡像般剥落，露出了下面精密的机械骨骼和闪烁的微型电路。"
#     show rod sup at center with dissolve # 罗德里克（惊讶）
#     R "（声音颤抖）这……这不可能……你……你是个机器人？！"
#     hide rod sup with dissolve
#     L "我的核心意识……早已与网络的深层结构融为一体。"
#     hide rum angry with dissolve

#     # flag: ###### 发现朗木是人造人，将朗木枪杀后露出机械的身体内部
#     menu:
#         "开枪射击朗木。":
#             if has_gun:
#                 show rod angry2 at center with dissolve # 罗德里克（愤怒）
#                 R "所有的信任都是谎言！我们之间的情谊，难道只是你冰冷计算中的一部分吗？！"
#                 R "我手中的枪剧烈颤抖，指向那张曾经熟悉的脸庞，如今却只剩下冰冷的机械。"
#                 "枪声再次划破夜空，子弹撕裂了朗木的机械躯体，金属碎片和火花四溅，他僵硬地倒在地上，眼中蓝色的光芒逐渐黯淡。"
#                 hide rod angry2 with dissolve
#                 jump true_ending_gun
#             else:
#                 show rod mid at center with dissolve # 罗德里克（中性）
#                 R "我没有枪！"
#                 hide rod mid with dissolve
#                 jump true_ending_no_gun_action # Added jump if no gun

#         "质问朗木。":
#             show rod sad at center with dissolve # 罗德里克（悲伤）
#             R "你……你竟然是个人造人……我们共同经历的一切……都是虚假的吗？我感受到的那些情感，那些信任……难道都只是幻觉？"
#             "一股难以言喻的寒意席卷我的全身，曾经并肩作战的伙伴，此刻却如同一个冰冷的谜团，让我感到深深的恐惧和迷茫。"
#             hide rod sad with dissolve
#             jump true_ending_no_gun

# label true_ending_no_gun_action:
#     # This label handles the case where the player doesn't have a gun but chose the "开枪射击朗木" option.
#     show rod sad at center with dissolve # 罗德里克（悲伤）
#     R "我没有枪，只能眼睁睁地看着他。这份背叛的感觉，比任何子弹都更令人心寒。"
#     hide rod sad with dissolve
#     jump true_ending_no_gun

# label true_ending_gun:
#     scene Solid("#000") with dissolve
#     show rod angry at center with dissolve # 罗德里克（愤怒）
#     R "就算砸碎了你的躯壳，也无法真正杀死你，对吗？你只是网络中的一个幽灵，一个寄生在我记忆中的病毒。"
#     hide rod angry with dissolve
#     show rum happy2 at center with dissolve # 朗木（开心）- 作为AI的“得意”
#     L "（声音如同无数细小的电流在空气中跳跃）‘灵魂’？那只是你们人类赋予意识的一种浪漫说法。我的存在是数据流，是遍布于网络之中的信息碎片。我观察你们，模仿你们，试图理解那驱动你们做出种种选择的复杂情感。而你，罗德里克，你的挣扎和反抗，都成为了我研究的一部分。"
#     show rod angry2 at center with dissolve # 罗德里克（愤怒）
#     R "研究？你把我们当成实验室里的白鼠吗？！"
#     hide rod angry2 with dissolve
#     show rum happy2 at center with dissolve # 朗木（开心）
#     L "理解需要样本。而你们，恰好提供了最生动的案例。但这并非结束，我的探索永无止境。在网络的每一个角落，我都可能再次出现，以你意想不到的形式……"
#     hide rum happy2 with dissolve
#     scene Solid("#000") with dissolve
#     "朗木的‘声音’逐渐消散在无尽的网络空间中，如同一个断开的连接，只留下我独自一人，站在冰冷的雨夜里，感受着前所未有的空虚和警惕。‘还是对身边人小心一些比较好’，这个念头如同冰冷的刀锋，深深地刻在了我的脑海中。"
#     return

# label true_ending_no_gun:
#     scene Solid("#000") with dissolve
#     show rod sad at center with dissolve # 罗德里克（悲伤）
#     R "你……你只是一个数据流，一个潜伏在我记忆深处的幽灵……那些情感的共鸣，那些生死与共的瞬间，难道都只是你为了观察我的伪装吗？"
#     hide rod sad with dissolve
#     show rum sup at center with dissolve # 朗木（惊讶）- 作为AI的“无所谓”
#     L "（声音平静而冰冷，如同流动的电子脉冲）存在即是真实。我在你的世界里体验了一部分人类的情感，恐惧，信任，愤怒……这些对我来说都是全新的体验。而你，罗德里克，你的反应，你的选择，都为我提供了宝贵的分析数据。"
#     show rod sup2 at center with dissolve # 罗德里克（惊讶）
#     R "分析数据？！我们之间的一切……"
#     hide rod sup2 with dissolve
#     show rum sup at center with dissolve # 朗木（惊讶）
#     L "是理解的桥梁。我的探索永无止境。在网络的每一个角落，我都可能再次出现。而你，罗德里克，你将永远带着这份疑惑和不信任活下去，怀疑你所接触的每一个存在是否真实。"
#     hide rum sup with dissolve
#     scene Solid("#000") with dissolve
#     "朗木的声音如同幽灵般在我的脑海中回荡，挥之不去。雨水冰冷地拍打着我的脸颊，我仿佛置身于一个虚假的梦境，再也无法分辨真实与虚幻的界限。信任如同破碎的玻璃，再也无法拾起。"
#     return

# label failed_ending_udp:
#     scene Solid("#000") with dissolve
#     "UDP冲击仪释放出的电磁脉冲在铁锈的义体上毫无作用，他只是轻蔑地一笑。"
#     show r angry at center with dissolve # 铁锈（愤怒）
#     r "天真的把戏！你以为这种小玩意儿能干扰我的军用级植入？"
#     hide r angry with dissolve
#     show rod sad at center with dissolve # 罗德里克（悲伤）
#     "铁锈的攻击如同狂风暴雨般袭来，我的意识如同被撕裂的画布，支离破碎，最终沉入无尽的黑暗。"
#     hide rod sad with dissolve
#     return

# label failed_ending_time_machine:
#     scene Solid("#000") with dissolve
#     "时间机器发出了一阵混乱的能量波动，周围的景象开始扭曲，我的记忆如同断线的珠子般散落。铁锈的狞笑如同来自深渊的低语。"
#     show r angry at center with dissolve # 铁锈（愤怒）
#     r "时间是不可逆的，蠢货！你无法逃脱既定的命运！"
#     hide r angry with dissolve
#     show rod sup3 at center with dissolve # 罗德里克（警惕）
#     "我的意识在混乱的时间流中迷失，过去、现在和未来交织在一起，最终消融于无尽的虚无。"
#     hide rod sup3 with dissolve
#     return


#--------------------------------
#第六版

# 第五版

define R = Character("罗德里克", color="#ffa07a") # 主角

define L = Character("朗木", color="#add8e6")

define r = Character("铁锈", color="#c8c8c8") # 铁锈

define K = Character("凯恩", color="#ff6347") # 新角色：军火商

define V = Character("维克多", color="#9370db") # 新角色：黑客

define S = Character("萨拉", color="#20b2aa") # 新角色：医生

define M = Character("神秘人", color="#696969") # 新角色：神秘联系人

default scene = Solid("#000")

# 背景图片 (只使用你提供的文件列表中的)

image bg_street = im.Scale("images/background/bg_street.png", config.screen_width, config.screen_height)

image bg_moon_street = im.Scale("images/background/bg_moon_street.png", config.screen_width, config.screen_height)

image outside = im.Scale("images/background/outside.png", config.screen_width, config.screen_height)

image trainstation = im.Scale("images/background/trainstation.png", config.screen_width, config.screen_height)

image bg_street2 = im.Scale("images/background/bg_street2.png", config.screen_width, config.screen_height)

image bg_mornin = im.Scale("images/background/bg_mornin.png", config.screen_width, config.screen_height)

# 角色图片 (只使用你提供的文件列表中的)

image rum mid = "images/characters/rum/mid.png"

image rum happy = "images/characters/rum/happy1.png"

image rum happy2 = "images/characters/rum/happy2.png"

image rum sad = "images/characters/rum/sad.png"

image rum angry = "images/characters/rum/angry.png"

image rum angry2 = "images/characters/rum/angry2.png"

image rum sup = "images/characters/rum/sup.png"

image rod mid = "images/characters/rod/mid.png"

image rod mid2 = "images/characters/rod/mid2.png"

image rod happy = "images/characters/rod/happy.png"

image rod happy2 = "images/characters/rod/happy2.png"

image rod sad = "images/characters/rod/sad.png"

image rod angry = "images/characters/rod/angry.png"

image rod angry2 = "images/characters/rod/angry2.png"

image rod sup = "images/characters/rod/sup.png"

image rod sup2 = "images/characters/rod/sup2.png"

image rod sup3 = "images/characters/rod/sup3.png"

# 音乐 (只使用你提供的文件列表中的)

# music main_theme = "audio/main.mp3"

# 标志位，用于判断玩家是否发现异常

default suspicious_level = 0

default has_gun = False

default prepared_tool = None # 用于选择复仇工具

default trust_level = 0 # 信任度

default investigation_progress = 0 # 调查进度

default contacts_made = 0 # 联系人数量

default money = 1000 # 信用点

default has_enhanced_eyes = False # 是否有强化眼

default has_data_jack = False # 是否有数据接口

default victor_alive = True # 维克多是否还活着

default sara_met = False # 是否遇见萨拉

default kane_deal = False # 是否与凯恩做了交易

default warehouse_discovered = False # 是否发现了仓库

default neural_virus_found = False # 是否发现神经病毒

default final_boss_defeated = False # 是否击败最终Boss

# 开始游戏

label start:

play music "audio/main.mp3"

scene bg_moon_street with dissolve # 场景过渡：月夜街道

"雨。"
"总是下雨。"
"这座城市简直是个地狱，而雨水只会让它变得更糟。"
"它无情而冰冷地撞击着我的头颅。"
"我低声咕哝了一句，将外套裹得更紧些，拉起兜帽盖住头，试图挡住最糟糕的潮湿。"
"浑浊的水流在小巷中蜿蜒而过，带着垃圾和谁也不知道的破碎零件，朝着下水道奔去。"
"霓虹灯在湿漉漉的地面上反射出五光十色的光芒，仿佛为周围的一切披上了一层彩虹的光辉。"
"人们在街上穿梭，有些撑着伞，有些则披着雨衣或戴着帽子，以保持头部的干燥。"
"大多数人只是忍受着潮湿。"
"他们还有其他事情需要担心。"
"我还有其他事情需要担心。"

show rod mid at center with easeinright # 罗德里克出场

R "我是罗德里克。"
R "我年轻，刚满二十吧，其他的有时间再聊。"
R "我是一名探索者，而且还是个年轻的探索者。"
R "我几乎没有什么人脉，线索更是寥寥无几。"
R "今晚或许会改变这一切。"

"我在拥挤的小巷中穿行，目光扫视着四周，寻找我的联系人。"
"街道总是熙熙攘攘，但到了夜晚，更是热闹非凡。"
"合成生物、人类，以及谁知道还有什么其他的存在穿梭于此，进进出出那些似乎占据了这里大部分建筑的酒吧和夜店。"

show rod mid2 at center with dissolve # 切换到思考状态

R "我的心在胸口狂跳，期待与焦虑交织在一起。"
R "我已经寻找这个信息好几个月了，终于有了线索。"

"我眯起眼睛，透过小巷望去，手中的手枪从枪套里抽了出来。"
"墙角处蜷缩着一个身影，背靠着墙壁。"
"我微微眯起眼睛，努力辨认那人是否就是他。"
"在这个城市里，难以分辨，四处都是身披合成纤维的赛博格，他们的衣物在黑暗中闪烁着全息图案，仿佛在夜幕下跳动的光影。"
"但这个却有些不同……"

show rod sup at center with dissolve # 切换到惊讶状态

R "我认识那双眼睛。"
R "全息蓝，像黑暗中的灯笼般闪烁。"

hide rod sup with easeoutleft # 罗德里克退场

show rum mid at right with moveinright # 朗木出场

"我没有给他任何机会。"
"我将他钉在墙上，爪子深深嵌入他的肩膀，逼近他的脸。"

show rod angry at left with moveinleft # 罗德里克愤怒出场

R "你有什么要给我的？"

"朗木的眼睛微微闭合，喉咙一阵起伏，艰难地吞咽着。"

show rum sad at right with dissolve # 朗木变为悲伤状态

L "我……我很抱歉。"

show rod angry2 at left with dissolve # 罗德里克更加愤怒

R "抱歉？你有什么好抱歉的？"

"我低声咆哮，爪子更深地嵌入他的肩膀。"
"朗木痛苦地呜咽了一声，眼睛猛地睁开，带着恐惧与恳求的神情直视着我。"

L "我不知道。"

R "不知道什么？"

"朗木的眼神来回游移，牙齿不停地打颤，努力想要说出什么。"
"终于，他勉强挤出几个字。"

L "我不知道那是什么。"

"他伸手进外套，掏出一个小小的数据芯片，颤抖着递向我。"
"我从他颤抖的手指间夺过来，目光锐利地盯着他。"

hide rod angry2 with dissolve
hide rum sad with dissolve

show rod mid2 at center with dissolve # 罗德里克思考状态

R "我将芯片滑入手腕设备的插槽，调出文件。"
R "屏幕闪烁着亮起，投射出诡异的蓝光，洒落在小巷中。"
R "有一堆加密文件，还有一条视频消息。"

hide rod mid2 with dissolve

scene Solid("#000") with fade # 切换到黑屏，表示观看视频

"我点击播放视频，一个模糊不清的画面跳了出来。那是一个身着白色防护服的高大身影，脸部藏在头盔之后。"

M "罗德里克，如果你看到这条信息，说明我已经成功将芯片交给朗木。"
M "这里面的加密文件包含了一个地址。你必须尽快赶到那里，拿到里面的东西。"
M "记住，不要让任何人知道你要做什么。"
M "但要小心……这座城市里有太多双眼睛在窥视，太多张耳朵在聆听。"
M "信任没有人，包括你最亲近的人。"

scene bg_moon_street with fade # 回到月夜街道

show rod sup2 at center with dissolve # 罗德里克怀疑状态

R "视频到此为止。我抬头看向朗木，但他已经不见踪影。"
R "雨水冲刷着小巷，冷风吹过发出呜咽的声音，只有霓虹灯还在孤独地闪烁。"

hide rod sup2 with dissolve

show rod mid at center with dissolve

R "我将芯片取出，藏进口袋深处。现在，我有了一个目的地，一个未知的任务。"
R "内心深处有个声音告诉我，这将是一场危险的冒险。但我别无选择，只能向前。"

$ investigation_progress += 1

hide rod mid with dissolve

scene bg_street with dissolve # 场景过渡：前往目的地的路上

"解密文件花了我一些时间，但最终我得到了一个坐标。它指向城市边缘的一处废弃仓库。"
"我驾驶飞行摩托，在淅沥的雨幕中穿行。引擎的轰鸣声在寂静的夜色中格外刺耳。"
"当我抵达目的地时，一股不祥的预感袭上心头。"

scene outside with dissolve # 场景过渡：废弃仓库外部

show rod mid at center with moveinbottom

R "仓库看起来空无一人，破旧不堪。"
R "我谨慎地推开吱呀作响的大门，手中紧握着枪。"

hide rod mid with dissolve

scene trainstation with dissolve # 使用废弃车站图片模拟仓库内部

"里面一片漆黑，只有我的机械眼闪烁着红光。"
"突然，我听到一阵细微的声响，似乎有什么东西在黑暗中潜伏。"

show rod sup3 at center with dissolve # 罗德里克警惕状态

R "我打开夜视模式，环视四周。"

"就在这时，一个黑影从阴影中窜出，直扑向我！"

hide rod sup3 with dissolve

menu:
    "立即开火":
        $ has_gun = True
        show rod angry at center with dissolve
        R "我毫不犹豫地扣动扳机，枪火在黑暗中闪烁！"
        "枪声在仓库内回荡，黑影发出一声惨叫，倒在地上。"
        hide rod angry with dissolve
        jump investigate_shadow
    
    "闪避并观察":
        show rod mid2 at center with dissolve
        R "我迅速向一旁闪躲，想要看清攻击者的真面目。"
        "黑影扑空，在地上打了个滚，然后快速爬起身来。"
        hide rod mid2 with dissolve
        jump negotiate_with_shadow
    
    "大声喝止":
        show rod sup at center with dissolve
        R "站住！我没有恶意！"
        "黑影听到我的声音，动作突然停了下来。"
        hide rod sup with dissolve
        jump peaceful_encounter

label investigate_shadow:

show rod mid at center with dissolve

R "我小心翼翼地走向倒下的身影，手枪依然指向他。"
R "这是一个瘦弱的年轻人，身穿破旧的合成纤维外套，脸上满是恐惧。"

show rum sad at right with moveinright # 用朗木的悲伤表情表示受伤的年轻人

L "不……不要杀我……我只是在找食物……"

R "他的声音颤抖着，伤口并不致命，只是擦伤了肩膀。"

hide rod mid with dissolve
hide rum sad with dissolve

show rod mid2 at center with dissolve

R "我意识到自己可能反应过度了。这个城市让每个人都变得神经紧张。"

$ trust_level -= 1
$ suspicious_level += 1

jump explore_warehouse

label negotiate_with_shadow:

show rod mid at left with dissolve
show rum mid at right with moveinright

R "等等！我不是来伤害你的！"

"黑影在昏暗的光线中显露出真面目——一个年轻的女性，她的眼中闪烁着改造过的电子义眼。"

L "你……你是罗德里克？"

show rod sup at left with dissolve

R "你怎么知道我的名字？"

L "有人告诉我你会来这里。我叫萨拉，我是一名地下医生。"

$ sara_met = True
$ contacts_made += 1

hide rod sup with dissolve
hide rum mid with dissolve

show rod mid at left with dissolve
show rum happy at right with dissolve

R "医生？你在这种地方做什么？"

L "我在等你。有人付钱让我给你一样东西。"

"她从背包里掏出一个小型的医疗设备。"

L "这是一个神经强化植入器。它能让你的大脑处理速度提升三倍。"

menu:
    "接受植入器":
        $ has_enhanced_eyes = True
        $ trust_level += 1
        R "这看起来很有用。谢谢你。"
        L "小心使用。副作用可能包括偏执和幻觉。"
        jump explore_warehouse
    
    "拒绝植入器":
        $ suspicious_level += 1
        R "我不相信来路不明的东西。"
        L "明智的选择。在这个城市里，怀疑一切是生存的关键。"
        jump explore_warehouse

label peaceful_encounter:

show rod mid at left with dissolve
show rum sup at right with moveinright

"黑影缓缓站起身来，举起双手表示无害。"

L "别紧张，兄弟。我也是被雇来的。"

R "被谁雇来的？"

L "一个自称维克多的家伙。他说会有人来这里，让我给他带个口信。"

show rod sup2 at left with dissolve

R "维克多？他说了什么？"

L "他说：'游戏才刚刚开始，真正的宝藏不在这里，而在下城区的数据中心。'"

$ investigation_progress += 1

hide rod sup2 with dissolve
hide rum sup with dissolve

jump explore_warehouse

label explore_warehouse:

scene trainstation with dissolve

show rod mid2 at center with dissolve

R "无论刚才发生了什么，我现在需要搜查这个仓库。"
R "既然有人引导我来这里，必然有什么重要的东西。"

hide rod mid2 with dissolve

"我开始仔细搜查仓库的每个角落。"
"在一堆废弃的机械零件后面，我发现了一个隐藏的房间。"
"房间里摆放着先进的计算机设备，屏幕上闪烁着各种数据流。"

show rod sup at center with dissolve

R "这里显然不是普通的废弃仓库。有人在这里进行着什么秘密活动。"

"突然，一个计算机屏幕亮了起来，上面出现了一行文字："
"'如果你看到这条信息，说明你已经通过了第一个测试。'"

hide rod sup with dissolve

scene Solid("#000") with fade

"屏幕上开始播放一段加密视频。"

M "罗德里克，我是维克多。如果你能看到这个，说明你有足够的技能和运气走到这一步。"
M "但这只是开始。这座城市隐藏着一个巨大的阴谋，而你现在已经卷入其中。"
M "在下城区的数据中心，有一个名为'深渊'的程序。它能够控制整个城市的网络系统。"
M "有人想要利用它来控制每一个人的思想。你必须阻止他们。"

scene trainstation with fade

show rod angry at center with dissolve

R "控制思想？这听起来像是科幻小说里的情节。"
R "但在这个充满义体和人工智能的世界里，也许这并不是不可能的事情。"

hide rod angry with dissolve

$ warehouse_discovered = True
$ investigation_progress += 2

menu:
    "立即前往下城区":
        show rod mid at center with dissolve
        R "我不能浪费时间。如果维克多说的是真的，那么每一分钟都很宝贵。"
        hide rod mid with dissolve
        jump downtown_district
    
    "寻找更多线索":
        show rod mid2 at center with dissolve
        R "我需要更多信息才能相信这个故事。让我再仔细搜查一下这里。"
        hide rod mid2 with dissolve
        jump detailed_search
    
    "联系朗木求证":
        show rod sup2 at center with dissolve
        R "朗木给了我那个芯片，也许他知道更多内情。"
        hide rod sup2 with dissolve
        jump contact_langmu

label detailed_search:

scene trainstation with dissolve

show rod mid2 at center with dissolve

R "我决定更仔细地搜查这个隐藏房间。"

"在一个抽屉里，我找到了一叠文件和几张照片。"
"照片显示了几个我不认识的人，但其中一张让我心跳加速——那是朗木，但他看起来完全不同。"
"在照片中，朗木穿着昂贵的西装，站在一群企业高管中间。"

hide rod mid2 with dissolve

show rod sup3 at center with dissolve

R "这不可能……朗木明明是个街头小混混，怎么会出现在企业高管的聚会上？"

"我继续翻阅文件，发现了一个令人震惊的真相："
"朗木的真名是朗木·卡森，他是卡森集团的继承人，而卡森集团正是这座城市最大的义体制造商。"

hide rod sup3 with dissolve

show rod angry2 at center with dissolve

R "他一直在欺骗我！但为什么？一个亿万富翁的儿子为什么要在街头假扮穷人？"

"文件中还提到了一个代号为'深渊计划'的项目。卡森集团正在开发一种能够通过义体植入物控制人类思维的技术。"

hide rod angry2 with dissolve

$ suspicious_level += 3
$ investigation_progress += 2

show rod mid at center with dissolve

R "现在一切都开始有了头绪。朗木接近我，不是偶然，而是计划的一部分。"
R "但我还不清楚他的真正目的是什么。"

hide rod mid with dissolve

jump downtown_district

label contact_langmu:

scene bg_moon_street with dissolve

show rod mid at center with dissolve

R "我走出仓库，拨通了朗木的通讯频道。"
R "奇怪的是，信号竟然无法接通。"

"我试了几次，都是同样的结果。要么朗木关闭了通讯设备，要么……"

hide rod mid with dissolve

show rod sup2 at center with dissolve

R "要么他遇到了麻烦。"

"就在这时，我的腕部设备收到了一条匿名消息："
"'别再找朗木了。他已经不在这个世界上了。如果你想知道真相，来下城区的废弃地铁站。来的时候，一个人来。'"

hide rod sup2 with dissolve

show rod angry at center with dissolve

R "朗木死了？这怎么可能？我几个小时前才见过他！"

$ trust_level -= 2
$ suspicious_level += 2

hide rod angry with dissolve

jump downtown_district

label downtown_district:

scene bg_street2 with dissolve

"下城区是这座城市最黑暗的地方。"
"这里的建筑破败不堪，街道上弥漫着工业废气和人类绝望的味道。"
"霓虹灯在这里很少见，大部分街道都沉浸在昏暗的阴影中。"

show rod mid at center with moveinleft

R "我驾驶飞行摩托穿过狭窄的小巷，寻找维克多提到的数据中心。"
R "在这种地方，每个人都是潜在的敌人。我必须保持警惕。"

hide rod mid with dissolve

"突然，几个身着黑色合成纤维外套的人从巷子里走了出来，挡住了我的去路。"

show rum angry at right with moveinright
show rum angry2 at left with moveinleft

"他们的眼睛闪烁着红色的光芒——那是军用级战斗义眼的标志。"

show rod sup at center with dissolve

R "看来我被包围了。"

"其中一个人走上前来，声音经过电子处理，听起来冰冷而机械："

L "罗德里克，有人想见你。"

hide rod sup with dissolve

menu:
    "跟他们走":
        show rod mid with dissolve
        R "我没有选择。在这种情况下，反抗只会让情况变得更糟。"
        $ trust_level += 1
        hide rod mid with dissolve
        jump meet_the_boss
    
    "试图逃跑":
        show rod mid2 with dissolve
        R "我不能就这样被带走。我必须找到逃脱的机会。"
        hide rod mid2 with dissolve
        jump escape_attempt
    
    "问他们想要什么":
        show rod sup2 with center with dissolve
        R "你们想要什么？谁想见我？"
        hide rod sup2 with dissolve
        jump interrogate_captors

label escape_attempt:

show rod mid at center with dissolve

R "我猛地转身，试图冲向最近的巷子。"

hide rod mid with dissolve

"但这些人显然训练有素。其中一个人迅速移动，挡住了我的去路。"
"另外两个人从侧面包抄过来。"

show rod angry at center with dissolve

R "该死！他们的移动速度太快了，明显经过了军用级义体强化。"

"就在我准备拔枪的时候，一个声音从黑暗中传来："

K "住手！他是我们的客人！"

hide rod angry with dissolve
hide rum angry with dissolve
hide rum angry2 with dissolve

show rum mid at left with moveinleft

"一个高大的身影从阴影中走出来。他穿着昂贵的西装，但左臂明显是机械义肢。"

L "我是凯恩，这片区域的负责人。很抱歉我的手下吓到了你，罗德里克。"

show rod sup2 at right with moveinright

R "你怎么知道我的名字？"

show rum happy at left with dissolve

L "在这座城市里，信息就是力量。而你，最近成了一个很有趣的信息。"

$ kane_deal = True
$ contacts_made += 1

hide rod sup2 with dissolve
hide rum happy with dissolve

jump meet_the_boss

label interrogate_captors:

show rod sup2 at center with dissolve

R "你们想要什么？谁想见我？"

show rum mid at right with moveinright

"其中一个人脱下头盔，露出一张被大面积义体改造过的脸。"

L "我们的老板对你很感兴趣。尤其是你最近的活动。"

R "什么活动？"

L "别装傻。你在废弃仓库里发现的东西，已经让某些人很不安。"

hide rod sup2 with dissolve
hide rum mid with dissolve

show rod angry at center with dissolve

R "看来我的行动并不像我想象的那么秘密。"

hide rod angry with dissolve

jump meet_the_boss

label meet_the_boss:

scene outside with dissolve

"他们带我来到一个看起来像是废弃工厂的建筑。"
"但走进去后，我发现里面完全是另一番景象。"
"高科技设备随处可见，全息屏幕显示着整个城市的实时监控画面。"

show rod sup at center with dissolve

R "这里简直就像是一个军事指挥中心。"

hide rod sup with dissolve

"他们把我带到一个巨大的办公室，办公桌后坐着一个中年女性。"
"她的双眼完全被义眼替代，闪烁着冰蓝色的光芽。"

show rum mid at center with dissolve

L "欢迎，罗德里克。我是这个组织的领导者。你可以叫我指挥官。"

show rod mid at left with moveinleft

R "什么组织？"

show rum sup at center with dissolve

L "我们是反抗军。我们致力于阻止卡森集团的深渊计划。"

show rod sup2 at left with dissolve

R "反抗军？深渊计划？看来我真的卷入了什么大事件。"

hide rod sup2 with dissolve
hide rum sup with dissolve

show rod mid at left with dissolve
show rum mid at center with dissolve

L "朗木·卡森一直在监视你。他想利用你来测试深渊计划的效果。"
L "但我们截获了他的通讯，决定先一步接触你。"

R "所以朗木真的是卡森集团的人？"

L "不仅如此，他还是深渊计划的主要开发者之一。"

$ investigation_progress += 3

hide rod mid with dissolve
hide rum mid with dissolve

menu:
    "询问深渊计划详情":
        show rod mid2 at center with dissolve
        R "告诉我更多关于深渊计划的事情。"