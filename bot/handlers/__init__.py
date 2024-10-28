from bot.dispacher import dp
from bot.handlers.main_handler import main_router
from bot.handlers.backup import routine
from bot.handlers.payment import payment

dp.include_routers(*[
    main_router,
    routine,
    payment
])
