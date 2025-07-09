import shutil

from cyclopts import App, Parameter
from loguru import logger

from tools import configs
from tools.configs import path_define, options
from tools.configs.options import FontFormat
from tools.services import font_service, publish_service

app = App(
    version=configs.version,
    default_parameter=Parameter(consume_multiple=True),
)


@app.default
def main(
        cleanup: bool = False,
        font_formats: set[FontFormat] | None = None,
):
    if font_formats is None:
        font_formats = options.font_formats
    else:
        font_formats = sorted(font_formats, key=lambda x: options.font_formats.index(x))

    logger.info('cleanup = {}', cleanup)
    logger.info('font_formats = {}', font_formats)

    if cleanup and path_define.build_dir.exists():
        shutil.rmtree(path_define.build_dir)
        logger.info("Delete dir: '{}'", path_define.build_dir)

    dump_logs = font_service.dump_fonts(font_formats)
    publish_service.make_release_zips(dump_logs, font_formats)

    if 'otf.woff2' in font_formats:
        publish_service.update_www(dump_logs)


if __name__ == '__main__':
    app()
