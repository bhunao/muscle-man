from fastapi import APIRouter, Request

from app.core.main import templates


router = APIRouter()


@router.get("/")
async def base_endpoint(request: Request):
    return templates.TemplateResponse(
        name="login.html",
        context=dict(
            request=request,
        ),
    )
