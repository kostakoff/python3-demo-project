"""Command‑line interface for demo_flask"""
import argparse
from werkzeug.serving import run_simple
from .version import __version__
from .app import create_app


def main():
    parser = argparse.ArgumentParser(description="demo_flask utility")
    parser.add_argument("--version", action="store_true", help="Show application version and exit")
    parser.add_argument("--serve", action="store_true", help="Run the Flask web server")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind (default: 0.0.0.0)")
    parser.add_argument("--port", default=5000, type=int, help="Port to bind (default: 5000)")
    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    if args.serve:
        app = create_app()
        run_simple(args.host, args.port, app, use_reloader=True, threaded=True)
        return

    parser.print_help()


if __name__ == "__main__":
    main()
