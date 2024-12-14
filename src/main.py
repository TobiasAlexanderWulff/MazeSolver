from window import Window


def main():
    win = Window(720, 480)
    win.running = True
    win.wait_for_close()


if __name__ == "__main__":
    main()
