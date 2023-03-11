# -*- coding: utf-8 -*-
from pydantic import BaseSettings, Field, HttpUrl


class Settings(BaseSettings):
    token: str = Field(..., env='BOT_TOKEN')
    webhook_url: HttpUrl = Field(..., env='WEBHOOK_URL')
    webapp_port: int = Field(7891, env='WEBAPP_PORT')

    class Config:
        env_file = '.env'
