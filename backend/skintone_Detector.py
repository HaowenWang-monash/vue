import torch
import torchvision.transforms as transforms
import torch.nn as nn
from PIL import Image



#CNN model
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 32 * 32, 128)
        self.fc2 = nn.Linear(128, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)  # Flatten
        x = self.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# Model Initialization
model = CNN()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
# Load the saved model

model.load_state_dict(torch.load("human_classifier.pth"))
model.eval()

# Transform the data for the model
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

#open image
image_path = "face2.jpg"

image = Image.open(image_path)

image = transform(image).unsqueeze(0)

with torch.no_grad():
    output = model(image)
    prediction = (output.item() < 0.5)

if prediction:
    print("The image contains a human face.")
else:
    print("The image does not contain a human face.")

if prediction:

    #CNN initals
    class CNN(nn.Module):
        def __init__(self):
            super(CNN, self).__init__()
            self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
            self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
            self.pool = nn.MaxPool2d(2, 2)

            self.fc1 = nn.Linear(64 * 32 * 32, 256)  # Fixed input size
            self.fc2 = nn.Linear(256, 4)  # 3 classes (Black, White, Brown)
            self.relu = nn.ReLU()

        def forward(self, x):
            x = self.pool(self.relu(self.conv1(x)))
            x = self.pool(self.relu(self.conv2(x)))

            x = x.view(x.size(0), -1)
            x = self.relu(self.fc1(x))
            x = self.fc2(x)
            return x


    # Model Initialization
    model = CNN()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    model.load_state_dict(torch.load("skintone_classifier2.pth"))
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((128, 128)),  # Resize to match training size
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))  # Use the same normalization
    ])

    # Load and transform the image

    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)  # Add batch dimension

    # Predict
    with torch.no_grad():
        output = model(image)
        predicted_class = torch.argmax(output).item()

    # Map class index to label
    class_names = ["dark", "light", "mid-dark", "mid-light"]
    print(f"Predicted Skin Tone: {class_names[predicted_class]}")