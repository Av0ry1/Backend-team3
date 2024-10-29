from fastapi import APIRouter,Form
import smtplib

#"baraholka_technical_sup", "P2OkhyPYi1t-"

router = APIRouter()


@router.post(path="/reset/")
async def reset(
        email: str = Form(),
):
        smtpSession = smtplib.SMTP('smtp.gmail.com', 587)
        smtpSession.ehlo()
        smtpSession.starttls()
        smtpSession.login("baraholka_technical_sup@mail.ru", "P2OkhyPYi1t-")
        message = """Вы или кто-то другой запросили восстановление пароля для вашей учетной записи на нашем сайте. Если вы не запрашивали восстановление пароля, просто проигнорируйте это письмо и ваш пароль останется прежним.

    Если вы действительно хотите сбросить свой пароль, просто нажмите на следующую кнопку:

    [Сбросить пароль]

    Эта ссылка для однократного использования истекает через 1 час.

    Если у вас возникли какие-либо вопросы, пожалуйста, не стесняйтесь связаться с нами.

    С уважением,
    Команда сайта."""
        smtpSession.sendmail("baraholka_technical_sup", email, message)
        smtpSession.quit()