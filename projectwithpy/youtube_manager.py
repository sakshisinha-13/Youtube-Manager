import json

def load_data():
    """
    Loads video data from 'youtube.txt'.
    
    Returns:
        list: A list of video dictionaries.
    """
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    finally:
        pass

def save_data_helper(videos):
    """
    Saves the list of videos to 'youtube.txt'.
    
    Args:
        videos (list): The list of video dictionaries to be saved.
    """
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    """
    Prints all video entries with names and durations.
    
    Args:
        videos (list): The list of video dictionaries.
    """
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index} , {video['name']} , Duration: {video['time']}")
    print("\n")
    print("*" * 50)

def add_video(videos):
    """
    Prompts user to add a new video entry.
    
    Args:
        videos (list): The list of video dictionaries to be updated.
    """
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    """
    Allows user to update details of an existing video.
    
    Args:
        videos (list): The list of video dictionaries to be updated.
    """
    list_all_videos(videos)
    index = input("Enter the video number to update: ")

    try:
        index = int(index)  # Convert input to integer
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            videos[index - 1] = {'name': name, 'time': time}
            save_data_helper(videos)
        else:
            print("Invalid index selected.")
    except ValueError:
        print("Please enter a valid number.")

def delete_video(videos):
    """
    Enables user to delete a video entry.
    
    Args:
        videos (list): The list of video dictionaries to be updated.
    """
    list_all_videos(videos)
    index = input("Enter the video number to be deleted: ")

    try:
        index = int(index)  # Convert input to integer
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
        else:
            print("Invalid video index selected.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """
    Manages user input and application flow.
    """
    videos = load_data()

    while True:
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
