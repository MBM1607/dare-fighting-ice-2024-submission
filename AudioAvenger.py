import logging

import numpy as np
from pyftg import (
    AIInterface,
    AudioData,
    CommandCenter,
    FrameData,
    GameData,
    Key,
    RoundResult,
    ScreenData,
)

logger = logging.getLogger(__name__)


class AudioAvenger(AIInterface):
    def __init__(self):
        super().__init__()
        self.blind_flag = True

        self.action_weights = {
            "JUMP": 0.0625,
            "FOR_JUMP": 0.0625,
            "BACK_JUMP": 0.0625,
            "STAND_GUARD": 0.0625,
            "CROUCH_FB": 0.15,
            "AIR_UB": 0.15,
            "STAND_F_D_DFB": 0.3,
            "AIR_D_DF_FB": 0.15,
        }

    def name(self) -> str:
        return self.__class__.__name__

    def is_blind(self) -> bool:
        return self.blind_flag

    def initialize(self, game_data: GameData, player_number: int):
        logger.info("initialize")
        self.cc = CommandCenter()
        self.key = Key()
        self.player = player_number

    def get_non_delay_frame_data(self, frame_data: FrameData):
        pass

    def input(self) -> Key:
        return self.key

    def get_information(self, frame_data: FrameData, is_control: bool):
        self.frame_data = frame_data
        self.cc.set_frame_data(self.frame_data, self.player)

    def get_screen_data(self, screen_data: ScreenData):
        self.screen_data = screen_data

    def get_audio_data(self, audio_data: AudioData):
        self.audio_data = audio_data

    def processing(self):
        if self.frame_data.empty_flag or self.frame_data.current_frame_number <= 0:
            return

        if self.cc.get_skill_flag():
            self.key = self.cc.get_skill_key()
        else:
            self.key.empty()
            self.cc.skill_cancel()

            action = np.random.choice(
                list(self.action_weights.keys()),
                p=list(self.action_weights.values()),
            )

            self.cc.command_call(action)

    def round_end(self, round_result: RoundResult):
        logger.info(f"round end: {round_result}")

    def game_end(self):
        logger.info("game end")
