def on_chat(num1, num2, num3):
    if True:
        text_list: List[str] = []
		text_list = ["a", "b", "c"]
        text_list += 1
    player.say(CHICKEN)
    agent.teleport_to_player()
player.on_chat("run", on_chat)
def travelled_walk():
    mobs.kill(mobs.target(ALL_ENTITIES))
player.on_travelled(WALK, travelled_walk)
def item_interacted_iron_shovel():
    builder.move(FORWARD, 1)
    blocks.place(BEDROCK, pos(0, 0, 0))
    gameplay.set_weather(RAIN)
    gameplay.set_game_mode(SURVIVAL, mobs.target(NEAREST_PLAYER))
player.on_item_interacted(IRON_SHOVEL, item_interacted_iron_shovel)