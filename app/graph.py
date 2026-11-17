
from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from openai import OpenAI

client = OpenAI()


class InventionState(TypedDict):
    words: list[str]
    inventor: str
    engineer: str
    investor: str


def ask_ai(instructions: str, message: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        input=message,
        max_output_tokens=400,
    )
    return response.output_text


def inventor_agent(state: InventionState):
    result = ask_ai(
        "Sen cilgin ve komik bir mucitsin. "
        "Turkce, kisa ve yaratici cevap ver.",
        f"Su uc kelimeden sacma bir icat uret: "
        f"{', '.join(state['words'])}. "
        "Icat adi, ne ise yaradigi, nasil calistigi "
        "ve komik bir slogan yaz."
    )
    return {"inventor": result}


def engineer_agent(state: InventionState):
    result = ask_ai(
        "Sen huysuz ve esprili bir muhendissin. "
        "Icatlari komik sekilde elestiriyorsun. "
        "Turkce ve kisa cevap ver. Puanlama yapma.",
        f"Bu icadi incele ve mantiksizliklariyla dalga gec:\n\n"
        f"{state['inventor']}"
    )
    return {"engineer": result}


def investor_agent(state: InventionState):
    result = ask_ai(
        "Sen asiri ozguvenli, komik bir yatirimcisin. "
        "En sacma urunu bile satabilecegine inaniyorsun. "
        "Turkce ve kisa cevap ver. Puanlama yapma.",
        f"Icat:\n{state['inventor']}\n\n"
        f"Muhendisin elestirisi:\n{state['engineer']}\n\n"
        "Bu urunu satmak icin komik bir reklam konusmasi yap. "
        "Sonunda yatirim yapip yapmayacagini soyle."
    )
    return {"investor": result}


builder = StateGraph(InventionState)

builder.add_node("inventor", inventor_agent)
builder.add_node("engineer", engineer_agent)
builder.add_node("investor", investor_agent)

builder.add_edge(START, "inventor")
builder.add_edge("inventor", "engineer")
builder.add_edge("engineer", "investor")
builder.add_edge("investor", END)

invention_graph = builder.compile()
