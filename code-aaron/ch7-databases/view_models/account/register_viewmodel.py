from view_models.shared.viewmodel import ViewModelBase
from fastapi import Request
from typing import Optional


class RegisterViewModel(ViewModelBase):
    def __init__(
        self,
        request: Request,
    ):
        super().__init__(request)
        self.email: Optional[str] = None
        self.name: Optional[str] = None
        self.password: Optional[str] = None
        self.age: Optional[int] = None

    async def load(self):
        form = await self.request.form()
        self.name = form.get("name")
        self.password = form.get("password")
        self.email = form.get("email")
        self.age = form.get("age")
        if not self.name or not self.name.strip():
            self.error = "Your name is required."
        elif not self.email or not self.email.strip():
            self.error = "Your email is required."
        elif not self.password or not len(self.password) > 5:
            self.error = "Your password is required and must be at least 5 characters."
