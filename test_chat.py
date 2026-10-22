from chat import ChatBot


def test_history_empty():
    bot = ChatBot("Você é um tutor, paciente que responde em português",None)
    assert bot.save_chat == []

def test_reset():
    bot = ChatBot("Você é um tutor, paciente que responde em português",None)
    bot.save_chat.append({"role":"user","content":"test"})
    assert len(bot.save_chat) == 1
    bot.reset()
    assert bot.save_chat == []

def test_save(tmp_path):
    bot = ChatBot("Você é um tutor, paciente que responde em português",None)
    bot.save_chat.append({"role":"user","content":"test"})
    bot.save(tmp_path / "test.json")
    assert (tmp_path/"test.json").exists()