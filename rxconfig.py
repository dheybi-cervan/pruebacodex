import reflex as rx

config = rx.Config(
    app_name="dheybicervan_app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
