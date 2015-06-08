
def main():
    import argparse                                                              
    from pushbullet import Pushbullet
    parser = argparse.ArgumentParser('hexflash')                                 
    parser.add_argument('-t', nargs='?', help='Title for alert')                     
    parser.add_argument('alert_text', help='Text to alert with Pushbullet')                     
    args = parser.parse_args()                                                   
    with open('api_key') as f:
        api_key = f.readline().strip()
    pb = Pushbullet(api_key)
    push = pb.push_note("", args.alert_text)


if __name__ == "__main__":
    main()

