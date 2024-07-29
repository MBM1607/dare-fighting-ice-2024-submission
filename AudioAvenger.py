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
        self.just_init = True
        self.actions = (
            "AIR_A",
            "AIR_B",
            "AIR_D_DB_BA",
            "AIR_D_DB_BB",
            "AIR_D_DF_FA",
            "AIR_D_DF_FB",
            "AIR_DA",
            "AIR_DB",
            "AIR_F_D_DFA",
            "AIR_F_D_DFB",
            "AIR_FA",
            "AIR_FB",
            "AIR_UA",
            "AIR_UB",
            "BACK_JUMP",
            "BACK_STEP",
            "CROUCH_A",
            "CROUCH_B",
            "CROUCH_FA",
            "CROUCH_FB",
            "CROUCH_GUARD",
            "DASH",
            "FOR_JUMP",
            "FORWARD_WALK",
            "JUMP",
            "NEUTRAL",
            "STAND_A",
            "STAND_B",
            "STAND_D_DB_BA",
            "STAND_D_DB_BB",
            "STAND_D_DF_FA",
            "STAND_D_DF_FB",
            "STAND_D_DF_FC",
            "STAND_F_D_DFA",
            "STAND_F_D_DFB",
            "STAND_FA",
            "STAND_FB",
            "STAND_GUARD",
            "THROW_A",
            "THROW_B",
        )
        self.permitted_actions = (
            "THROW_B",
            "CROUCH_FB",
            "AIR_F_D_DFB",
        )

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

        if self.just_init:
            self.just_init = False
            action = "FORWARD_WALK"
        else:
            action = np.random.choice(self.permitted_actions)

        self.cc.command_call(action)
        self.inputKey = self.cc.get_skill_key()

    def round_end(self, round_result: RoundResult):
        logger.info(f"round end: {round_result}")
        just_init = False

    def game_end(self):
        logger.info("game end")
