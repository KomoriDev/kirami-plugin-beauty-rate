import base64
from io import BytesIO

from nonebot import require
from nonebot.typing import T_State

from kirami.utils.request import Request
from kirami.typing import MessageEvent, MessageSegment

require("nonebot_plugin_alconna")
from arclet.alconna.args import Args
from arclet.alconna.core import Alconna
from arclet.alconna.typing import CommandMeta

from nonebot_plugin_alconna import Match, on_alconna, AlconnaArg, AlconnaMatch
from nonebot_plugin_alconna.matcher import AlconnaMatcher
from nonebot_plugin_alconna.adapters import Image

from .config import API_KEY, SECRET_KEY
from .utils import FaceRecognition


face_val = on_alconna(
    Alconna(
        "颜值评分",
        Args["img?", Image],
        meta=CommandMeta(
            description="让bot为你的颜值打分！",
            usage="颜值评分 [图片]",
            example="颜值评分 [图片]",
            author="Komorebi",
            compact=True
        )
    ),
    aliases={"颜值打分"}
)


@face_val.handle()
async def get_pic(
    matcher: AlconnaMatcher, image: Match[Image] = AlconnaMatch("img")
):
    if image.available:
        matcher.set_path_arg("img", image.result)


@face_val.got_path("img", prompt="请发送照片")
async def get_avatar_img(state: T_State, image: Image = AlconnaArg("img")):
    if image.url:
        state["img"] = image.url
    else:
        state["img"] = image.id


@face_val.handle()
async def score(event: MessageEvent, state: T_State):
    img_url = state.get("img")
    if img_url is None:
        await face_val.finish("没有找到图片！", at_sender=True)
    res = await Request.get(img_url)

    img_b64_str = base64.b64encode(res.content).decode()

    faces = FaceRecognition(img_b64_str, API_KEY, SECRET_KEY)
    result = await faces.face_beauty()

    if result["error_msg"] == "pic not has face":
        await face_val.finish("未从图片中识别到人脸！", at_sender=True)
    elif result["error_msg"] == "image size is too large":
        await face_val.finish("图片尺寸过大！", at_sender=True)

    faces_gender = []
    faces_pos = []
    faces_beauty = []
    try:
        for face in result["result"]["face_list"]:
            faces_gender.append("男" if face["gender"]["type"] == "male" else "女")
            faces_pos.append(face["location"])
            faces_beauty.append(face["beauty"])
    except (KeyError, TypeError):
        await face_val.finish("请重新检查指令！", at_sender=True)

    pic = res.content
    pic_bytes_stream = BytesIO(pic)
    buf = BytesIO()
    await faces.draw_face_rects(pic_bytes_stream, buf, faces_pos)

    msg = "\n".join([f"Face{i + 1}:\n"
                    f"性别: {gender}\n"
                    f"颜值评分: {beauty}/100"
                    for i, (gender, beauty) in enumerate(zip(faces_gender, faces_beauty))])
    await face_val.send(MessageSegment.reply(event.message_id) + msg, at_sender=True)

    pic_bytes_stream.close()
    buf.close()
