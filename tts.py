import os
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechSynthesisOutputFormat
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                       region=os.environ.get('SPEECH_REGION'))
speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat.Audio48Khz192KBitRateMonoMp3)
# audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
# speech_config.speech_synthesis_language = 'zh-CN'
audio_config = speechsdk.audio.AudioOutputConfig(filename="voice.mp3")
# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name = 'zh-CN-YunzeNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# text = """大家好，技术宅就是我，我就是老王。
# Hello world写好了就能年薪百万，搞不好还能达到人生巅峰，迎娶白富美？不管你信不信，反正我是信了。
# 如果你真的以为Hello world就是这个。。。。那你的想法真的是，太傻太天真了。
# 今天我们就来看一下各种千奇百怪的hello world。
# 大家请注意听，“hello world！”。
# 哈哈，这就是我要给大家说的第一个Hello world！
# 也许你已经发现了，我今天的声音和以前不一样了。
# 其实你现在听到的声音是我通过TTS转换而来的。
# 惊不惊喜，意不意外！
# 下面我们来一起看一下，老王我绞尽脑汁想出来的所有Hello world。
# 如果每一种你都能信手拈来，那我觉得你离年薪百万应该也不远了。
# 如果大家想出了新的Hello world，也欢迎留言。咱们再出个Hello world第二期！
#
# """
text = '这个是利用装饰器写的Hello world。装饰器是一个很著名的设计模式。' \
       'python中所谓的面相切面的编程，指的就是装饰器。'

# text = """
# 怎么样？有点意思吧？
# 这可是老王我花了整整一个星期，想出的各种Hello world的花式写法。
# 里面涉及到了很多我们未来会更加深入学习到的技术和概念。
# 不瞒您说，老王我就是凭借着这些技术和概念，找到了一份收入不错的工作。
# 虽然达不到年薪百万，但我却迎娶了白富美。嘿嘿。
# 如果你想快速学习python，请订阅我的频道。
# 今天关于Hello world就聊到这里，拜拜。
#
# """
speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
# speech_synthesizer.speak_text_async(text)
# if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#     print("Speech synthesized for text [{}]".format(text))
# elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#     cancellation_details = speech_synthesis_result.cancellation_details
#     print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#     if cancellation_details.reason == speechsdk.CancellationReason.Error:
#         if cancellation_details.error_details:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")
