# Audio Avenger

![Audio Avenger](./audio-avenger.svg)

DareFightingICE 2024 AI competition entry by Muhammad Khan. This is a Blind AI that ignores
all information about the game and only uses prebuilt probability move tables based on the
move's hitbox, speed, and damage.

## File Description

- `DisplayInfo.py` is an example AI that utilizes screen data as input.
- `AudioAvenger.py` is the main submission file that contains the AI logic.
- `OneSecondAI.py` is an example AI that utilizes multi-threading to achieve a processing time of one second.
- `Main_PyAIvsPyAI.py` is the script to run two instances of the Python AI and set up the game. This is when both AI are implemented using Python
- `Main_SinglePyAI.py` is the script to run a single instance of the Python AI, e.g. when the opposing AI is not implemented using Python.

## Instruction

- First, install our interface on implementing python AI using `pip`. (Python version >= 3.10 required)

```bash
pip install -r requirements.txt
```

## Instruction on using Main_PyAIvsPyAI.py

- Boot DareFightingICE with option `--grpc-auto`.
- Execute `Main_PyAIvsPyAI.py` to connect to the DareFightingICE platform where `port` is the exposed port of DareFightingICE (optional).

```bash
python Main_PyAIvsPyAI.py --port {port}
```

## Instruction on using Main_SinglePyAI.py

- Boot DareFightingICE.
- To run a single instance of the Python AI, refer to `Main_SinglePyAI.py`.
- Execute `Main_SinglePyAI.py`, the following example shows how to use AudioAvenger as player 1 and KickAI as player 2.

```bash
python Main_SinglePyAI.py --a1 AudioAvenger --a2 KickAI
```
