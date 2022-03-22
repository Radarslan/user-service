from fastapi import APIRouter

from app.api.v1.endpoints.emails import router as emails_router
from app.api.v1.endpoints.health_check import router as health_check_router
from app.api.v1.endpoints.phone_numbers import router as phone_numbers_router
from app.api.v1.endpoints.users import router as users_router

PREFIX = "/users"
api_router = APIRouter()
api_router.include_router(health_check_router)
api_router.include_router(emails_router, prefix=PREFIX)
api_router.include_router(phone_numbers_router, prefix=PREFIX)
api_router.include_router(users_router, prefix=PREFIX)


# module_path = ["app", "api", "v1", "endpoints"]
# modules_tree = os.listdir(os.path.abspath(os.path.join(*module_path)))
# for module_name in modules_tree:
#     if "__" not in module_name:
#         module_base_name = module_name.split(".")[0]
#         absolute_module_path = ".".join(module_path) + "." + module_base_name
#         module = importlib.import_module(absolute_module_path)
#         for attribute_name in dir(module):
#             if "_" not in attribute_name and attribute_name == "router":
#                 attribute = getattr(module, attribute_name)
#                 api_router.include_router(
#                     attribute, prefix=f"/{module_base_name}"
#                 )
