import reflex as rx
# import requests as rq
import re

class LoginState(rx.State):
  loader: bool = False
  username: str = "example@mail.com"
  password: str 
  error = False
  response: dict = {}

  # @rx.background
  def loginService(self, data: dict):
    # async with self:
    #   self.loader = True
    #   self.error = False
    print("Datos enviados:", data)
      #response = rq.post('http//localhost:3001/auth/login', json=data, headers={'Content-Type': 'application/json'})

      # if response.status_code == 200:
      #   self.response = response.json()
      #   self.loader = False
      #   return rx.redirect('/home')
      # else:
      #   self.loader = False
      #   self.error = True
      #   return rx.message("Error al iniciar sesion, verifique sus credenciales", color="red")
  
  @rx.var
  def user_invalid(self) -> bool:
    return not(re.match(r"[^@]+@[^@]+.[^@]+", self.username) and "example@email.com")
  
  @rx.var
  def user_empty(self) -> bool:
    return not self.username.strip()
  
  @rx.var
  def password_empty(self) -> bool:
    return not (self.password.strip())
  
  @rx.var
  def validate_fields(self) -> bool:
    return (
      self.user_empty
      or self.user_invalid
      or self.password_empty
    )

@rx.page(route='/login', title='Login')
def login() -> rx.Component:
  return rx.section(
    rx.flex(
      rx.image(src="https://cdn-icons-png.flaticon.com/512/25/25231.png", width="300px", border_radius="15px, 50px"),
      rx.heading("Inicio de Sesion", size="1", text_align="center"),
      rx.form.root(
        rx.flex(
          field_form_component_general(
            "Usuario",
            "Ingrese su correo",
            "Ingrese un correo valido",
            "username",
            LoginState.set_username,
            LoginState.user_invalid
          ),
          field_form_component(
            "Contraseña",
            "Ingrese su contraseña",
            "password",
            LoginState.set_password,
            "password"
          ),
          rx.form.submit(
            rx.cond(
              LoginState.loader,
              rx.spinner(color="red", size="2"),
              rx.button(
                "Iniciar Sesion",
                disabled=LoginState.validate_fields,
                width="30vw"
              ),
            ),
            as_child=True
          ),
          direction="column",
          justify="center",
          align="center",
          spacing="2",
        ),
        rx.cond(
          LoginState.error,
          rx.callout(
            "Credenciales Incorrectas",
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            style={"margin-top": "10px"}
          ),
          None
        ),
        on_submit=LoginState.loginService,
        reset_on_submit=True,
        width="80%",
      ),
      width="100%",
      direction="column",
      align="center",
      justify="center",
    ),
    style=style_section,
    justify="center",
    width="100%",
  )


def field_form_component(label:str, placeholder:str, name_var:str, on_change_function, type_field:str) -> rx.Component:
  return rx.form.field(
    rx.flex(
      rx.form.label(label),
      rx.form.control(
        rx.input(
          placeholder=placeholder,
          on_change=on_change_function,
          name=name_var,
          type=type_field,
          required=True
        ),
      as_child=True,
      ),
      rx.form.message(
        "El campo no puede ser nulo",
        match="valueMissing",
        color="red"
      ),
      direction="column",
      spacing="2",
      align="stretch"
    ),
    name=name_var,
    width="30vw"
  )

def field_form_component_general(label: str, placeholder: str, message_validate: str, name: str, on_change_function, show ) -> rx.Component:
  return rx.form.field(
    rx.flex(
      rx.form.label(label),
      rx.form.control(
        rx.input(
          placeholder=placeholder,
          on_change=on_change_function,
          name=name,
          required=True
        ),
        as_child=True,
      ),
      rx.form.message(
        message_validate,
        name=name,
        match="valueMissing",
        force_match=show,
        color="red"
      ),
      direction="column",
      spacing="2",
      align="stretch"
    ),
    name=name,
    width="30vw"
  )

style_section = {
  "height": "90vh",
  "width": "80%",
  "margin": "auto",
}