import reflex as rx
import httpx

class StateApiRick(rx.State):

  listPers: list[dict] = []
  error: str = ""

  async def getRickAndMorty(self):
    try:
      async with httpx.AsyncClient() as client:
        response = await client.get("https://rickandmortyapi.com/api/character")
        response.raise_for_status()
        self.listPers = response.json().get('results', [])
    except Exception as e:
        self.error = f"Error: {str(e)}"


@rx.page(route='/rick_and_morty', title='Rick and Morty', on_load=StateApiRick.getRickAndMorty)
def rickAndMorty() -> rx.Component:
  return rx.vstack(
    rx.heading('Rick and Morty'),
    rx.foreach(StateApiRick.listPers,
        lambda person: rx.card(
          # rx.box(
          #   rx.text(person['id']),
          #   align_items="center",
          #   justify_content="center",  
          #   height="100%",  
          #   style={
          #     "display": "flex", 
          #     "flexDirection": "column", 
          #   }
          # ),
            rx.image(src=person['image'], width='100px'),
            rx.text(person['name']),
            rx.text(f"Species: {person['species']}"),
            rx.text(f"Status: {person['status']}"),

        )
    ),
    align_items="center",
    justify_content="center", 
    height="100%",
  )

