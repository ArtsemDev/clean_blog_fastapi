from fastapi import APIRouter, Request, HTTPException, Depends, BackgroundTasks
from fastapi.responses import HTMLResponse
from sqlalchemy import select

from core.models import Post
from core.schemas import ContactSchema
from .templating import templates


blog_router = APIRouter()


def send_email(to: str, message: str):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    msg = MIMEMultipart()
    msg['From'] = 'pratayeu@yandex.ru'
    msg['To'] = to
    msg['Subject'] = 'Тест скрипта SMTP'
    message = message
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.yandex.ru', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('pratayeu@yandex.ru', 'ljzlwbhdzmdpdrbg')
    mailserver.sendmail('pratayeu@yandex.ru', to, msg.as_string())


@blog_router.get('/', response_class=HTMLResponse, name='blog_index')
async def index(request: Request):
    objs = await Post.scalars(select(Post).order_by(Post.date_created))
    return templates.TemplateResponse('index.html', {'request': request, 'posts': objs})


@blog_router.get('/about', response_class=HTMLResponse, name='blog_about')
async def about(request: Request):
    return templates.TemplateResponse('about.html', {'request': request})


@blog_router.get('/contact', response_class=HTMLResponse, name='blog_contact')
async def contact(request: Request):
    return templates.TemplateResponse('contact.html', {'request': request})


@blog_router.post('/contact', response_class=HTMLResponse)
async def contact(
        request: Request,
        background_tasks: BackgroundTasks,
        contact_form: ContactSchema = Depends(ContactSchema.as_form),
):
    if isinstance(contact_form, ContactSchema):
        error = ''
        success = True
        background_tasks.add_task(send_email, contact_form.email, contact_form.message)
    else:
        error = contact_form
        success = False
    return templates.TemplateResponse('contact.html', {'request': request, 'error': error, 'success': success})


@blog_router.get('/{post_slug}', response_class=HTMLResponse, name='post_detail')
async def detail(request: Request, post_slug: str):
    post = await Post.scalars(select(Post).filter(Post.slug == post_slug))
    if post:
        return templates.TemplateResponse('post.html', {'request': request, 'post': post[0]})
    raise HTTPException(status_code=404)
